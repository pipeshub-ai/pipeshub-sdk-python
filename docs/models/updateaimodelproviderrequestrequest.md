# UpdateAIModelProviderRequestRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `model_type`                                                                     | [models.ModelType](../models/modeltype.md)                                       | :heavy_check_mark:                                                               | Type of AI model                                                                 |
| `model_key`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | Unique model key (UUID)                                                          |
| `body`                                                                           | [models.UpdateAIModelProviderRequest](../models/updateaimodelproviderrequest.md) | :heavy_check_mark:                                                               | Request payload                                                                  |