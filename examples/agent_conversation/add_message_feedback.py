import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import client, load_env
from helpers import agent_key, default_filters, stream_create
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

    with client() as pipeshub_client:
        conv_id, _, answer, bot_response_message_id = stream_create(
            pipeshub_client, FIRST_MESSAGE, default_filters()
        )
        print(f"conversation id: {conv_id}")
        print(f"bot response message id: {bot_response_message_id}")
        print(f"\nBot response ({len(answer)} chars):\n{answer}")

        if not bot_response_message_id:
            raise RuntimeError("missing bot response message id")

        res = pipeshub_client.agents.update_agent_conversation_message_feedback(
            agent_key=agent_key(),
            conversation_id=conv_id,
            message_id=bot_response_message_id,
            is_helpful=True,
            categories=POSITIVE_CATEGORIES,
            comments={"positive": POSITIVE_COMMENT},
        )
        print(f"feedback submitted: {res.conversation_id}")


if __name__ == "__main__":
    main()
