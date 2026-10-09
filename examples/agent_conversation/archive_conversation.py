import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    load_dotenv()
    AGENT_KEY = os.environ["AGENT_KEY"]
    FILTERS: FiltersTypedDict = {"apps": [os.environ["CONNECTOR_APP_KEY"]]}

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
        timeout_ms=300_000,
    ) as pipeshub_client:
        stream = pipeshub_client.agents.stream_agent_conversation(
            agent_key=AGENT_KEY,
            query=FIRST_MESSAGE,
            filters=FILTERS,
            chat_mode="quick",
        )
        conv_id = None
        title = ""
        for event in stream:
            if event.event == "RUN_ERROR":
                raise RuntimeError(f"stream error: {event.data}")
            if event.event == "RUN_FINISHED" and event.data:
                conversation = event.data["result"]["conversation"]
                conv_id = conversation["_id"]
                title = conversation.get("title") or ""
                break
        if conv_id is None:
            raise RuntimeError("stream ended without a RUN_FINISHED event")
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


if __name__ == "__main__":
    main()
