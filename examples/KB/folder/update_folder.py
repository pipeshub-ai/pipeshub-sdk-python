"""Rename a folder in a knowledge base."""

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

        updated_folder = await pipeshub_client.knowledge_base.update_folder_async(
            kb_id=kb.id,
            folder_id=folder.id,
            folder_name="Reports (updated)",
        )
        print("Updated folder:", updated_folder)


if __name__ == "__main__":
    asyncio.run(main())
