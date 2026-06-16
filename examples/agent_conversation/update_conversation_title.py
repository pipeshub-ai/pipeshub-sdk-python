import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

from helpers import stream_bot_reply

AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
FILTERS: FiltersTypedDict = {"apps": ["270d4bac-234a-4c0d-963f-84f152cd21f0"]}

FIRST_MESSAGE = "Who moved the cheese?"
NEW_TITLE = "SDK example: updated title"


def main() -> None:
    load_dotenv()

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        conv_id, old_title, _, _ = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            )
        )

        print(f"conversation id: {conv_id}")
        res = pipeshub_client.agents.update_agent_conversation_title(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
            title=NEW_TITLE,
        )
        print(f"old title: {old_title!r}")
        print(f"new title: {res.conversation.title!r}")


if __name__ == "__main__":
    main()
