# ParentNode

Parent of `currentNode` when present; `null` when not applicable.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `name`                                           | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `node_type`                                      | *str*                                            | :heavy_check_mark:                               | One of `app`, `recordGroup`, `folder`, `record`. |
| `sub_type`                                       | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | N/A                                              |