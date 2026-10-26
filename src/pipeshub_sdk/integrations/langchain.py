"""PipesHub as a LangChain retriever.

    from pipeshub_sdk import Pipeshub, models
    from pipeshub_sdk.integrations.langchain import PipesHubRetriever

    client = Pipeshub(server_url=".../api/v1", security=models.Security(bearer_auth=token))
    docs = PipesHubRetriever(client=client, limit=5).invoke("How do we roll back a canary?")

Each ``Document`` holds one chunk: ``page_content`` is its text, ``id`` is the
chunk id, and ``metadata`` has the record (``recordId``, ``name``,
``connector``, ``mimeType``, ``updatedAt``), the citation (``url``,
``recordUrl``, ``pageNum``, ``blockIndex``) and ``score``.
"""

from typing import Any, List, Optional

from langchain_core.callbacks import (
    AsyncCallbackManagerForRetrieverRun,
    CallbackManagerForRetrieverRun,
)
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from pydantic import ConfigDict, Field

from pipeshub_sdk import models
from pipeshub_sdk.integrations import _chunks
from pipeshub_sdk.sdk import Pipeshub


class PipesHubRetriever(BaseRetriever):
    """Permission-filtered passages with citations from ``POST /retrieve``."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: Pipeshub
    limit: int = Field(default=8, ge=1, le=50)
    filters: Optional[models.FiltersTypedDict] = None
    max_chunks_per_record: Optional[int] = Field(default=None, ge=1, le=50)
    rewrite_query: bool = False

    def _options(self) -> dict[str, Any]:
        return _chunks.retrieve_options(
            self.limit, self.filters, self.max_chunks_per_record, self.rewrite_query
        )

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return [_document(c) for c in _chunks.retrieve(self.client, query, self._options())]

    async def _aget_relevant_documents(
        self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun
    ) -> List[Document]:
        chunks = await _chunks.retrieve_async(self.client, query, self._options())
        return [_document(c) for c in chunks]


def _document(chunk: models.RetrieveChunk) -> Document:
    return Document(id=chunk.id, page_content=chunk.text, metadata=_chunks.chunk_metadata(chunk))
