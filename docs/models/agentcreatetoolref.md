# AgentCreateToolRef


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | Surrounding whitespace is trimmed; a blank name is refused with `400`.  |
| `full_name`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Surrounding whitespace is trimmed; a blank value is refused with `400`. |
| `description`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |