# OAuthRegistryPagination

Pagination block of `GET /oauth/registry` and `GET /oauth/{connectorType}`


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `page`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | Current page number                             |
| `limit`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Items per page                                  |
| `search`                                        | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | The search term that was applied, or null       |
| `total_count`                                   | *Optional[int]*                                 | :heavy_minus_sign:                              | Number of items that match                      |
| `total_pages`                                   | *Optional[int]*                                 | :heavy_minus_sign:                              | N/A                                             |
| `has_prev`                                      | *Optional[bool]*                                | :heavy_minus_sign:                              | N/A                                             |
| `has_next`                                      | *Optional[bool]*                                | :heavy_minus_sign:                              | N/A                                             |
| `prev_page`                                     | *OptionalNullable[int]*                         | :heavy_minus_sign:                              | Previous page number, or null on the first page |
| `next_page`                                     | *OptionalNullable[int]*                         | :heavy_minus_sign:                              | Next page number, or null on the last page      |