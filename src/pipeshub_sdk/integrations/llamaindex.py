"""PipesHub as a LlamaIndex retriever.

    from pipeshub_sdk import Pipeshub, models
    from pipeshub_sdk.integrations.llamaindex import PipesHubRetriever

    client = Pipeshub(server_url=".../api/v1", security=models.Security(bearer_auth=token))
    nodes = PipesHubRetriever(client=client, limit=5).retrieve("How do we roll back a canary?")

Each ``NodeWithScore`` holds one chunk: a ``TextNode`` whose ``id_`` is the
chunk id and whose ``metadata`` has the record and citation fields (see
``pipeshub_sdk.integrations.langchain``), with the chunk's ``score``.
"""

from typing import Any, List, Optional

from llama_index.core.base.base_retriever import BaseRetriever
from llama_index.core.schema import NodeWithScore, QueryBundle, TextNode

from pipeshub_sdk import models
from pipeshub_sdk.integrations import _chunks
from pipeshub_sdk.sdk import Pipeshub


class PipesHubRetriever(BaseRetriever):
    """Permission-filtered passages with citations from ``POST /retrieve``."""

    def __init__(
        self,
        client: Pipeshub,
        limit: int = 8,
        filters: Optional[models.FiltersTypedDict] = None,
        max_chunks_per_record: Optional[int] = None,
        rewrite_query: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._client = client
        self._options = _chunks.retrieve_options(limit, filters, max_chunks_per_record, rewrite_query)

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        chunks = _chunks.retrieve(self._client, query_bundle.query_str, self._options)
        return [_node(c) for c in chunks]

    async def _aretrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        chunks = await _chunks.retrieve_async(self._client, query_bundle.query_str, self._options)
        return [_node(c) for c in chunks]


def _node(chunk: models.RetrieveChunk) -> NodeWithScore:
    metadata = _chunks.chunk_metadata(chunk)
    score = metadata.pop("score")
    node = TextNode(id_=chunk.id, text=chunk.text, metadata=metadata)
    # The prompt gets the passage; links and ids stay in metadata for citing.
    node.excluded_llm_metadata_keys = list(metadata)
    return NodeWithScore(node=node, score=score)
