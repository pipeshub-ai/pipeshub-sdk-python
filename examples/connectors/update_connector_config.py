"""Update a connector's sync config (the connector must be disabled).

Env: PIPESHUB_CLIENT_ID, PIPESHUB_CLIENT_SECRET, PIPESHUB_BASE_URL, PIPESHUB_CONNECTOR_ID
(optional PIPESHUB_TOKEN_URL).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
connector_id = os.environ["PIPESHUB_CONNECTOR_ID"]

with Pipeshub(
    server_url=server_url,
    security=models.Security(oauth2=models.SchemeOauth2(
        client_id=os.environ["PIPESHUB_CLIENT_ID"],
        client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
        token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
    )),
) as pipeshub:
    res = pipeshub.connector_configuration.update_connector_config(
        connector_id=connector_id,
        sync={"selectedStrategy": "MANUAL", "feed_urls": "http://feeds.arstechnica.com/arstechnica/index/"},
    )
    print(res)
