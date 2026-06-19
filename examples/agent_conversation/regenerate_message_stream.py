import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

from helpers import stream_bot_reply

FIRST_MESSAGE = "Who moved the cheese?"


def main() -> None:
    load_dotenv()
    AGENT_KEY = os.environ["AGENT_KEY"]
    FILTERS: FiltersTypedDict = {"apps": [os.environ["CONNECTOR_APP_KEY"]]}

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        conv_id, _, original, bot_response_message_id = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            )
        )

        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nOriginal bot response ({len(original)} chars):\n{original}")
        assert bot_response_message_id is not None

        print(f"\nRegenerating message {bot_response_message_id} ...\n\nBot: ", end="", flush=True)
        _, _, regenerated, _ = stream_bot_reply(
            pipeshub_client.agents.regenerate_agent_conversation_message(
                agent_key=AGENT_KEY,
                conversation_id=conv_id,
                message_id=bot_response_message_id,
                filters=FILTERS,
            )
        )

        print(f"\nRegenerated bot response ({len(regenerated)} chars):\n{regenerated}")


if __name__ == "__main__":
    main()
