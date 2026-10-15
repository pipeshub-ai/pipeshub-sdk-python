"""Add a follow-up message to a conversation and wait for the answer (non-streaming).

Env: PIPESHUB_CLIENT_ID, PIPESHUB_CLIENT_SECRET, PIPESHUB_BASE_URL, PIPESHUB_CONVERSATION_ID
(optional PIPESHUB_TOKEN_URL).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
conversation_id = os.environ["PIPESHUB_CONVERSATION_ID"]

with Pipeshub(
    server_url=server_url,
    timeout_ms=300_000,
    security=models.Security(oauth2=models.SchemeOauth2(
        client_id=os.environ["PIPESHUB_CLIENT_ID"],
        client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
        token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
    )),
) as pipeshub:
    res = pipeshub.conversations.add_message(
        conversation_id=conversation_id,
        query="Summarize that in one sentence.",
        chat_mode="internal_search",
    )
    print(res.result.conversation.status)
