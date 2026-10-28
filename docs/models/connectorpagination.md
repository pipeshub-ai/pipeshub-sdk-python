# ConnectorPagination


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `page`                                                | *int*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `limit`                                               | *int*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `search`                                              | *OptionalNullable[str]*                               | :heavy_minus_sign:                                    | The search term the list was filtered by              |
| `total_count`                                         | *int*                                                 | :heavy_check_mark:                                    | Number of items matching the request across all pages |
| `total_pages`                                         | *int*                                                 | :heavy_check_mark:                                    | Number of pages at the current `limit`                |
| `has_prev`                                            | *bool*                                                | :heavy_check_mark:                                    | Whether a page exists before this one                 |
| `has_next`                                            | *bool*                                                | :heavy_check_mark:                                    | Whether a page exists after this one                  |
| `prev_page`                                           | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | Previous page number, `null` on the first page        |
| `next_page`                                           | *OptionalNullable[int]*                               | :heavy_minus_sign:                                    | Next page number, `null` on the last page             |