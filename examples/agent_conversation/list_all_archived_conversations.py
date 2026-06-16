import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_bot_reply

QUERIES = [
    "What is 2+2?",
    "Name three primary colors.",
    "What day comes after Monday?",
]


def print_archived(convs) -> int:
    if not convs:
        print("  (no archived conversations for this agent)")
        return 0
    for conv in convs:
        title = conv.title or "(untitled)"
        archived = conv.archived_at.strftime("%Y-%m-%d %H:%M:%S %Z") if conv.archived_at else "-"
        print(f"  - {title!r} - {conv.id} - archived {archived}")
    return len(convs)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()
    created: list[tuple[str, str]] = []

    with client() as pipeshub_client:
        print(f"Using agent {key}\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Creating conversation {i}/{len(QUERIES)}...")
            with pipeshub_client.agents.stream_agent_conversation(
                agent_key=key,
                query=query,
                filters=filters,
                chat_mode="auto",
            ) as stream:
                conv_id, title, _, _ = stream_bot_reply(stream, print_output=False)
            title = title or query

            pipeshub_client.agents.archive_agent_conversation(
                agent_key=key,
                conversation_id=conv_id,
            )
            created.append((conv_id, title))
            print(f"  archived {conv_id} - {title!r}")

        print("\nArchived conversations for this agent (newest first):")
        archived = []
        page = 1
        while True:
            res = pipeshub_client.agents.list_agent_conversation_archives(
                agent_key=key,
                page=page,
                limit=20,
                sort_by="lastActivityAt",
                sort_order="desc",
            )
            archived.extend(res.conversations)
            p = res.pagination
            if not p.has_next_page or page >= p.total_pages:
                break
            page += 1

        ours = {cid for cid, _ in created}
        matched = [c for c in archived if c.id in ours]
        count = print_archived(matched)
        print(f"\nFound {count} of {len(created)} conversation(s) we just archived.")

        print("\nDeleting archived conversations:")
        for conv_id, title in created:
            pipeshub_client.agents.delete_agent_conversation_by_id(
                agent_key=key,
                conversation_id=conv_id,
            )
            print(f"  deleted {conv_id} - {title!r}")

        print("\nArchived conversations after cleanup:")
        remaining: list[Any] = []
        page = 1
        while True:
            res = pipeshub_client.agents.list_agent_conversation_archives(
                agent_key=key,
                page=page,
                limit=20,
                sort_by="lastActivityAt",
                sort_order="desc",
            )
            remaining.extend(c for c in res.conversations if c.id in ours)
            p = res.pagination
            if not p.has_next_page or page >= p.total_pages:
                break
            page += 1
        print_archived(remaining)


if __name__ == "__main__":
    main()
