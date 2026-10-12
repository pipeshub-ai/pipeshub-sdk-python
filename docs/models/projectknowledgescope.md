# ProjectKnowledgeScope

Retrieval scope (app connector / knowledge-base ids) inherited by
every conversation in the project when the request itself carries no
`filters`. Same id shapes as `Filters`.



## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `apps`                                                           | List[*str*]                                                      | :heavy_minus_sign:                                               | Connector instance ids scoping this project's default retrieval. |
| `kb`                                                             | List[*str*]                                                      | :heavy_minus_sign:                                               | Knowledge-base app ids scoping this project's default retrieval. |