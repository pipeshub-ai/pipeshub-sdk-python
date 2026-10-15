"""Restore several records from the trash in one call.

Creates a knowledge base, uploads PIPESHUB_UPLOAD_PATH twice under two names,
deletes both records so they move to the trash, restores them together, then
deletes the knowledge base.

Requires the workspace Labs setting "Move Deleted Records to the Trash"
(`ENABLE_SOFT_DELETE`). Without it, deleting a record removes it permanently.
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
            content = upload_path.read_bytes()
            upload_stream = await client.knowledge_base.upload_records_async(
                kb_id=kb.id,
                files=[
                    {"file_name": f"copy-1-{upload_path.name}", "content": content},
                    {"file_name": f"copy-2-{upload_path.name}", "content": content},
                ],
            )
            # Each new record's ID arrives in its own `file:succeeded` event.
            record_ids = []
            async for event in upload_stream:
                if event.event == "file:succeeded" and event.data:
                    record_ids.append(event.data["recordId"])
            assert len(record_ids) == 2
            for record_id in record_ids:
                await client.knowledge_base.delete_record_async(record_id=record_id)

            restored = await client.knowledge_base.restore_records_async(record_ids=record_ids)
            print(f"restored: {restored.restored_count}, failed: {restored.failed_count}")
            for result in restored.results:
                print(f"{result.record_id}  success={result.success}  {result.message or result.reason}")
        finally:
            await client.knowledge_base.delete_knowledge_base_async(kb_id=kb.id)


if __name__ == "__main__":
    asyncio.run(main())
