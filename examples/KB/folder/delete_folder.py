"""Delete a folder (cascade deletes all subfolders and records within)."""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

base_url = os.environ.get("PIPESHUB_BASE_URL")
token = os.environ.get("PIPESHUB_BEARER_AUTH")

if not base_url:
    raise RuntimeError("Missing PIPESHUB_BASE_URL environment variable")
if not token:
    raise RuntimeError("Missing PIPESHUB_BEARER_AUTH environment variable")


async def main() -> None:
    async with SDK(
        server_url=f'{base_url.rstrip("/")}/api/v1' if base_url else None,
        security=models.Security(bearer_auth=token),
    ) as pipeshub_client:

        kb = await pipeshub_client.knowledge_base.create_knowledge_base_async(
            kb_name="Internal documents",
        )

        folder = await pipeshub_client.knowledge_base.create_folder_async(
            kb_id=kb.id,
            folder_name="Reports",
        )

        delete_result = await pipeshub_client.knowledge_base.delete_folder_async(
            kb_id=kb.id,
            folder_id=folder.id,
        )
        print("Delete result:", delete_result)


if __name__ == "__main__":
    asyncio.run(main())
