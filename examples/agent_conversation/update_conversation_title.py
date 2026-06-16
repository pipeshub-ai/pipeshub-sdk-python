import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_bot_reply

FIRST_MESSAGE = "Who moved the cheese?"
NEW_TITLE = "SDK example: updated title"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()

    with client() as pipeshub_client:
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.stream_agent_conversation(
            agent_key=key,
            query=FIRST_MESSAGE,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            conv_id, old_title, _, _ = stream_bot_reply(stream)

        print(f"conversation id: {conv_id}")
        res = pipeshub_client.agents.update_agent_conversation_title(
            agent_key=key,
            conversation_id=conv_id,
            title=NEW_TITLE,
        )
        print(f"old title: {old_title!r}")
        print(f"new title: {res.conversation.title!r}")


if __name__ == "__main__":
    main()
