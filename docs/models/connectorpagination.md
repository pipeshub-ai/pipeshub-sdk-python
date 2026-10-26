# ConnectorPagination


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `page`                                   | *int*                                    | :heavy_check_mark:                       | N/A                                      |
| `limit`                                  | *int*                                    | :heavy_check_mark:                       | N/A                                      |
| `search`                                 | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | The search term the list was filtered by |
| `total_count`                            | *int*                                    | :heavy_check_mark:                       | N/A                                      |
| `total_pages`                            | *int*                                    | :heavy_check_mark:                       | N/A                                      |
| `has_prev`                               | *bool*                                   | :heavy_check_mark:                       | N/A                                      |
| `has_next`                               | *bool*                                   | :heavy_check_mark:                       | N/A                                      |
| `prev_page`                              | *OptionalNullable[int]*                  | :heavy_minus_sign:                       | N/A                                      |
| `next_page`                              | *OptionalNullable[int]*                  | :heavy_minus_sign:                       | N/A                                      |