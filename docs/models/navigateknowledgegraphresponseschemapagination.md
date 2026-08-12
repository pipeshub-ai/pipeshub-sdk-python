# NavigateKnowledgeGraphResponseSchemaPagination

Pagination envelope for a navigate listing.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `page`                                                   | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `limit`                                                  | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `total`                                                  | *int*                                                    | :heavy_check_mark:                                       | Total children of the current node, ignoring pagination. |
| `has_next`                                               | *bool*                                                   | :heavy_check_mark:                                       | N/A                                                      |
| `has_prev`                                               | *bool*                                                   | :heavy_check_mark:                                       | N/A                                                      |