# GetAIModelsProvidersResponse

AI model providers retrieved


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `status`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `message`                                                      | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `models`                                                       | [Optional[models.AIModelsConfig]](../models/aimodelsconfig.md) | :heavy_minus_sign:                                             | Must have at least one model type configured                   |