# ReindexRecordGroupRequestBody

Request payload


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `depth`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | Processing depth (-1 for unlimited, 0 for direct records only) |
| `force`                                                        | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Force reindexing even if already indexed                       |