"""Move a record from a source folder into a destination folder.

Creates a knowledge base and a source folder, uploads a PDF into it, captures the
new record's ID from the upload stream, creates a destination folder, and moves
the record there.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

base_url = os.environ.get("PIPESHUB_BASE_URL")
token = os.environ.get("PIPESHUB_BEARER_AUTH")
upload_path = os.environ.get("PIPESHUB_UPLOAD_PATH")

if not base_url:
    raise RuntimeError("Missing PIPESHUB_BASE_URL environment variable")
if not token:
    raise RuntimeError("Missing PIPESHUB_BEARER_AUTH environment variable")


async def main() -> None:
    if not upload_path:
        raise RuntimeError("Missing PIPESHUB_UPLOAD_PATH environment variable")

    async with SDK(
        server_url=f'{base_url.rstrip("/")}/api/v1' if base_url else None,
        security=models.Security(bearer_auth=token),
    ) as pipeshub_client:

        kb = await pipeshub_client.knowledge_base.create_knowledge_base_async(
            kb_name="Internal documents",
        )

        # Create the source folder
        source_folder = await pipeshub_client.knowledge_base.create_folder_async(
            kb_id=kb.id,
            folder_name="Source",
        )

        # Upload a PDF into the source folder
        with open(upload_path, "rb") as f:
            content = f.read()

        upload_stream = await pipeshub_client.knowledge_base.upload_records_async(
            kb_id=kb.id,
            folder_id=source_folder.id,
            files=[
                {
                    "file_name": Path(upload_path).name,
                    "content": content,
                },
            ],
        )

        # Grab the new record's ID from the `file:succeeded` event payload.
        record_id = None
        async for event in upload_stream:
            if event.event == "file:succeeded" and event.data:
                payload = event.data
                record_id = (
                    payload.get("recordId")
                    or payload.get("id")
                    or (payload.get("record") or {}).get("id")
                )
        if not record_id:
            raise RuntimeError(
                "Could not determine the uploaded record ID from the upload stream"
            )

        # Create the destination folder
        dest_folder = await pipeshub_client.knowledge_base.create_folder_async(
            kb_id=kb.id,
            folder_name="Destination",
        )

        # Move the uploaded record from the source folder into the destination folder
        moved = await pipeshub_client.knowledge_base.move_record_async(
            kb_id=kb.id,
            record_id=record_id,
            new_parent_id=dest_folder.id,
        )
        print("Move result:", moved)


if __name__ == "__main__":
    asyncio.run(main())
