import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import default_filters, stream_create, update_title

FIRST_MESSAGE = "Who moved the cheese?"
NEW_TITLE = "SDK example: updated title"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    with client() as pipeshub_client:
        conv_id, old_title, _, _ = stream_create(
            pipeshub_client, FIRST_MESSAGE, default_filters()
        )
        print(f"conversation id: {conv_id}")
        updated = update_title(pipeshub_client, conv_id, NEW_TITLE)
        print(f"old title: {old_title!r}")
        print(f"new title: {updated!r}")


if __name__ == "__main__":
    main()
