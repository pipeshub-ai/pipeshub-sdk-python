# RestoredRecordSchema


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `record_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `name`                                                                    | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | The name it has now                                                       |
| `renamed_from`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Its name before restore, when another item next to it had taken that name |