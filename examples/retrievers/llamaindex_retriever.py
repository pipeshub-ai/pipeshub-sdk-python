"""PipesHub as a LlamaIndex retriever: pip install "pipeshub-sdk[llamaindex]>=1.8.0"."""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models
from pipeshub_sdk.integrations.llamaindex import PipesHubRetriever

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
token = os.environ["PIPESHUB_BEARER_AUTH"]


def main() -> None:
    with SDK(server_url=server_url, security=models.Security(bearer_auth=token)) as client:
        retriever = PipesHubRetriever(client=client, limit=5)
        for result in retriever.retrieve("How do we roll back a canary deploy?"):
            # Pass the retriever to a query engine as usual; the links stay in node metadata.
            print(f"{result.score:.2f}", result.node.metadata["name"], result.node.metadata["url"])


if __name__ == "__main__":
    main()
