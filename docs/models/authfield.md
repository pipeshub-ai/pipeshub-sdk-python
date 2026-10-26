# AuthField


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `name`                                       | *str*                                        | :heavy_check_mark:                           | N/A                                          | clientId                                     |
| `display_name`                               | *str*                                        | :heavy_check_mark:                           | N/A                                          |                                              |
| `placeholder`                                | *str*                                        | :heavy_check_mark:                           | N/A                                          |                                              |
| `description`                                | *str*                                        | :heavy_check_mark:                           | N/A                                          |                                              |
| `field_type`                                 | [models.FieldType](../models/fieldtype.md)   | :heavy_check_mark:                           | N/A                                          |                                              |
| `required`                                   | *bool*                                       | :heavy_check_mark:                           | N/A                                          |                                              |
| `usage`                                      | [models.Usage](../models/usage.md)           | :heavy_check_mark:                           | N/A                                          |                                              |
| `default_value`                              | *str*                                        | :heavy_check_mark:                           | N/A                                          |                                              |
| `validation`                                 | [models.Validation](../models/validation.md) | :heavy_check_mark:                           | N/A                                          |                                              |
| `is_secret`                                  | *bool*                                       | :heavy_check_mark:                           | N/A                                          |                                              |
| `options`                                    | List[*str*]                                  | :heavy_minus_sign:                           | Present on SELECT fields                     |                                              |