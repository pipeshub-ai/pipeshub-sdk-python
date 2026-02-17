# UpdateAgentRequestBody

Request body for Update agent


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `name`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `description`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `system_prompt`                                                            | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `tools`                                                                    | List[*str*]                                                                | :heavy_minus_sign:                                                         | N/A                                                                        |
| `knowledge_bases`                                                          | List[*str*]                                                                | :heavy_minus_sign:                                                         | N/A                                                                        |
| `llm_config`                                                               | [Optional[models.UpdateAgentLlmConfig]](../models/updateagentllmconfig.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `is_public`                                                                | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |