"""Create a conversation and wait for the full answer (non-streaming).

Env: PIPESHUB_CLIENT_ID, PIPESHUB_CLIENT_SECRET, PIPESHUB_BASE_URL
(optional PIPESHUB_TOKEN_URL).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'

with Pipeshub(
    server_url=server_url,
    timeout_ms=300_000,
    security=models.Security(oauth2=models.SchemeOauth2(
        client_id=os.environ["PIPESHUB_CLIENT_ID"],
        client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
        token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
    )),
) as pipeshub:
    res = pipeshub.conversations.create_conversation(
        query="Who moved the cheese?",
        chat_mode="internal_search",
    )
    print(res.result.conversation.id)
