# AgentAddMessageResponseMeta


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request_id`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Request correlation id. Omitted when no request id was set on the context. |
| `timestamp`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_check_mark:                                                         | Server timestamp when the response was sent.                               |
| `duration`                                                                 | *int*                                                                      | :heavy_check_mark:                                                         | Total handler duration in milliseconds.                                    |
| `records_used`                                                             | *int*                                                                      | :heavy_check_mark:                                                         | Same value as the top-level `recordsUsed`.                                 |