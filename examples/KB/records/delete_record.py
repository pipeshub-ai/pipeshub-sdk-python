"""Delete a record permanently."""

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

        with open(upload_path, "rb") as f:
            content = f.read()

        upload_stream = await pipeshub_client.knowledge_base.upload_records_async(
            kb_id=kb.id,
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

        deleted = await pipeshub_client.knowledge_base.delete_record_async(
            record_id=record_id,
        )
        print("Delete result:", deleted)


if __name__ == "__main__":
    asyncio.run(main())
