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
    stream_create,
)

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
        archived = conv.archived_at.strftime("%Y-%m-%d %H:%M:%S %Z") if conv.archived_at else "—"
        print(f"  - {title!r} — {conv.id} — archived {archived}")
    return len(convs)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()
    created: list[tuple[str, str]] = []

    with new_client() as sdk:
        print(f"Using agent {key}\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Creating conversation {i}/{len(QUERIES)}...")
            conv_id, title, _, _ = stream_create(sdk, query, filters, print_bot=False)
            if not title:
                title = query
            archive_conversation(sdk, conv_id, key=key)
            created.append((conv_id, title))
            print(f"  archived {conv_id} — {title!r}")

        print("\nArchived conversations for this agent (newest first):")
        archived = list_archived(sdk, key=key)
        ours = {cid for cid, _ in created}
        matched = [c for c in archived if c.id in ours]
        count = print_archived(matched)
        print(f"\nFound {count} of {len(created)} conversation(s) we just archived.")

        print("\nDeleting archived conversations:")
        for conv_id, title in created:
            delete_conversation(sdk, conv_id, key=key)
            print(f"  deleted {conv_id} — {title!r}")

        print("\nArchived conversations after cleanup:")
        remaining = [c for c in list_archived(sdk, key=key) if c.id in ours]
        print_archived(remaining)


if __name__ == "__main__":
    main()
