import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import agent_key, format_activity

PAGE_LIMIT = 20


def print_section(heading: str, convs) -> None:
    print(f"\n{heading}:")
    if not convs:
        print("  (none)")
        return
    for conv in convs:
        title = conv.title or "(untitled)"
        print(f"  - {title!r} — {conv.id} — {format_activity(conv)}")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    with new_client() as sdk:
        print(f"Active conversations for agent {key} (newest first):")
        page = 1
        owned = []
        shared = []
        owned_total = 0

        while True:
            res = sdk.agents.list_agent_conversations(
                agent_key=key,
                page=page,
                limit=PAGE_LIMIT,
                sort_by="lastActivityAt",
                sort_order="desc",
            )
            if page == 1:
                owned_total = res.pagination.total_count
            owned.extend(res.conversations)
            shared.extend(res.shared_with_me_conversations)
            p = res.pagination
            if not p.has_next_page or page >= p.total_pages:
                break
            page += 1

        print_section("Your conversations", owned)
        print_section("Shared with you", shared)

        if not owned and not shared:
            print("\n(no active conversations for this agent)")
            return
        print(f"\nListed {len(owned)} owned and {len(shared)} shared conversation(s) (owned total reported: {owned_total}).")


if __name__ == "__main__":
    main()
