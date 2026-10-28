# AgentCreateModelEntry


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `model_key`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Surrounding whitespace is trimmed; a blank key is refused with `400`. |
| `model_name`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `provider`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `is_reasoning`                                                        | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |