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
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.stream_agent_conversation(
            agent_key=key,
            query=FIRST_MESSAGE,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            conv_id, _, original, bot_response_message_id = stream_bot_reply(stream)

        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nOriginal bot response ({len(original)} chars):\n{original}")
        assert bot_response_message_id is not None

        print(f"\nRegenerating message {bot_response_message_id} ...\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.regenerate_agent_conversation_message(
            agent_key=key,
            conversation_id=conv_id,
            message_id=bot_response_message_id,
            filters=filters,
        ) as stream:
            _, _, regenerated, _ = stream_bot_reply(stream)

        print(f"\nRegenerated bot response ({len(regenerated)} chars):\n{regenerated}")


if __name__ == "__main__":
    main()
