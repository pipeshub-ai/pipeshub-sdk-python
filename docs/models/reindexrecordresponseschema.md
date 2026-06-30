# ReIndexRecordResponseSchema

Response returned by POST /knowledgeBase/reindex/record/{recordId}.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `success`               | *bool*                  | :heavy_check_mark:      | N/A                     |
| `message`               | *str*                   | :heavy_check_mark:      | N/A                     |
| `record_id`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `record_name`           | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `connector`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `event_published`       | *bool*                  | :heavy_check_mark:      | N/A                     |
| `user_role`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `depth`                 | *int*                   | :heavy_check_mark:      | N/A                     |