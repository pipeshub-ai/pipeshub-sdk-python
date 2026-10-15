"""Register an RSS connector, sync and index a feed, then search what it indexed.

Looks RSS up in the connector registry, creates a team RSS connector for
PIPESHUB_RSS_FEED_URL (default: Hacker News), turns its sync on, waits until
every record is indexed, runs a semantic search scoped to the connector, and
finally turns the sync off and deletes the connector.
"""

import asyncio
import os
import time
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
# OAuth2 client credentials. The SDK fetches the access token itself.
security = models.Security(oauth2=models.SchemeOauth2(
    client_id=os.environ["PIPESHUB_CLIENT_ID"],
    client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
    token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
))
feed_url = os.environ.get("PIPESHUB_RSS_FEED_URL") or "https://news.ycombinator.com/rss"

# Indexing statuses that mean a record is still on its way.
PENDING = ("not_started", "queued", "in_progress")


async def wait_until_indexed(client: SDK, connector_id: str, timeout_s: int = 600) -> models.Stats:
    """Poll the connector's stats until it has records and none is still pending."""
    deadline = time.monotonic() + timeout_s
    while True:
        stats = (await client.connector_instances.get_connector_stats_async(
            connector_id=connector_id,
        )).data.stats
        counts = stats.indexing_status
        pending = sum(getattr(counts, s) or 0 for s in PENDING)
        print(f"records: {stats.total}  indexed: {counts.completed}  pending: {pending}  failed: {counts.failed}")
        if stats.total and not pending:
            return stats
        if time.monotonic() > deadline:
            raise TimeoutError(f"records still pending after {timeout_s}s")
        await asyncio.sleep(10)


async def main() -> None:
    async with SDK(server_url=server_url, security=security, timeout_ms=120_000) as client:
        registry = await client.connector_registry.get_connector_registry_async(search="RSS")
        rss = next(c for c in registry.connectors if c.type == "RSS")
        print(f"registry: {rss.name} ({rss.type}), auth types {rss.supported_auth_types}")

        schema = await client.connector_registry.get_connector_schema_async(connector_type="RSS")
        print("sync fields:", [f.name for f in schema.schema_.sync.custom_fields])

        created = await client.connector_instances.create_connector_instance_async(
            connector_type="RSS",
            instance_name="RSS example",
            scope="team",
            auth_type="NONE",
            config={
                "auth": {},
                "sync": {
                    "selectedStrategy": "MANUAL",
                    "feed_urls": feed_url,
                    "max_articles_per_feed": 10,
                    "fetch_full_content": False,
                },
            },
        )
        connector_id = created.connector.connector_id
        print(f"created connector {connector_id}")
        try:
            # Toggling flips the sync state; turning it on tests the feed and starts a full sync.
            await client.connector_control.toggle_connector_async(connector_id=connector_id, type_="sync")
            print("sync on")

            stats = await wait_until_indexed(client, connector_id)
            print(f"indexed {stats.indexing_status.completed} of {stats.total} records")

            results = await client.semantic_search.search_async(
                query="technology news",
                filters={"apps": [connector_id]},
                limit=3,
            )
            # Hits are chunks, so one record can match several times; print each record once.
            names = dict.fromkeys(
                hit.metadata.record_name for hit in results.search_response.search_results if hit.metadata
            )
            for name in names:
                print(f"- {name}")
        finally:
            instance = (await client.connector_instances.get_connector_instance_async(
                connector_id=connector_id,
            )).connector
            if instance.is_active:
                await client.connector_control.toggle_connector_async(connector_id=connector_id, type_="sync")
            await client.connector_instances.delete_connector_instance_async(connector_id=connector_id)
            print("sync off, connector deleted")


if __name__ == "__main__":
    asyncio.run(main())
