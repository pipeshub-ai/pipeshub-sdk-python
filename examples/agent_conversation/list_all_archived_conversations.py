import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

QUERIES = [
    "What is 2+2?",
    "Name three primary colors.",
    "What day comes after Monday?",
]


def main() -> None:
    load_dotenv()
    AGENT_KEY = os.environ["AGENT_KEY"]
    FILTERS: FiltersTypedDict = {"apps": [os.environ["CONNECTOR_APP_KEY"]]}

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
        timeout_ms=300_000,
    ) as pipeshub_client:
        print(f"Using agent {AGENT_KEY}\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Creating conversation {i}/{len(QUERIES)}...")
            stream = pipeshub_client.agents.stream_agent_conversation(
                agent_key=AGENT_KEY,
                query=query,
                filters=FILTERS,
                chat_mode="quick",
            )
            conv_id = None
            title = ""
            for event in stream:
                if event.event == "RUN_ERROR":
                    raise RuntimeError(f"stream error: {event.data}")
                if event.event == "RUN_FINISHED" and event.data:
                    conversation = event.data["result"]["conversation"]
                    conv_id = conversation["_id"]
                    title = conversation.get("title") or ""
                    break
            if conv_id is None:
                raise RuntimeError("stream ended without a RUN_FINISHED event")
            title = title or query

            pipeshub_client.agents.archive_agent_conversation(
                agent_key=AGENT_KEY,
                conversation_id=conv_id,
            )
            print(f"  archived {conv_id} - {title!r}")

        print("\nArchived conversations for this agent (newest first):")
        archived = []
        page = 1
        while True:
            res = pipeshub_client.agents.list_agent_conversation_archives(
                agent_key=AGENT_KEY,
                page=page,
                limit=20,
                sort_by="lastActivityAt",
                sort_order="desc",
            )
            archived.extend(res.conversations)
            p = res.pagination
            if not p.has_next_page or page >= p.total_pages:
                break
            page += 1

        if not archived:
            print("  (no archived conversations for this agent)")
        else:
            for conv in archived:
                title = conv.title or "(untitled)"
                archived_at = (
                    conv.archived_at.strftime("%Y-%m-%d %H:%M:%S %Z") if conv.archived_at else "-"
                )
                print(f"  - {title!r} - {conv.id} - archived {archived_at}")


if __name__ == "__main__":
    main()
