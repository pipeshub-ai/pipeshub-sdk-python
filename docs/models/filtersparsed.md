# FiltersParsed

Server-derived read-only object parsed from the stored
`filters` JSON by the graph provider on GET (Neo4j / Arango).
Empty object when `filters` is missing or invalid JSON.



## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `record_groups`                                        | List[*str*]                                            | :heavy_minus_sign:                                     | Record-group ids (e.g. knowledge-base roots) in scope. |
| `records`                                              | List[*str*]                                            | :heavy_minus_sign:                                     | Individual record ids in scope.                        |