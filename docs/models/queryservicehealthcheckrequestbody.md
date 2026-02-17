# QueryServiceHealthCheckRequestBody

Request payload


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `provider`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Model provider (openai, anthropic, ollama, etc.)                                                 |
| `configuration`                                                                                  | [models.QueryServiceHealthCheckConfiguration](../models/queryservicehealthcheckconfiguration.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `is_multimodal`                                                                                  | *Optional[bool]*                                                                                 | :heavy_minus_sign:                                                                               | Whether model supports vision/images                                                             |