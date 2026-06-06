import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import default_filters, stream_create, stream_regenerate

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    filters = default_filters()
    with client() as pipeshub_client:
        conv_id, _, original, bot_response_message_id = stream_create(
            pipeshub_client, FIRST_MESSAGE, filters
        )
        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nOriginal bot response ({len(original)} chars):\n{original}")

        if not bot_response_message_id:
            raise RuntimeError("missing bot response message id")

        regenerated = stream_regenerate(
            pipeshub_client, conv_id, bot_response_message_id, filters
        )
        print(f"\nRegenerated bot response ({len(regenerated)} chars):\n{regenerated}")


if __name__ == "__main__":
    main()
