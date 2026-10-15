"""Finish an OAuth sign-in with the code and state the provider redirected back with.

Env: PIPESHUB_CLIENT_ID, PIPESHUB_CLIENT_SECRET, PIPESHUB_BASE_URL, PIPESHUB_OAUTH_CODE, PIPESHUB_OAUTH_STATE
(optional PIPESHUB_TOKEN_URL).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
oauth_code = os.environ["PIPESHUB_OAUTH_CODE"]
oauth_state = os.environ["PIPESHUB_OAUTH_STATE"]

with Pipeshub(
    server_url=server_url,
    security=models.Security(oauth2=models.SchemeOauth2(
        client_id=os.environ["PIPESHUB_CLIENT_ID"],
        client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
        token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
    )),
) as pipeshub:
    res = pipeshub.connector_o_auth.handle_o_auth_callback(
        code=oauth_code,
        state=oauth_state,
    )
    print(res)
