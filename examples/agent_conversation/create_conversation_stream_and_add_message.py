import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_bot_reply

FIRST_MESSAGE = "Who moved the cheese?"
FOLLOW_UP = "Can you give me more details on that?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()

    with client() as pipeshub_client:
        print(f"agent key: {key}")
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.stream_agent_conversation(
            agent_key=key,
            query=FIRST_MESSAGE,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            conv_id, _, _, _ = stream_bot_reply(stream)

        print(f"conversation id: {conv_id}")
        print(f"\nYou: {FOLLOW_UP}\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.stream_agent_conversation_message(
            agent_key=key,
            conversation_id=conv_id,
            query=FOLLOW_UP,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            stream_bot_reply(stream)


if __name__ == "__main__":
    main()
