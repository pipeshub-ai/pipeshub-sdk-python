# SemanticSearchHistorySortField

Used for `available.sorting.{sortBy,sortOrder}` and
`available.sortingMessages.{sortBy,sortOrder}`. The `applied` flag
is present on `sorting.*` and absent on `sortingMessages.*`, so it
is optional here.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `values`           | List[*str*]        | :heavy_check_mark: | N/A                |
| `default`          | *str*              | :heavy_check_mark: | N/A                |
| `description`      | *str*              | :heavy_check_mark: | N/A                |
| `current`          | *str*              | :heavy_check_mark: | N/A                |
| `applied`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |