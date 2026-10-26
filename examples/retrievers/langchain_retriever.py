"""PipesHub as a LangChain retriever: pip install "pipeshub-sdk[langchain]>=1.8.0"."""

import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models
from pipeshub_sdk.integrations.langchain import PipesHubRetriever

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
token = os.environ["PIPESHUB_BEARER_AUTH"]


def main() -> None:
    with SDK(server_url=server_url, security=models.Security(bearer_auth=token)) as client:
        retriever = PipesHubRetriever(client=client, limit=5)
        for doc in retriever.invoke("How do we roll back a canary deploy?"):
            # Cite doc.metadata["url"] next to anything the model says from doc.page_content.
            print(doc.metadata["name"], doc.metadata["url"])


if __name__ == "__main__":
    main()
