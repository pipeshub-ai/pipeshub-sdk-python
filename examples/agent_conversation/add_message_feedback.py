import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict, MessageFeedbackSubmitRequestCategory

from helpers import stream_bot_reply

AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
FILTERS: FiltersTypedDict = {"apps": ["270d4bac-234a-4c0d-963f-84f152cd21f0"]}

FIRST_MESSAGE = "Who moved the cheese?"
POSITIVE_CATEGORIES: list[MessageFeedbackSubmitRequestCategory] = [
    "excellent_answer",
    "helpful_citations",
    "well_explained",
]
POSITIVE_COMMENT = (
    "The answer stayed on topic and covered the main points without filler. "
    "Citations pointed to relevant sources I could verify."
)


def main() -> None:
    load_dotenv()

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        conv_id, _, answer, bot_response_message_id = stream_bot_reply(
            pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=FIRST_MESSAGE,
                filters=FILTERS,
                chat_mode="auto",
            )
        )

        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nBot response ({len(answer)} chars):\n{answer}")
        assert bot_response_message_id is not None

        res = pipeshub_client.agents.update_agent_conversation_message_feedback(
            agent_key=AGENT_KEY,
            conversation_id=conv_id,
            message_id=bot_response_message_id,
            is_helpful=True,
            categories=POSITIVE_CATEGORIES,
            comments={"positive": POSITIVE_COMMENT},
        )
        print(f"feedback submitted: {res.conversation_id}")


if __name__ == "__main__":
    main()
