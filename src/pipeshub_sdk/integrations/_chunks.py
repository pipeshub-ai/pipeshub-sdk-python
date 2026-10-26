"""What every framework retriever needs from ``POST /retrieve``."""

from typing import Any, Dict, List, Optional, Union

from pipeshub_sdk import models
from pipeshub_sdk.sdk import Pipeshub


def retrieve_options(
    limit: int,
    filters: Optional[Union[models.Filters, models.FiltersTypedDict]],
    max_chunks_per_record: Optional[int],
    rewrite_query: bool,
) -> Dict[str, Any]:
    """Keyword arguments for ``retrieve``; unset options are left to the server."""
    options: Dict[str, Any] = {"limit": limit, "rewrite_query": rewrite_query}
    if filters is not None:
        options["filters"] = filters
    if max_chunks_per_record is not None:
        options["max_chunks_per_record"] = max_chunks_per_record
    return options


def chunk_metadata(chunk: models.RetrieveChunk) -> Dict[str, Any]:
    """The record and citation fields of a chunk, under the API's own names.

    ``url`` is the deep link to the passage: keep it with the text so an
    answer can cite its source.
    """
    return {
        **chunk.record.model_dump(by_alias=True),
        **chunk.citation.model_dump(by_alias=True),
        # An absent score is the SDK's UNSET sentinel, which frameworks cannot take.
        "score": chunk.score if isinstance(chunk.score, float) else None,
    }


def retrieve(client: Pipeshub, query: str, options: Dict[str, Any]) -> List[models.RetrieveChunk]:
    return client.semantic_search.retrieve(query=query, **options).chunks


async def retrieve_async(
    client: Pipeshub, query: str, options: Dict[str, Any]
) -> List[models.RetrieveChunk]:
    return (await client.semantic_search.retrieve_async(query=query, **options)).chunks
