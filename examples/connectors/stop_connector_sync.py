"""Stop a connector's running sync.

Env: PIPESHUB_BEARER_AUTH, PIPESHUB_BASE_URL, PIPESHUB_CONNECTOR_ID.
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
    security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
) as pipeshub:
    res = pipeshub.connector_instances.stop_connector_sync(connector_id=connector_id)
    print(res)
