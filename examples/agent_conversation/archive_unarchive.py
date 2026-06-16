import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_bot_reply

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()

    with client() as pipeshub_client:
        with pipeshub_client.agents.stream_agent_conversation(
            agent_key=key,
            query=FIRST_MESSAGE,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            conv_id, title, _, _ = stream_bot_reply(stream, print_output=False)
        title = title or FIRST_MESSAGE
        print(f"Created conversation: {conv_id}")
        print(f"Title: {title!r}")

        archived = pipeshub_client.agents.archive_agent_conversation(
            agent_key=key,
            conversation_id=conv_id,
        )
        if archived.archived_at:
            print(f"Archived (by you at {archived.archived_at}): conversation is now in archives")
        else:
            print("Archived (by you): conversation is now in archives")

        unarchived = pipeshub_client.agents.unarchive_agent_conversation(
            agent_key=key,
            conversation_id=conv_id,
        )
        if unarchived.unarchived_at:
            print(f"Unarchived (at {unarchived.unarchived_at}): conversation is back in your active list")
        else:
            print("Unarchived: conversation is back in your active list")


if __name__ == "__main__":
    main()
