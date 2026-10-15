"""Cancel a streaming chat after its first chunk of answer text.

The run is cancelled with the client-generated `run_id` that was sent when the
stream started. The stream then ends with a RUN_FINISHED event whose
conversation status is `Stopped`.
"""

import asyncio
import os
import uuid
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
# OAuth2 client credentials. The SDK fetches the access token itself.
security = models.Security(oauth2=models.SchemeOauth2(
    client_id=os.environ["PIPESHUB_CLIENT_ID"],
    client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
    token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
))


async def main() -> None:
    async with SDK(
        server_url=server_url,
        security=security,
        timeout_ms=300_000,
    ) as client:
        run_id = str(uuid.uuid4())
        conv_id = None
        chat_stream = await client.conversations.stream_chat_async(
            query="Write a 300 word story about a mouse who loves cheese.",
            chat_mode="internal_search",
            run_id=run_id,
        )
        try:
            cancelled = False
            async for event in chat_stream:
                data: Any = event.data
                if event.event == "RUN_ERROR":
                    raise RuntimeError(f"stream error: {data}")
                if event.event == "RUN_STARTED" and data:
                    # threadId is the new conversation's id.
                    conv_id = data["threadId"]
                elif event.event == "TEXT_MESSAGE_CONTENT" and conv_id and not cancelled:
                    print(f"first chunk: {data['delta']!r}")
                    result = await client.conversations.cancel_conversation_stream_async(
                        conversation_id=conv_id,
                        run_id=run_id,
                    )
                    print(f"cancel result: {result}")
                    cancelled = True
                elif event.event == "RUN_FINISHED" and data:
                    status = data["result"]["conversation"]["status"]
                    print(f"final conversation status: {status}")
        finally:
            if conv_id:
                await client.conversations.delete_conversation_by_id_async(
                    conversation_id=conv_id,
                )


if __name__ == "__main__":
    asyncio.run(main())
