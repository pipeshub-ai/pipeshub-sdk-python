import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

from helpers import stream_bot_reply

AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
FILTERS: FiltersTypedDict = {"apps": ["270d4bac-234a-4c0d-963f-84f152cd21f0"]}

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    load_dotenv()

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        conv_id, title, _, _ = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            ),
            print_output=False,
        )
        title = title or FIRST_MESSAGE
        print(f"Created conversation: {conv_id}")
        print(f"Title: {title!r}")

        archived = pipeshub_client.agents.archive_agent_conversation(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
        )
        if archived.archived_at:
            print(f"Archived (by you at {archived.archived_at}): conversation is now in archives")
        else:
            print("Archived (by you): conversation is now in archives")

        unarchived = pipeshub_client.agents.unarchive_agent_conversation(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
        )
        if unarchived.unarchived_at:
            print(f"Unarchived (at {unarchived.unarchived_at}): conversation is back in your active list")
        else:
            print("Unarchived: conversation is back in your active list")


if __name__ == "__main__":
    main()
