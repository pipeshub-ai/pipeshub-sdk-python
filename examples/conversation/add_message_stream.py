"""Add a follow-up message to a conversation with a streaming response."""

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
        timeout_ms=300_000,
    ) as client:
        conv_id = None
        new_conversation_stream = await client.conversations.stream_chat_async(
            query="Who moved the cheese?",
            chat_mode="agent",
        )
        async for event in new_conversation_stream:
            data: Any = event.data
            if event.event == "RUN_FINISHED" and data:
                conv_id = data["result"]["conversation"]["_id"]
        assert conv_id is not None

        reply_stream = await client.conversations.add_message_stream_async(
            conversation_id=conv_id,
            query="Can you give me more details on that?",
            chat_mode="agent",
        )
        async for event in reply_stream:
            data = event.data
            if event.event == "TEXT_MESSAGE_CONTENT" and data:
                print(data["delta"], end="", flush=True)
        print()


if __name__ == "__main__":
    asyncio.run(main())
