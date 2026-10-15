"""Search archived conversations by title."""

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
        conv_id = created.result.conversation.id
        assert conv_id is not None
        try:
            await client.conversations.archive_conversation_async(
                conversation_id=conv_id,
            )

            results = await client.conversations.search_archived_conversations_async(
                search="cheese",
            )
            for conversation in results.conversations or []:
                print(f"{conversation.id}  {conversation.title}")
            print(results.pagination)
        finally:
            await client.conversations.delete_conversation_by_id_async(
                conversation_id=conv_id,
            )


if __name__ == "__main__":
    asyncio.run(main())
