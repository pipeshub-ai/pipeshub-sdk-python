# CitationReference

Reference to a source document cited in a response


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `citation_id`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | ID of the citation record                        |
| `relevance_score`                                | *Optional[float]*                                | :heavy_minus_sign:                               | How relevant this citation is to the query (0-1) |
| `excerpt`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | Relevant excerpt from the source document        |
| `context`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | Additional context around the citation           |