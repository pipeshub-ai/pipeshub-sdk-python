import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import agent_key, default_filters, stream_create

FIRST_MESSAGE = "Who moved the cheese?"
SECOND_MESSAGE = "Can you give me more details on that?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()
    created: list[tuple[str, str]] = []

    with new_client() as sdk:
        for i, query in enumerate([FIRST_MESSAGE, SECOND_MESSAGE], 1):
            print(f"Creating conversation {i} (waiting for response...)...")
            conv_id, title, _, _ = stream_create(sdk, query, filters, print_bot=False)
            if not title:
                title = query
            sdk.agents.archive_agent_conversation(agent_key=key, conversation_id=conv_id)
            created.append((conv_id, title))

        print("\nCreated and archived:")
        for i, (cid, title) in enumerate(created, 1):
            print(f"  {i}. {cid} — {title!r}")

        res = sdk.agents.list_agent_archived_conversations_grouped(agent_page=1, agent_limit=20)
        group = next((g for g in res.groups if g.agent_key == key), None)

        print("\nArchived conversations for this agent (grouped list):")
        if not group:
            print("  (no group found for this agentKey)")
            return

        created_ids = {cid: title for cid, title in created}
        matched = 0
        for conv in group.conversations:
            if conv.id in created_ids:
                matched += 1
                print(f"  - {conv.title!r} ({conv.id})")

        if matched == 0:
            print("  (none of the conversations we created appear in this page of results)")
        elif matched == len(created):
            print(f"\nBoth conversations created in this run appear under agent {key}.")
        else:
            print(f"\n{matched} of {len(created)} conversations created in this run appear under agent {key}.")


if __name__ == "__main__":
    main()
