# SemanticSearchHistoryMeta

`requestId` comes from `req.context?.requestId` and is omitted from
the JSON when upstream middleware did not set it.



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `duration`                                                           | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |