# CurrentNode

Node being browsed when `parentId` is in the path; `null` at root.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `node_type`                                                      | *str*                                                            | :heavy_check_mark:                                               | One of `app`, `recordGroup`, `folder`, `record`.                 |
| `sub_type`                                                       | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | Connector name or record type when applicable; otherwise `null`. |