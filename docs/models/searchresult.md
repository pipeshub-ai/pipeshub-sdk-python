# SearchResult

Result of a semantic search operation, containing matching
document chunks with relevance scores.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Unique search record identifier                                            |
| `search_id`                                                                | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Alias for _id                                                              |
| `query`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The original search query                                                  |
| `results`                                                                  | List[[models.SearchResultItem](../models/searchresultitem.md)]             | :heavy_minus_sign:                                                         | Matching content chunks                                                    |
| `records`                                                                  | Dict[str, *str*]                                                           | :heavy_minus_sign:                                                         | Map of record IDs to record names                                          |
| `user_id`                                                                  | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `org_id`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `is_shared`                                                                | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `shared_with`                                                              | List[[models.SearchResultSharedWith](../models/searchresultsharedwith.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |
| `is_archived`                                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |