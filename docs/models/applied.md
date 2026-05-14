# Applied

Echo of applied filters; unused slots are JSON `null`.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `q`                                                  | *Nullable[str]*                                      | :heavy_check_mark:                                   | N/A                                                  |
| `node_types`                                         | List[*str*]                                          | :heavy_check_mark:                                   | N/A                                                  |
| `record_types`                                       | List[*str*]                                          | :heavy_check_mark:                                   | N/A                                                  |
| `origins`                                            | List[*str*]                                          | :heavy_check_mark:                                   | N/A                                                  |
| `connector_ids`                                      | List[*str*]                                          | :heavy_check_mark:                                   | N/A                                                  |
| `indexing_status`                                    | List[*str*]                                          | :heavy_check_mark:                                   | N/A                                                  |
| `created_at`                                         | [Nullable[models.CreatedAt]](../models/createdat.md) | :heavy_check_mark:                                   | N/A                                                  |
| `updated_at`                                         | [Nullable[models.UpdatedAt]](../models/updatedat.md) | :heavy_check_mark:                                   | N/A                                                  |
| `size`                                               | [Nullable[models.Size]](../models/size.md)           | :heavy_check_mark:                                   | N/A                                                  |
| `sort_by`                                            | *str*                                                | :heavy_check_mark:                                   | Effective sort field after server normalisation.     |
| `sort_order`                                         | *str*                                                | :heavy_check_mark:                                   | Effective sort order after server normalisation.     |