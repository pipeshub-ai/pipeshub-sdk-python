"""Submit feedback on a conversation message."""

import asyncio
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
token = os.environ["PIPESHUB_BEARER_AUTH"]


async def main() -> None:
    async with SDK(
        server_url=server_url,
        security=models.Security(bearer_auth=token),
    ) as client:
        conv_id = msg_id = None
        new_conversation_stream = await client.conversations.stream_chat_async(
            query="Who moved the cheese?",
        )
        async for event in new_conversation_stream:
            data: Any = event.data
            if event.event == "complete" and data:
                conversation = data["conversation"]
                conv_id = conversation["_id"]
                msg_id = next(
                    message for message in reversed(conversation["messages"])
                    if message.get("messageType") == "bot_response"
                ).get("_id")
        assert conv_id is not None and msg_id is not None

        feedback = await client.conversations.update_message_feedback_async(
            conversation_id=conv_id,
            message_id=msg_id,
            is_helpful=True,
        )
        print(feedback)


if __name__ == "__main__":
    asyncio.run(main())
