import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import default_filters, print_conversation, stream_create

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    with client() as pipeshub_client:
        conv_id, _, _, _ = stream_create(
            pipeshub_client, FIRST_MESSAGE, default_filters(), print_bot=False
        )
        print(f"created conversation id: {conv_id}")
        print(f"\n--- conversation by id: {conv_id} ---")
        print_conversation(pipeshub_client, conv_id, verbose=True)


if __name__ == "__main__":
    main()
