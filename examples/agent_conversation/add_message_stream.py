import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

FIRST_MESSAGE = "Who moved the cheese?"
FOLLOW_UP = "Can you give me more details on that?"


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
        for event in stream:
            if event.event == "RUN_ERROR":
                raise RuntimeError(f"stream error: {event.data}")
            if event.event == "RUN_FINISHED" and event.data:
                conv_id = event.data["result"]["conversation"]["_id"]
                break
        if conv_id is None:
            raise RuntimeError("stream ended without a RUN_FINISHED event")
        print(f"conversation id: {conv_id}")

        # Send a follow-up message on the same conversation; consume the stream.
        follow_up = pipeshub_client.agents.stream_agent_conversation_message(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
            query=FOLLOW_UP,
            filters=FILTERS,
            chat_mode="quick",
        )
        completed = False
        for event in follow_up:
            if event.event == "RUN_ERROR":
                raise RuntimeError(f"stream error: {event.data}")
            if event.event == "RUN_FINISHED" and event.data:
                completed = True
                break
        if not completed:
            raise RuntimeError("stream ended without a RUN_FINISHED event")
        print(f"follow-up message sent to conversation: {conv_id}")


if __name__ == "__main__":
    main()
