# UpdateOAuthAppRequestKnowledgeLimit

`null` lifts the limit. Any change, a lift included, revokes the
app's outstanding tokens, so users connect again.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `apps`                                                                     | List[*str*]                                                                | :heavy_minus_sign:                                                         | Whole connectors and collections.                                          |
| `record_groups`                                                            | List[*str*]                                                                | :heavy_minus_sign:                                                         | Record groups (a drive, space or project), with the groups nested in them. |
| `records`                                                                  | List[*str*]                                                                | :heavy_minus_sign:                                                         | Folders or records, with everything under them.                            |