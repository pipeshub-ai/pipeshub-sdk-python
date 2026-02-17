# GetQueueStatsResponse

Queue statistics retrieved successfully


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `success`                                              | *Optional[bool]*                                       | :heavy_minus_sign:                                     | N/A                                                    | true                                                   |
| `message`                                              | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    | Queue statistics retrieved successfully                |
| `data`                                                 | [Optional[models.QueueStats]](../models/queuestats.md) | :heavy_minus_sign:                                     | Aggregate statistics for the crawling job queue        |                                                        |