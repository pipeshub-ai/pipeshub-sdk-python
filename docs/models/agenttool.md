# AgentTool

A tool that agents can use to perform actions


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `app_name`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | Application/service the tool belongs to          | calendar                                         |
| `tool_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Name of the specific tool                        | create_calendar_event                            |
| `full_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Fully qualified tool name (app_name.tool_name)   | calendar.create_calendar_event                   |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | What the tool does                               |                                                  |
| `parameters`                                     | List[[models.Parameter](../models/parameter.md)] | :heavy_minus_sign:                               | Tool input parameters                            |                                                  |
| `returns`                                        | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Tool return value description                    |                                                  |
| `examples`                                       | List[[models.Example](../models/example.md)]     | :heavy_minus_sign:                               | Usage examples                                   |                                                  |
| `tags`                                           | List[*str*]                                      | :heavy_minus_sign:                               | Tags for categorization                          |                                                  |