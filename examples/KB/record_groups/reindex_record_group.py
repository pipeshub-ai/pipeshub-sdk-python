"""Reindex a connector record group.

Env: PIPESHUB_CLIENT_ID, PIPESHUB_CLIENT_SECRET, PIPESHUB_BASE_URL, PIPESHUB_RECORD_GROUP_ID
(optional PIPESHUB_TOKEN_URL).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
record_group_id = os.environ["PIPESHUB_RECORD_GROUP_ID"]

with Pipeshub(
    server_url=server_url,
    security=models.Security(oauth2=models.SchemeOauth2(
        client_id=os.environ["PIPESHUB_CLIENT_ID"],
        client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
        token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
    )),
) as pipeshub:
    res = pipeshub.knowledge_base.reindex_record_group(record_group_id=record_group_id)
    print(res)
