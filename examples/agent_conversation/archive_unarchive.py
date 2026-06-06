import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import agent_key, default_filters, stream_create

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    with new_client() as sdk:
        conv_id, title, _, _ = stream_create(sdk, FIRST_MESSAGE, default_filters(), print_bot=False)
        if not title:
            title = FIRST_MESSAGE
        print(f"Created conversation: {conv_id}")
        print(f"Title: {title!r}")

        archived = sdk.agents.archive_agent_conversation(agent_key=key, conversation_id=conv_id)
        at = archived.archived_at
        if at:
            print(f"Archived (by you at {at}): conversation is now in archives")
        else:
            print("Archived (by you): conversation is now in archives")

        unarchived = sdk.agents.unarchive_agent_conversation(agent_key=key, conversation_id=conv_id)
        uat = unarchived.unarchived_at
        if uat:
            print(f"Unarchived (at {uat}): conversation is back in your active list")
        else:
            print("Unarchived: conversation is back in your active list")


if __name__ == "__main__":
    main()
