"""Reindex a connector record group.

Record groups come from connectors (a drive, a space, a feed). A knowledge base
or a knowledge base folder is not a record group. The example finds the
connector named PIPESHUB_CONNECTOR_NAME through the knowledge hub, takes its
first record group and queues it for reindexing.

The knowledge hub methods are deprecated, but they are still the way to browse
a connector's record groups.
"""

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
connector_name = os.environ["PIPESHUB_CONNECTOR_NAME"]


async def main() -> None:
    async with SDK(server_url=server_url, security=security) as client:
        roots = await client.knowledge_hub.get_knowledge_hub_root_nodes_async()
        app = next(
            (node for node in roots.items
             if node.node_type == "app" and node.name == connector_name),
            None,
        )
        if app is None:
            raise RuntimeError(f"connector {connector_name!r} not found")

        children = await client.knowledge_hub.get_knowledge_hub_child_nodes_async(
            parent_type="app",
            parent_id=app.id,
        )
        group = next(
            (node for node in children.items if node.node_type == "recordGroup"),
            None,
        )
        if group is None:
            raise RuntimeError(f"connector {connector_name!r} has no record groups")
        print(f"record group: {group.name} ({group.id})")

        result = await client.knowledge_base.reindex_record_group_async(
            record_group_id=group.id,
        )
        print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
