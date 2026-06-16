import os

from dotenv import load_dotenv
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import FiltersTypedDict

from helpers import stream_bot_reply

AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
FILTERS: FiltersTypedDict = {"apps": ["270d4bac-234a-4c0d-963f-84f152cd21f0"]}

FIRST_MESSAGE = "Who moved the cheese?"
SECOND_MESSAGE = "Can you give me more details on that?"


def main() -> None:
    load_dotenv()

    created: list[tuple[str, str]] = []

    with Pipeshub(
        server_url=f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1',
        security=models.Security(bearer_auth=os.environ["PIPESHUB_BEARER_AUTH"]),
    ) as pipeshub_client:
        for i, query in enumerate([FIRST_MESSAGE, SECOND_MESSAGE], 1):
            print(f"Creating conversation {i} (waiting for response...)...")
            conv_id, title, _, _ = stream_bot_reply(
                pipeshub_client.agents.stream_agent_conversation(
                    agent_key=AGENT_KEY,
                    query=query,
                    filters=FILTERS,
                    chat_mode="auto",
                ),
                print_output=False,
            )
            created.append((conv_id, title or query))

            pipeshub_client.agents.archive_agent_conversation(
                agent_key=AGENT_KEY,
                conversation_id=conv_id,
            )

        print("\nCreated and archived:")
        for i, (conv_id, title) in enumerate(created, 1):
            print(f"  {i}. {conv_id} - {title!r}")

        res = pipeshub_client.agents.list_agent_archived_conversations_grouped(
            agent_page=1,
            agent_limit=20,
        )
        group = next((g for g in res.groups if g.agent_key == AGENT_KEY), None)

        print("\nArchived conversations for this agent (grouped list):")
        if not group:
            print("  (no group found for this agentKey)")
            return

        created_conv_ids = {conv_id: title for conv_id, title in created}
        matched = 0
        for conv in group.conversations:
            if conv.id in created_conv_ids:
                matched += 1
                print(f"  - {conv.title!r} ({conv.id})")

        if matched == 0:
            print("  (none of the conversations we created appear in this page of results)")
        elif matched == len(created):
            print(f"\nBoth conversations created in this run appear under agent {AGENT_KEY}.")
        else:
            print(f"\n{matched} of {len(created)} conversations created in this run appear under agent {AGENT_KEY}.")


if __name__ == "__main__":
    main()
