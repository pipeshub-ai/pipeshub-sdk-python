# DeleteRecordResponseSchema

Response returned by DELETE /knowledgeBase/record/{recordId}.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `success`               | *bool*                  | :heavy_check_mark:      | N/A                     |
| `message`               | *str*                   | :heavy_check_mark:      | N/A                     |
| `record_id`             | *str*                   | :heavy_check_mark:      | N/A                     |
| `connector`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `timestamp`             | *OptionalNullable[int]* | :heavy_minus_sign:      | N/A                     |