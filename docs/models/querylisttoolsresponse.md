# QueryListToolsResponse


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `name`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Tool name identifier                                   |
| `description`                                          | *Optional[str]*                                        | :heavy_minus_sign:                                     | Human-readable tool description                        |
| `parameters`                                           | [Optional[models.Parameters]](../models/parameters.md) | :heavy_minus_sign:                                     | Tool parameter definitions                             |
| `tags`                                                 | List[*str*]                                            | :heavy_minus_sign:                                     | Tool categorization tags                               |