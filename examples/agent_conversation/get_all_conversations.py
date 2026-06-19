import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models

PAGE_LIMIT = 20


def main() -> None:
    load_dotenv()
    AGENT_KEY = os.environ["AGENT_KEY"]

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        print(f"Active conversations for agent {AGENT_KEY} (newest first):")
        conversations = []
        page = 1

        while True:
            res = pipeshub_client.agents.list_agent_conversations(
                agent_key=AGENT_KEY,
                page=page,
                limit=PAGE_LIMIT,
                sort_by="lastActivityAt",
                sort_order="desc",
            )
            conversations.extend(res.conversations)
            p = res.pagination
            if not p.has_next_page or page >= p.total_pages:
                break
            page += 1

        if not conversations:
            print("  (none)")
            return

        for conv in conversations:
            title = conv.title or "(untitled)"
            if conv.last_activity_at:
                activity = datetime.fromtimestamp(
                    conv.last_activity_at / 1000, tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M:%S UTC")
            elif conv.updated_at:
                activity = conv.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
            else:
                activity = "-"
            print(f"  - {title!r} - {conv.id} - {activity}")


if __name__ == "__main__":
    main()
