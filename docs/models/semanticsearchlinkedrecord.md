# SemanticSearchLinkedRecord


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `relation`                                            | [models.Relation](../models/relation.md)              | :heavy_check_mark:                                    | N/A                                                   |
| `record_id`                                           | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `record_name`                                         | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `record_type`                                         | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `connector`                                           | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `status`                                              | *Optional[str]*                                       | :heavy_minus_sign:                                    | The linked record's `statusSummary`, when it has one. |