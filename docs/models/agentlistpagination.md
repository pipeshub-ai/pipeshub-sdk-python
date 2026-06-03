# AgentListPagination

Pagination block returned by `GET /agents`.


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `current_page`                                    | *int*                                             | :heavy_check_mark:                                | Current 1-based page number.                      | 1                                                 |
| `limit`                                           | *int*                                             | :heavy_check_mark:                                | Page size actually applied by the backend.        | 20                                                |
| `total_items`                                     | *int*                                             | :heavy_check_mark:                                | Total number of matching agents across all pages. | 2                                                 |
| `total_pages`                                     | *int*                                             | :heavy_check_mark:                                | Total number of pages for the current query.      | 1                                                 |
| `has_next`                                        | *bool*                                            | :heavy_check_mark:                                | Whether a later page exists.                      | false                                             |
| `has_prev`                                        | *bool*                                            | :heavy_check_mark:                                | Whether an earlier page exists.                   | false                                             |