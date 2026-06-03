# AgentConversationDetailMeta

Request-scoped metadata returned by the by-id GET route. `requestId`
is omitted when upstream middleware did not attach one.



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `duration`                                                           | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `conversation_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `message_count`                                                      | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |