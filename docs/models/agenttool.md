# AgentTool

A tool that agents can use to perform actions


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `key`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Unique tool identifier                                   | web-search                                               |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | Display name                                             | Web Search                                               |
| `description`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | What the tool does                                       |                                                          |
| `input_schema`                                           | [Optional[models.InputSchema]](../models/inputschema.md) | :heavy_minus_sign:                                       | JSON Schema for tool inputs                              |                                                          |
| `is_enabled`                                             | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Whether tool is currently available                      |                                                          |