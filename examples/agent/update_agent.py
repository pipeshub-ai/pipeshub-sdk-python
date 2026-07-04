"""Update an agent.

Creates a lightweight agent, renames it, fetches it again to confirm the change,
then deletes it to clean up.
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
            name="Update Demo Agent",
            description="Demo agent created by the update_agent example.",
            system_prompt="You are a helpful assistant.",
            models=[{
                "model_key": model_key,
                "model_name": model_name,
                "provider": model_provider,
                "is_reasoning": True,
            }],
        )
        agent_key = created.agent.key

        # Rename the agent
        await pipeshub_client.agents.update_agent_async(
            agent_key=agent_key,
            name="Update Demo Agent (updated)",
            description="Updated by the update_agent example.",
        )

        # Get the agent again to confirm the update
        updated = await pipeshub_client.agents.get_agent_async(agent_key=agent_key)
        print(updated.model_dump_json(indent=2))

        # Clean up the agent created for this example
        await pipeshub_client.agents.delete_agent_async(agent_key=agent_key)


if __name__ == "__main__":
    asyncio.run(main())
