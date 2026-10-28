# ReIndexRecordGroupResponseSchema

Response returned by POST /knowledgeBase/reindex/record-group/{recordGroupId}.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `success`                                                | *Literal[True]*                                          | :heavy_check_mark:                                       | N/A                                                      |
| `message`                                                | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `record_group_id`                                        | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `depth`                                                  | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `connector_id`                                           | *str*                                                    | :heavy_check_mark:                                       | Id of the connector instance the record group belongs to |
| `connector`                                              | *Nullable[str]*                                          | :heavy_check_mark:                                       | N/A                                                      |
| `event_published`                                        | *bool*                                                   | :heavy_check_mark:                                       | N/A                                                      |