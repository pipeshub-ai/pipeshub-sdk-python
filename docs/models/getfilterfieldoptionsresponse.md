# GetFilterFieldOptionsResponse

Filter options


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `success`                                  | *bool*                                     | :heavy_check_mark:                         | N/A                                        |
| `options`                                  | List[[models.Option](../models/option.md)] | :heavy_check_mark:                         | N/A                                        |
| `page`                                     | *Optional[int]*                            | :heavy_minus_sign:                         | N/A                                        |
| `limit`                                    | *Optional[int]*                            | :heavy_minus_sign:                         | N/A                                        |
| `has_more`                                 | *Optional[bool]*                           | :heavy_minus_sign:                         | N/A                                        |
| `cursor`                                   | *OptionalNullable[str]*                    | :heavy_minus_sign:                         | Pass back to get the next page             |
| `message`                                  | *OptionalNullable[str]*                    | :heavy_minus_sign:                         | N/A                                        |