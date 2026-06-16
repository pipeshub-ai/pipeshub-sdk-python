import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_bot_reply
from pipeshub_sdk.models import MessageFeedbackSubmitRequestCategory

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
    if len(sys.argv) < 2:
        sys.exit(f"usage: uv run python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])

    key = agent_key()
    filters = default_filters()

    with client() as pipeshub_client:
        print(f"You: {FIRST_MESSAGE}\n\nBot: ", end="", flush=True)
        with pipeshub_client.agents.stream_agent_conversation(
            agent_key=key,
            query=FIRST_MESSAGE,
            filters=filters,
            chat_mode="auto",
        ) as stream:
            conv_id, _, answer, bot_response_message_id = stream_bot_reply(stream)

        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nBot response ({len(answer)} chars):\n{answer}")
        assert bot_response_message_id is not None

        res = pipeshub_client.agents.update_agent_conversation_message_feedback(
            agent_key=key,
            conversation_id=conv_id,
            message_id=bot_response_message_id,
            is_helpful=True,
            categories=POSITIVE_CATEGORIES,
            comments={"positive": POSITIVE_COMMENT},
        )
        print(f"feedback submitted: {res.conversation_id}")


if __name__ == "__main__":
    main()
