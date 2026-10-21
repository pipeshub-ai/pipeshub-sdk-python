# KnowledgeHubNodesResponsePagination


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `page`                                                    | *int*                                                     | :heavy_check_mark:                                        | Current page (1-indexed).                                 |
| `limit`                                                   | *int*                                                     | :heavy_check_mark:                                        | Page size.                                                |
| `total_items`                                             | *int*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `total_pages`                                             | *int*                                                     | :heavy_check_mark:                                        | N/A                                                       |
| `has_next`                                                | *bool*                                                    | :heavy_check_mark:                                        | N/A                                                       |
| `has_prev`                                                | *bool*                                                    | :heavy_check_mark:                                        | N/A                                                       |
| `next_cursor`                                             | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | Cursor for the next page; null on the last page.          |
| `prev_cursor`                                             | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | Cursor for the previous page; null on the first page.     |
| `start_index`                                             | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | 1-based index of the first item on this page, when known. |
| `end_index`                                               | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | 1-based index of the last item on this page, when known.  |
| `current_page_items`                                      | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | Number of items on this page.                             |