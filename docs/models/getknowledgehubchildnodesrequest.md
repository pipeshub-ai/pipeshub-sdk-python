# GetKnowledgeHubChildNodesRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `parent_type`                                    | *str*                                            | :heavy_check_mark:                               | Type of parent node (KB, FOLDER, CONNECTOR, APP) |
| `parent_id`                                      | *str*                                            | :heavy_check_mark:                               | ID of parent node                                |
| `page`                                           | *Optional[int]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `limit`                                          | *Optional[int]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `q`                                              | *Optional[str]*                                  | :heavy_minus_sign:                               | Search query                                     |