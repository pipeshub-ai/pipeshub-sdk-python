# SemanticSearchHistoryFilterToggle

Generic "filter X is available, current value is Y" block used for
`shared`, `tags`, `minMessages`, `search`, and `messageType`. Either
`type` (free-form value) or `values` (enum of allowed strings) is
present, not both. `current` is the caller-supplied value passed
through from `req.query`, hence string-or-null even when `type` is
`'number'`.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `values`           | List[*str*]        | :heavy_minus_sign: | N/A                |
| `description`      | *str*              | :heavy_check_mark: | N/A                |
| `current`          | *Nullable[str]*    | :heavy_check_mark: | N/A                |
| `applied`          | *bool*             | :heavy_check_mark: | N/A                |