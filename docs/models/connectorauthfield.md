# ConnectorAuthField

One field of an auth form. Send its value in `config.auth` under `name`.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `name`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `display_name`                                                | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `placeholder`                                                 | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `description`                                                 | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `field_type`                                                  | *Optional[str]*                                               | :heavy_minus_sign:                                            | Input type, for example TEXT, PASSWORD, URL, SELECT, CHECKBOX |
| `required`                                                    | *Optional[bool]*                                              | :heavy_minus_sign:                                            | N/A                                                           |
| `usage`                                                       | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `default_value`                                               | *Optional[Any]*                                               | :heavy_minus_sign:                                            | Default value; its type follows `fieldType`                   |
| `validation`                                                  | Dict[str, *Any*]                                              | :heavy_minus_sign:                                            | N/A                                                           |
| `is_secret`                                                   | *Optional[bool]*                                              | :heavy_minus_sign:                                            | Stored values come back masked                                |
| `options`                                                     | List[*Any*]                                                   | :heavy_minus_sign:                                            | N/A                                                           |