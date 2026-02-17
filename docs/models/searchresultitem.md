# SearchResultItem

A single matching chunk from semantic search


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `content`                                                                          | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The matching text content                                                          |
| `chunk_index`                                                                      | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Index of this chunk within the source document                                     |
| `citation_type`                                                                    | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Type of citation/source                                                            |
| `metadata`                                                                         | [Optional[models.SearchResultItemMetadata]](../models/searchresultitemmetadata.md) | :heavy_minus_sign:                                                                 | Additional metadata about the source                                               |
| `score`                                                                            | *Optional[float]*                                                                  | :heavy_minus_sign:                                                                 | Relevance score (higher is more relevant)                                          |