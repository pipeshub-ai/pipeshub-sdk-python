"""Unarchive a semantic search."""

import asyncio
import os
from pathlib import Path

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
        search = await client.semantic_search.search_async(query="quarterly revenue", limit=10)
        await client.semantic_search.archive_search_async(search_id=search.search_id)
        unarchived = await client.semantic_search.unarchive_search_async(search_id=search.search_id)
        print(unarchived)


if __name__ == "__main__":
    asyncio.run(main())
