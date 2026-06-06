import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import (
    agent_key,
    archive_conversation,
    default_filters,
    delete_conversation,
    list_archived,
    stream_create_async,
    update_title_async,
)
from pipeshub_sdk.errors.errorresponse import ErrorResponse
from pipeshub_sdk.errors.responsevalidationerror import ResponseValidationError

COUNT = 20
BATCH_SIZE = 10


def title(n: int) -> str:
    return f"conv {n}"


def conv_num(t: str) -> int:
    return int(t.removeprefix("conv "))


def conv_batch(t: str) -> int:
    return 1 if conv_num(t) <= BATCH_SIZE else 2


def ok(label: str, passed: bool, detail: str = "") -> bool:
    mark = "PASS" if passed else "FAIL"
    extra = f" ({detail})" if detail else ""
    print(f"  [{mark}] {label}{extra}")
    return passed


def list_convs(sdk, **kwargs):
    return sdk.agents.list_agent_conversations(agent_key=agent_key(), **kwargs)


def list_convs_archived(sdk, archived: bool, **kwargs):
    return list_convs(sdk, is_archived="true" if archived else "false", **kwargs)


def titles(res) -> list[str]:
    return [c.title or "" for c in res.conversations]


def safe_delete(sdk, conv_id: str) -> None:
    try:
        delete_conversation(sdk, conv_id)
    except (ResponseValidationError, ErrorResponse):
        pass


def cleanup_conv_titled(sdk) -> None:
    for _ in range(30):
        removed = False
        for conv in list_convs(sdk, limit=100, search="conv ").conversations:
            if conv.id:
                safe_delete(sdk, conv.id)
                removed = True
        for conv in list_archived(sdk):
            if (conv.title or "").startswith("conv ") and conv.id:
                safe_delete(sdk, conv.id)
                removed = True
        if not removed:
            break
    remaining = list_convs(sdk, limit=1, search="conv ").pagination.total_count
    if remaining:
        raise RuntimeError(f"cleanup left {remaining} conv-titled conversations")


async def wait_for_search_count(sdk, expected: int, *, search: str) -> None:
    for _ in range(30):
        if list_convs(sdk, limit=100, search=search).pagination.total_count == expected:
            return
        await asyncio.sleep(1)
    count = list_convs(sdk, limit=100, search=search).pagination.total_count
    raise RuntimeError(f"timed out waiting for {expected} conversations matching {search!r}, got {count}")


async def create_one(sdk, n: int) -> str:
    cid, _, _, _ = await stream_create_async(sdk, f"ping {n}", default_filters(), print_bot=False)
    await update_title_async(sdk, cid, title(n))
    return cid


async def create_conversations(sdk) -> list[str]:
    ids: list[str] = []
    for batch_start in range(1, COUNT + 1, BATCH_SIZE):
        batch_end = min(batch_start + BATCH_SIZE - 1, COUNT)
        batch_ids = await asyncio.gather(*(create_one(sdk, n) for n in range(batch_start, batch_end + 1)))
        ids.extend(batch_ids)
        print(f"  batch {batch_start}-{batch_end} done ({len(batch_ids)} conversations)")
    return ids


async def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    passed = True
    with new_client() as sdk:
        print("Cleaning old conv-titled conversations...")
        cleanup_conv_titled(sdk)

        print(f"Creating {COUNT} conversations in batches of {BATCH_SIZE}...")
        ids = await create_conversations(sdk)
        await wait_for_search_count(sdk, COUNT, search="conv ")

        print("\n--- pagination (sort createdAt asc) ---")
        res = list_convs(sdk, page=3, limit=5, sort_by="createdAt", sort_order="asc", search="conv ")
        p = res.pagination
        page3 = titles(res)
        passed &= ok("page 3 has 5 conversations", len(page3) == 5)
        passed &= ok("total_count == 20", p.total_count == COUNT, str(p.total_count))
        passed &= ok("total_pages == 4", p.total_pages == 4, str(p.total_pages))

        res = list_convs(sdk, page=4, limit=5, sort_by="createdAt", sort_order="asc", search="conv ")
        page4 = titles(res)
        batch2 = {title(i) for i in range(11, 21)}
        passed &= ok(
            "pages 3-4 are batch 2 (conv 11-20)",
            set(page3) | set(page4) == batch2,
            f"page3={page3} page4={page4}",
        )

        print("\n--- sorting ---")
        res = list_convs(sdk, limit=BATCH_SIZE, sort_by="createdAt", sort_order="asc", search="conv ")
        passed &= ok(
            "createdAt asc first page is batch 1",
            all(conv_batch(t) == 1 for t in titles(res)),
            str(titles(res)),
        )
        res = list_convs(sdk, limit=BATCH_SIZE, sort_by="createdAt", sort_order="desc", search="conv ")
        passed &= ok(
            "createdAt desc first page is batch 2",
            all(conv_batch(t) == 2 for t in titles(res)),
            str(titles(res)),
        )

        print("\n--- search ---")
        passed &= ok("search conv 5 -> 1 hit", len(list_convs(sdk, limit=100, search="conv 5").conversations) == 1)
        passed &= ok(
            "search conv  -> 20 hits",
            list_convs(sdk, limit=100, search="conv ").pagination.total_count == COUNT,
        )

        print("\n--- archive ---")
        to_archive = ids[-5:]
        for cid in to_archive:
            archive_conversation(sdk, cid)
        active = list_convs_archived(sdk, False, limit=100, search="conv ")
        passed &= ok(
            "is_archived=false total_count == 15",
            active.pagination.total_count == 15,
            str(active.pagination.total_count),
        )
        archived_query = list_convs_archived(sdk, True, limit=100, search="conv ")
        passed &= ok(
            "is_archived=true main list still excludes archived",
            archived_query.pagination.total_count == 15,
            str(archived_query.pagination.total_count),
        )
        archived_titles = {c.title or "" for c in list_archived(sdk) if c.id in to_archive}
        passed &= ok(
            "archived conv 16-20 visible in archives",
            archived_titles == {title(i) for i in range(16, 21)},
            str(sorted(archived_titles)),
        )

        print("\n--- cleanup ---")
        for cid in ids:
            safe_delete(sdk, cid)
        passed &= ok("active batch removed", list_convs(sdk, limit=100, search="conv ").pagination.total_count == 0)
        passed &= ok("archived batch removed", not any(c.id in ids for c in list_archived(sdk)))

    if not passed:
        sys.exit("Some checks failed.")
    print("\nAll checks passed.")


if __name__ == "__main__":
    asyncio.run(main())
