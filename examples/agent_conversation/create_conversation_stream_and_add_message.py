import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

from helpers import stream_bot_reply

FIRST_MESSAGE = "Who moved the cheese?"
FOLLOW_UP = "Can you give me more details on that?"


def main() -> None:
    load_dotenv()
    AGENT_KEY = os.environ["AGENT_KEY"]
    FILTERS: FiltersTypedDict = {"apps": [os.environ["CONNECTOR_APP_KEY"]]}

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        print(f"agent key: {AGENT_KEY}")
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        conv_id, _, _, _ = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            )
        )

        print(f"conversation id: {conv_id}")
        print(f"\nYou: {FOLLOW_UP}\n\nBot: ", end="", flush=True)
        stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation_message(
                agent_key=AGENT_KEY,
                conversation_id=conv_id,
                query=FOLLOW_UP,
                filters=FILTERS,
                chat_mode="auto",
            )
        )


if __name__ == "__main__":
    main()
