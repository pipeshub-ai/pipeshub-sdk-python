# ConnectorPagination

Pagination information for connector lists


## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `page`                   | *Optional[int]*          | :heavy_minus_sign:       | Current page number      |
| `limit`                  | *Optional[int]*          | :heavy_minus_sign:       | Items per page           |
| `total`                  | *Optional[int]*          | :heavy_minus_sign:       | Total number of items    |
| `has_more`               | *Optional[bool]*         | :heavy_minus_sign:       | Whether more pages exist |