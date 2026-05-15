# GetArchivedConversationsPagination


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `page`                                           | *Optional[int]*                                  | :heavy_minus_sign:                               | Current page number                              |
| `limit`                                          | *Optional[int]*                                  | :heavy_minus_sign:                               | Items per page                                   |
| `total_count`                                    | *Optional[int]*                                  | :heavy_minus_sign:                               | Total archived conversations matching the filter |
| `total_pages`                                    | *Optional[int]*                                  | :heavy_minus_sign:                               | Total pages at the current limit                 |
| `has_next_page`                                  | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether a next page exists                       |
| `has_prev_page`                                  | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether a previous page exists                   |