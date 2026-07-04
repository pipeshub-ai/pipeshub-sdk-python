"""List agents.

Lists the agents visible to the caller, with paging and sorting.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

base_url = os.environ["PIPESHUB_BASE_URL"]
token = os.environ["PIPESHUB_BEARER_AUTH"]

server_url = f'{base_url.rstrip("/")}/api/v1'


async def main() -> None:
    async with SDK(
        server_url=server_url,
        security=models.Security(bearer_auth=token),
    ) as pipeshub_client:

        agents = await pipeshub_client.agents.list_agents_async(
            page=1,
            limit=20,
            sort_by="updatedAtTimestamp",
            sort_order="desc",
        )
        print(agents.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
