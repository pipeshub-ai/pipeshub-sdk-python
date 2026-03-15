# GetFilterFieldOptionsRequest


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `connector_id`                     | *str*                              | :heavy_check_mark:                 | N/A                                |                                    |
| `filter_key`                       | *str*                              | :heavy_check_mark:                 | Filter field key                   | folders                            |
| `page`                             | *Optional[int]*                    | :heavy_minus_sign:                 | N/A                                |                                    |
| `limit`                            | *Optional[int]*                    | :heavy_minus_sign:                 | N/A                                |                                    |
| `search`                           | *Optional[str]*                    | :heavy_minus_sign:                 | Search term for filtering options  |                                    |
| `cursor`                           | *Optional[str]*                    | :heavy_minus_sign:                 | Cursor for cursor-based pagination |                                    |