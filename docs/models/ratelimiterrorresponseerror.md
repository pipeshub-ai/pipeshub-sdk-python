# RateLimitErrorResponseError


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `code`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Error code.                                |
| `message`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `retry_after`                              | *OptionalNullable[int]*                    | :heavy_minus_sign:                         | Suggested seconds to wait before retrying. |