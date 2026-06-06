import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import agent_key, default_filters, stream_add_message, stream_create

FIRST_MESSAGE = "Who moved the cheese?"
FOLLOW_UP = "Can you give me more details on that?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    with new_client() as sdk:
        key = agent_key()
        print(f"agent key: {key}")
        filters = default_filters()
        conv_id, _, _, _ = stream_create(sdk, FIRST_MESSAGE, filters, key=key)
        print(f"conversation id: {conv_id}")
        stream_add_message(sdk, conv_id, FOLLOW_UP, filters, key=key)


if __name__ == "__main__":
    main()
