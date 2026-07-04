"""Create an agent.

Creates an agent that attaches the first available knowledge base (discovered via
the knowledge-base list API) and DuckDuckGo web search. If no knowledge base
exists, the agent is created without a knowledge source.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

base_url = os.environ["PIPESHUB_BASE_URL"]
token = os.environ["PIPESHUB_BEARER_AUTH"]
model_key = os.environ["PIPESHUB_MODEL_KEY"]
model_name = os.environ["PIPESHUB_MODEL_NAME"]
model_provider = os.environ["PIPESHUB_MODEL_PROVIDER"]

server_url = f'{base_url.rstrip("/")}/api/v1'


async def main() -> None:
    async with SDK(
        server_url=server_url,
        security=models.Security(bearer_auth=token),
    ) as pipeshub_client:

        # Attach the first available knowledge base (if any) as a knowledge source.
        kb_list = await pipeshub_client.knowledge_base.list_knowledge_bases_async(limit=1)
        kbs = kb_list.knowledge_bases or []
        kb = kbs[0] if kbs else None
        knowledge: list[models.AgentCreateKnowledgeTypedDict] | None = (
            [{
                "connector_id": kb.connector_id,
                "filters": {"record_groups": [kb.id], "records": []},
            }]
            if kb and kb.connector_id
            else None
        )

        created = await pipeshub_client.agents.create_agent_async(
            name="CRUD Demo Agent",
            description="Demo agent created by the create_agent example.",
            system_prompt="You are a helpful assistant.",
            models=[{
                "model_key": model_key,
                "model_name": model_name,
                "provider": model_provider,
                "is_reasoning": True,
            }],
            knowledge=knowledge,
            web_search={"provider": "duckduckgo"},
        )
        print(created.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
