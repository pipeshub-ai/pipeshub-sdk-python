"""List the values a connector offers for one filter.

Env: PIPESHUB_BEARER_AUTH, PIPESHUB_BASE_URL, PIPESHUB_CONNECTOR_ID, PIPESHUB_FILTER_KEY.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
connector_id = os.environ["PIPESHUB_CONNECTOR_ID"]
filter_key = os.environ["PIPESHUB_FILTER_KEY"]

with Pipeshub(
    server_url=server_url,
    security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
) as pipeshub:
    res = pipeshub.connector_filters.get_filter_field_options(connector_id=connector_id, filter_key=filter_key, limit=10)
    print(res)
