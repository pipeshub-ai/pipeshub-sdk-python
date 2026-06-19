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
        conv_id, _, _, _ = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            ),
            print_output=False,
        )

        print(f"created conversation id: {conv_id}")
        print(f"\n--- conversation by id: {conv_id} ---")

        res = pipeshub_client.agents.get_agent_conversation_by_id(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
        )
        conv = res.conversation
        print(f"  id: {conv.id}")
        if conv.title:
            print(f"  title: {conv.title!r}")
        print(f"  messages: {len(conv.messages or [])}")
        for i, msg in enumerate(conv.messages or [], 1):
            print(f"\n--- message {i} [{msg.message_type or ''}] ---\n{msg.content or ''}")


if __name__ == "__main__":
    main()
