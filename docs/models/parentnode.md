# ParentNode

Parent of `currentNode` when present; `null` when not applicable,
and for a connected app whose limit leaves that parent out. For
such an app, `breadcrumbs` likewise names only the nodes inside
its limit.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `name`                                           | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `node_type`                                      | *str*                                            | :heavy_check_mark:                               | One of `app`, `recordGroup`, `folder`, `record`. |
| `sub_type`                                       | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | N/A                                              |