"""Register a Confluence Cloud connector with an API token, sync one space and index it, then search it.

Reads the connector's auth fields from the registry, creates a team
"Confluence" connector with an Atlassian API token
(PIPESHUB_ATLASSIAN_BASE_URL, PIPESHUB_ATLASSIAN_EMAIL,
PIPESHUB_ATLASSIAN_API_TOKEN), limits its sync to one space
(PIPESHUB_CONFLUENCE_SPACE_KEY, or the first space it can see), turns the sync
on, waits until the sync and indexing have finished, runs a semantic search
scoped to the connector, and finally turns the sync off and deletes the
connector.

Confluence records keep Confluence's permissions, so search only finds pages
for PipesHub users whose email can view them in Confluence. The example reports
that instead of failing when the caller sees none.
"""

import asyncio
import os
import time
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, errors, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
# OAuth2 client credentials. The SDK fetches the access token itself.
security = models.Security(oauth2=models.SchemeOauth2(
    client_id=os.environ["PIPESHUB_CLIENT_ID"],
    client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
    token_url=os.environ.get("PIPESHUB_TOKEN_URL") or f"{server_url}/oauth2/token",
))
atlassian_base_url = os.environ["PIPESHUB_ATLASSIAN_BASE_URL"]
atlassian_email = os.environ["PIPESHUB_ATLASSIAN_EMAIL"]
atlassian_api_token = os.environ["PIPESHUB_ATLASSIAN_API_TOKEN"]
preferred_space_keys = os.environ.get("PIPESHUB_CONFLUENCE_SPACE_KEY")
search_query = os.environ.get("PIPESHUB_CONFLUENCE_SEARCH_QUERY") or "onboarding"

CONNECTOR_TYPE = "Confluence"
AUTH_TYPE = "API_TOKEN"
# Indexing statuses that mean a record is still on its way.
PENDING = ("not_started", "queued", "in_progress")


async def wait_until_indexed(client: SDK, connector_id: str, timeout_s: int = 1800) -> models.Stats:
    """Poll until the sync has finished and no record is still waiting to be indexed.

    A sync can legitimately find nothing, so finishing is judged from the
    connector's status, not from the record count.
    """
    started_at = time.monotonic()
    seen_sync = False
    while True:
        connector = (await client.connector_instances.get_connector_instance_async(
            connector_id=connector_id,
        )).connector
        syncing = connector.status in ("SYNCING", "FULL_SYNCING")
        stats = (await client.connector_instances.get_connector_stats_async(
            connector_id=connector_id,
        )).data.stats
        counts = stats.indexing_status
        pending = sum(getattr(counts, s) or 0 for s in PENDING)
        seen_sync = seen_sync or syncing or bool(stats.total)
        print(f"status: {connector.status}  records: {stats.total}  indexed: {counts.completed}  "
              f"pending: {pending}  failed: {counts.failed}")
        # Give the sync a minute to show up before trusting an idle status.
        if not syncing and not pending and (seen_sync or time.monotonic() - started_at > 60):
            return stats
        if time.monotonic() - started_at > timeout_s:
            raise TimeoutError(f"sync or indexing still running after {timeout_s}s")
        await asyncio.sleep(15)


async def search(client: SDK, connector_id: str) -> None:
    """Search the connector and print each matching record once (hits are chunks)."""
    try:
        results = await client.semantic_search.search_async(
            query=search_query,
            filters={"apps": [connector_id]},
            limit=3,
        )
    except errors.PipeshubDefaultError as e:
        # Search answers 404 when the caller can see no indexed record.
        if e.status_code != 404:
            raise
        print("search: nothing you can see yet. This connector keeps the source's permissions, "
              "so only PipesHub users whose email has access in the source find its records")
        return
    names = dict.fromkeys(
        hit.metadata.record_name for hit in results.search_response.search_results if hit.metadata
    )
    for name in names:
        print(f"- {name}")


async def main() -> None:
    async with SDK(server_url=server_url, security=security, timeout_ms=120_000) as client:
        schema = await client.connector_registry.get_connector_schema_async(connector_type=CONNECTOR_TYPE)
        fields = schema.schema_.auth.schemas[AUTH_TYPE].fields
        print(f"{CONNECTOR_TYPE} auth fields:", [f.name for f in fields])

        created = await client.connector_instances.create_connector_instance_async(
            connector_type=CONNECTOR_TYPE,
            instance_name="Confluence example",
            scope="team",
            auth_type=AUTH_TYPE,
            config={
                # Auth fields are keyed by the registry schema's field names.
                "auth": {"baseUrl": atlassian_base_url, "email": atlassian_email, "apiToken": atlassian_api_token},
                "sync": {"selectedStrategy": "MANUAL"},
            },
        )
        connector_id = created.connector.connector_id
        print(f"created connector {connector_id}")
        try:
            options = (await client.connector_filters.get_filter_field_options_async(
                connector_id=connector_id,
                filter_key="space_keys",
                limit=10,
            )).options
            print("spaces it can sync:", [o.label for o in options])
            # The options are paged; an explicit value needs no lookup.
            chosen = preferred_space_keys or (options[0].id if options else None)
            if not chosen:
                raise RuntimeError("the connector can't see any space")

            # Filter values are keyed by the schema's filter names; each has an operator and a type.
            await client.connector_configuration.update_connector_filters_sync_config_async(
                connector_id=connector_id,
                filters={"sync": {"values": {
                    "space_keys": {"operator": "in", "value": [chosen], "type": "list"},
                }}},
            )
            print(f"syncing space {chosen}; sync filters:", ['space_keys'])

            # Toggling flips the sync state; turning it on tests the credentials and starts a full sync.
            await client.connector_control.toggle_connector_async(connector_id=connector_id, type_="sync")
            print("sync on")

            stats = await wait_until_indexed(client, connector_id)
            print(f"indexed {stats.indexing_status.completed} of {stats.total} records")
            await search(client, connector_id)
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
