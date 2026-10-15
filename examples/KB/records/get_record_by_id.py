"""Get a record by ID.

Creates a knowledge base, uploads PIPESHUB_UPLOAD_PATH into it, fetches the new
record, then deletes the knowledge base.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
# OAuth2 client credentials. The SDK fetches the access token itself.
security = models.Security(oauth2=models.SchemeOauth2(
    client_id=os.environ["PIPESHUB_CLIENT_ID"],
    client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
    token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
))
upload_path = Path(os.environ["PIPESHUB_UPLOAD_PATH"])


async def main() -> None:
    async with SDK(server_url=server_url, security=security) as client:
        kb = await client.knowledge_base.create_knowledge_base_async(
            kb_name="Internal documents",
        )
        try:
            upload_stream = await client.knowledge_base.upload_records_async(
                kb_id=kb.id,
                files=[{"file_name": upload_path.name, "content": upload_path.read_bytes()}],
            )
            # The new record's ID arrives in the `file:succeeded` event.
            record_id = None
            async for event in upload_stream:
                if event.event == "file:succeeded" and event.data:
                    record_id = event.data["recordId"]
            assert record_id is not None

            record = await client.knowledge_base.get_record_by_id_async(record_id=record_id)
            print(record.model_dump_json(indent=2))
        finally:
            await client.knowledge_base.delete_knowledge_base_async(kb_id=kb.id)


if __name__ == "__main__":
    asyncio.run(main())
