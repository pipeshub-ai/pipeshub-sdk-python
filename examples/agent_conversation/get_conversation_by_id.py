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
            conv_id, _, _, _ = stream_bot_reply(stream, print_output=False)

        print(f"created conversation id: {conv_id}")
        print(f"\n--- conversation by id: {conv_id} ---")

        res = pipeshub_client.agents.get_agent_conversation_by_id(
            agent_key=key,
            conversation_id=conv_id,
        )
        conv = res.conversation
        print(f"  id: {conv.id}")
        if conv.title:
            print(f"  title: {conv.title!r}")
        print(f"  messages: {len(conv.messages or [])}")
        for i, msg in enumerate(conv.messages or [], 1):
            print(f"\n--- message {i} [{msg.message_type or ''}] ---\n{msg.content or ''}")


if __name__ == "__main__":
    main()
