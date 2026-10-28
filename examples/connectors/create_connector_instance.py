"""Create a team RSS connector for one feed.

Env: PIPESHUB_BEARER_AUTH, PIPESHUB_BASE_URL.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'

with Pipeshub(
    server_url=server_url,
    security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
) as pipeshub:
    res = pipeshub.connector_instances.create_connector_instance(
        connector_type="RSS",
        instance_name="RSS example",
        scope="team",
        auth_type="NONE",
        config={
            "auth": {},
            "sync": {
                "selectedStrategy": "MANUAL",
                "feed_urls": "http://feeds.arstechnica.com/arstechnica/index/",
                "max_articles_per_feed": 10,
                "fetch_full_content": False,
            },
        },
    )
    print(res.connector.connector_id)
