"""The framework retrievers against a mocked ``POST /retrieve``."""

import copy
import json

import httpx
import pytest

from pipeshub_sdk import Pipeshub, models

RESPONSE = {
    "requestId": "req-1",
    "incomplete": False,
    "chunks": [
        {
            "id": "v1:4",
            "text": "Roll back the canary by setting its weight to 0.",
            "score": 0.83,
            "record": {
                "recordId": "r1", "name": "Deploy runbook", "connector": "CONFLUENCE",
                "mimeType": "text/html", "updatedAt": "2026-10-01T09:12:00Z",
            },
            "citation": {
                "url": "https://wiki.example.com/runbook#:~:text=Roll%20back",
                "recordUrl": "https://wiki.example.com/runbook",
                "pageNum": None,
                "blockIndex": 4,
            },
        }
    ],
}


@pytest.fixture
def sent() -> list:
    return []


@pytest.fixture
def response() -> dict:
    return copy.deepcopy(RESPONSE)


@pytest.fixture
def client(sent: list, response: dict) -> Pipeshub:
    def handler(request: httpx.Request) -> httpx.Response:
        sent.append((request.url.path, request.headers.get("authorization"), json.loads(request.content)))
        return httpx.Response(200, json=response)

    transport = httpx.MockTransport(handler)
    return Pipeshub(
        server_url="https://pipeshub.test/api/v1",
        security=models.Security(bearer_auth="tok"),
        client=httpx.Client(transport=transport),
        async_client=httpx.AsyncClient(transport=transport),
    )


METADATA = {
    "recordId": "r1", "name": "Deploy runbook", "connector": "CONFLUENCE",
    "mimeType": "text/html", "updatedAt": "2026-10-01T09:12:00Z",
    "url": "https://wiki.example.com/runbook#:~:text=Roll%20back",
    "recordUrl": "https://wiki.example.com/runbook", "pageNum": None, "blockIndex": 4,
}


class TestLangChain:
    def test_each_chunk_becomes_a_document_with_its_citation(self, client, sent) -> None:
        pytest.importorskip("langchain_core")
        from pipeshub_sdk.integrations.langchain import PipesHubRetriever

        docs = PipesHubRetriever(client=client, limit=5, filters={"apps": ["a1"]}).invoke("canary rollback")

        assert [(d.id, d.page_content) for d in docs] == [("v1:4", "Roll back the canary by setting its weight to 0.")]
        assert docs[0].metadata == {**METADATA, "score": 0.83}
        assert sent == [(
            "/api/v1/retrieve", "Bearer tok",
            {"query": "canary rollback", "limit": 5, "filters": {"apps": ["a1"]}, "rewriteQuery": False},
        )]

    @pytest.mark.asyncio
    async def test_async_uses_the_async_client(self, client, sent) -> None:
        pytest.importorskip("langchain_core")
        from pipeshub_sdk.integrations.langchain import PipesHubRetriever

        docs = await PipesHubRetriever(client=client, max_chunks_per_record=2).ainvoke("q")

        assert docs[0].id == "v1:4"
        assert sent[0][2] == {"query": "q", "limit": 8, "maxChunksPerRecord": 2, "rewriteQuery": False}

    @pytest.mark.parametrize("key", ["recordGroups", "record_groups"])
    def test_filters_keep_record_groups_in_either_spelling(self, client, sent, key) -> None:
        pytest.importorskip("langchain_core")
        from pipeshub_sdk.integrations.langchain import PipesHubRetriever

        PipesHubRetriever(client=client, filters={"apps": ["a1"], key: ["g1"]}).invoke("q")

        assert sent[0][2]["filters"] == {"apps": ["a1"], "recordGroups": ["g1"]}

    def test_a_missing_score_is_none(self, client, response) -> None:
        pytest.importorskip("langchain_core")
        from pipeshub_sdk.integrations.langchain import PipesHubRetriever

        del response["chunks"][0]["score"]
        docs = PipesHubRetriever(client=client).invoke("q")

        assert docs[0].metadata["score"] is None
        json.dumps(docs[0].metadata)

    def test_limit_is_bounded_like_the_api(self, client) -> None:
        pytest.importorskip("langchain_core")
        from pipeshub_sdk.integrations.langchain import PipesHubRetriever

        with pytest.raises(ValueError):
            PipesHubRetriever(client=client, limit=51)


class TestLlamaIndex:
    def test_each_chunk_becomes_a_scored_node_with_its_citation(self, client, sent) -> None:
        pytest.importorskip("llama_index.core")
        from pipeshub_sdk.integrations.llamaindex import PipesHubRetriever

        nodes = PipesHubRetriever(client=client, limit=3, rewrite_query=True).retrieve("canary rollback")

        assert [(n.node.node_id, n.node.get_content(), n.score) for n in nodes] == [
            ("v1:4", "Roll back the canary by setting its weight to 0.", 0.83)
        ]
        assert nodes[0].node.metadata == METADATA
        # Links and ids are for citing, not for the model's prompt.
        assert "recordUrl" not in nodes[0].node.get_content(metadata_mode="llm")
        assert sent[0][2] == {"query": "canary rollback", "limit": 3, "rewriteQuery": True}

    def test_a_missing_score_is_none(self, client, response) -> None:
        pytest.importorskip("llama_index.core")
        from pipeshub_sdk.integrations.llamaindex import PipesHubRetriever

        del response["chunks"][0]["score"]

        assert PipesHubRetriever(client=client).retrieve("q")[0].score is None

    @pytest.mark.asyncio
    async def test_async_uses_the_async_client(self, client, sent) -> None:
        pytest.importorskip("llama_index.core")
        from pipeshub_sdk.integrations.llamaindex import PipesHubRetriever

        nodes = await PipesHubRetriever(client=client).aretrieve("q")

        assert nodes[0].node.node_id == "v1:4" and sent[0][0] == "/api/v1/retrieve"
