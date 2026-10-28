# UpdateOAuthAppRequestKnowledgeLimit

`null` lifts the limit. A change that takes anything away revokes
the app's outstanding tokens, so users connect again. A change
that only adds (a lift included) keeps them: each token, and each
refresh of it, stays at the limit its user agreed to, and the new
items reach a user once they connect again.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `apps`                                                                     | List[*str*]                                                                | :heavy_minus_sign:                                                         | Whole connectors and collections.                                          |
| `record_groups`                                                            | List[*str*]                                                                | :heavy_minus_sign:                                                         | Record groups (a drive, space or project), with the groups nested in them. |
| `records`                                                                  | List[*str*]                                                                | :heavy_minus_sign:                                                         | Folders or records, with everything under them.                            |