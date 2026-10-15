"""Create a conversation and wait for the complete answer (non-streaming)."""

import asyncio
import os
from pathlib import Path

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
        created = await client.conversations.create_conversation_async(
            query="Who moved the cheese?",
            chat_mode="internal_search",
        )
        conversation = created.result.conversation
        assert conversation.id is not None
        try:
            print(f"conversation id: {conversation.id}")
            print(f"status: {conversation.status}")
            answer = next(
                message for message in reversed(conversation.messages or [])
                if message.message_type == "bot_response"
            )
            print(answer.content)
        finally:
            await client.conversations.delete_conversation_by_id_async(
                conversation_id=conversation.id,
            )


if __name__ == "__main__":
    asyncio.run(main())
