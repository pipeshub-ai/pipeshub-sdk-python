# Filter


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `key`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter field key                                                     |
| `label`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Display label                                                        |
| `type`                                                               | [Optional[models.FilterOptionsType]](../models/filteroptionstype.md) | :heavy_minus_sign:                                                   | Filter input type                                                    |
| `options`                                                            | List[[models.Option](../models/option.md)]                           | :heavy_minus_sign:                                                   | N/A                                                                  |
| `dynamic`                                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether options are loaded dynamically                               |