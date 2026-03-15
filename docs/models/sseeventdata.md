# SSEEventData

Event payload


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `message`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Status or connection message                                    |
| `status`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Current processing status                                       |
| `chunk`                                                         | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Partial response text (for answer_chunk events)                 |
| `accumulated`                                                   | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Full accumulated response text so far (for answer_chunk events) |
| `citations`                                                     | List[[models.Citation](../models/citation.md)]                  | :heavy_minus_sign:                                              | Citation references (for answer_chunk events)                   |