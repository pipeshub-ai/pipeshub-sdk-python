"""Get an agent by key.

Creates a lightweight agent, fetches it by key, then deletes it to clean up.
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

        created = await pipeshub_client.agents.create_agent_async(
            name="Get Demo Agent",
            description="Demo agent created by the get_agent example.",
            system_prompt="You are a helpful assistant.",
            models=[{
                "model_key": model_key,
                "model_name": model_name,
                "provider": model_provider,
                "is_reasoning": True,
            }],
        )
        agent_key = created.agent.key

        # Get the agent by key
        fetched = await pipeshub_client.agents.get_agent_async(agent_key=agent_key)
        print(fetched.model_dump_json(indent=2))

        # Clean up the agent created for this example
        await pipeshub_client.agents.delete_agent_async(agent_key=agent_key)


if __name__ == "__main__":
    asyncio.run(main())
