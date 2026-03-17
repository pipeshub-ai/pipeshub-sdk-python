# AgentCreateResponse

Agent object returned from create endpoint


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `key`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `description`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `start_message`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `system_prompt`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `instructions`                                             | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `models`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `tags`                                                     | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `is_active`                                                | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `created_by`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `updated_by`                                               | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        |
| `created_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `updated_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `is_deleted`                                               | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `toolsets`                                                 | List[[models.AgentToolset](../models/agenttoolset.md)]     | :heavy_minus_sign:                                         | N/A                                                        |
| `knowledge`                                                | List[[models.AgentKnowledge](../models/agentknowledge.md)] | :heavy_minus_sign:                                         | N/A                                                        |