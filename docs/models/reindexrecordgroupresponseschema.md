# ReIndexRecordGroupResponseSchema

Response returned by POST /knowledgeBase/reindex/record-group/{recordGroupId}.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `success`               | *bool*                  | :heavy_check_mark:      | N/A                     |
| `message`               | *str*                   | :heavy_check_mark:      | N/A                     |
| `record_group_id`       | *str*                   | :heavy_check_mark:      | N/A                     |
| `depth`                 | *int*                   | :heavy_check_mark:      | N/A                     |
| `connector`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `event_published`       | *bool*                  | :heavy_check_mark:      | N/A                     |