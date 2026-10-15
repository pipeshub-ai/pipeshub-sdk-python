"""Get the upload limits: files per request and maximum file size."""

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


async def main() -> None:
    async with SDK(server_url=server_url, security=security) as client:
        limits = await client.knowledge_base.get_upload_limits_async()
        print(f"max files per request: {limits.max_files_per_request}")
        print(f"max file size: {limits.max_file_size_bytes} bytes")


if __name__ == "__main__":
    asyncio.run(main())
