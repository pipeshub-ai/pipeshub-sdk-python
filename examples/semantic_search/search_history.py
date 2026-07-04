"""List semantic search history."""

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
        history = await client.semantic_search.search_history_async(limit=20)
        print(history.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
