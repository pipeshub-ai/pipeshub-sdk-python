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
        bot_response_message_id = None
        for event in stream:
            if event.event == "RUN_ERROR":
                raise RuntimeError(f"stream error: {event.data}")
            if event.event == "RUN_FINISHED" and event.data:
                conversation = event.data["result"]["conversation"]
                conv_id = conversation["_id"]
                bot = next(
                    m for m in reversed(conversation["messages"])
                    if m.get("messageType") == "bot_response"
                )
                bot_response_message_id = bot.get("_id")
                break
        if conv_id is None:
            raise RuntimeError("stream ended without a RUN_FINISHED event")

        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        assert bot_response_message_id is not None

        print(f"Regenerating message {bot_response_message_id} ...")
        regenerate = pipeshub_client.agents.regenerate_agent_conversation_message(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
            message_id=bot_response_message_id,
            filters=FILTERS,
            chat_mode="quick",
        )
        completed = False
        for event in regenerate:
            if event.event == "RUN_ERROR":
                raise RuntimeError(f"stream error: {event.data}")
            if event.event == "RUN_FINISHED" and event.data:
                completed = True
                break
        if not completed:
            raise RuntimeError("stream ended without a RUN_FINISHED event")

        print(f"regenerated message {bot_response_message_id}")


if __name__ == "__main__":
    main()
