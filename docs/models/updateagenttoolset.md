# UpdateAgentToolset


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `name`                                                       | *str*                                                        | :heavy_check_mark:                                           | Toolset identifier name (lowercased)                         |
| `display_name`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | Human-readable display name                                  |
| `type`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | Type of toolset                                              |
| `instance_id`                                                | *Optional[str]*                                              | :heavy_minus_sign:                                           | Admin-created instance UUID                                  |
| `instance_name`                                              | *Optional[str]*                                              | :heavy_minus_sign:                                           | Instance name                                                |
| `tools`                                                      | List[[models.UpdateAgentTool](../models/updateagenttool.md)] | :heavy_minus_sign:                                           | N/A                                                          |