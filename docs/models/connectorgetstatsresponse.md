# ConnectorGetStatsResponse

Connector statistics


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `total_records`                        | *Optional[int]*                        | :heavy_minus_sign:                     | Total number of records                |
| `indexed_records`                      | *Optional[int]*                        | :heavy_minus_sign:                     | Number of successfully indexed records |
| `failed_records`                       | *Optional[int]*                        | :heavy_minus_sign:                     | Number of failed records               |
| `pending_records`                      | *Optional[int]*                        | :heavy_minus_sign:                     | Number of pending records              |
| `last_sync_timestamp`                  | *Optional[int]*                        | :heavy_minus_sign:                     | Last sync timestamp                    |