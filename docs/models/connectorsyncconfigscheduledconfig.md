# ConnectorSyncConfigScheduledConfig


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `interval_minutes`                                 | *Optional[int]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `timezone`                                         | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `start_time`                                       | *Optional[int]*                                    | :heavy_minus_sign:                                 | Epoch milliseconds                                 |
| `start_date_time`                                  | *Optional[Any]*                                    | :heavy_minus_sign:                                 | When the schedule starts, as the frontend sends it |
| `__pydantic_extra__`                               | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |