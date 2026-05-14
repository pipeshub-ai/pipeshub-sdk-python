# SemanticSearchHistoryPagination

Pagination block emitted by `buildPaginationMetadata` (utils.ts:417).
`totalPages` is `Math.ceil(totalCount / limit)`, so an empty result
has `totalPages: 0`, not `1`.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `page`             | *int*              | :heavy_check_mark: | N/A                |
| `limit`            | *int*              | :heavy_check_mark: | N/A                |
| `total_count`      | *int*              | :heavy_check_mark: | N/A                |
| `total_pages`      | *int*              | :heavy_check_mark: | N/A                |
| `has_next_page`    | *bool*             | :heavy_check_mark: | N/A                |
| `has_prev_page`    | *bool*             | :heavy_check_mark: | N/A                |