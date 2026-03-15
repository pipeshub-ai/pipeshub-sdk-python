# ConnectorPagination

Pagination information for connector lists


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `page`                         | *Optional[int]*                | :heavy_minus_sign:             | Current page number            |
| `limit`                        | *Optional[int]*                | :heavy_minus_sign:             | Items per page                 |
| `search`                       | *OptionalNullable[str]*        | :heavy_minus_sign:             | Applied search query           |
| `total_count`                  | *Optional[int]*                | :heavy_minus_sign:             | Total number of items          |
| `total_pages`                  | *Optional[int]*                | :heavy_minus_sign:             | Total number of pages          |
| `has_prev`                     | *Optional[bool]*               | :heavy_minus_sign:             | Whether a previous page exists |
| `has_next`                     | *Optional[bool]*               | :heavy_minus_sign:             | Whether a next page exists     |
| `prev_page`                    | *Optional[int]*                | :heavy_minus_sign:             | Previous page number           |
| `next_page`                    | *Optional[int]*                | :heavy_minus_sign:             | Next page number               |