# GetAllConversationsValues

Current value for each applied filter. Only keys
present in `filters` are populated; others are
omitted.



## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `search`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `shared`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `tags`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `min_messages`                                                   | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `sort_by`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `sort_order`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `start_date`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `end_date`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `message_type`                                                   | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `page`                                                           | *Optional[int]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `limit`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `date_range`                                                     | [Optional[models.ValuesDateRange]](../models/valuesdaterange.md) | :heavy_minus_sign:                                               | N/A                                                              |