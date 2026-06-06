import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import load_env, new_client
from helpers import default_filters, print_conversation, stream_create

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    with new_client() as sdk:
        conv_id, _, _, _ = stream_create(sdk, FIRST_MESSAGE, default_filters(), print_bot=False)
        print(f"created conversation id: {conv_id}")
        print(f"\n--- conversation by id: {conv_id} ---")
        print_conversation(sdk, conv_id, verbose=True)


if __name__ == "__main__":
    main()
