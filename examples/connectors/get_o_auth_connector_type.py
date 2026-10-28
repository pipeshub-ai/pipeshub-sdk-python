"""Get the OAuth setup details of a connector type.

Env: PIPESHUB_BEARER_AUTH, PIPESHUB_BASE_URL, PIPESHUB_CONNECTOR_TYPE.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
connector_type = os.environ["PIPESHUB_CONNECTOR_TYPE"]

with Pipeshub(
    server_url=server_url,
    security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
) as pipeshub:
    res = pipeshub.o_auth_configuration.get_o_auth_connector_type(connector_type=connector_type)
    print(res)
