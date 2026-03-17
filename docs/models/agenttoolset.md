# AgentToolset

A toolset attached to an agent providing external tool capabilities


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `key`                                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | Unique key of the toolset                                   |                                                             |
| `name`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | Toolset identifier name                                     | github                                                      |
| `display_name`                                              | *Optional[str]*                                             | :heavy_minus_sign:                                          | Human-readable display name                                 | GitHub Integration                                          |
| `type`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | Type of toolset                                             | app                                                         |
| `instance_id`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | Instance ID of the connected app                            |                                                             |
| `selected_tools`                                            | List[*str*]                                                 | :heavy_minus_sign:                                          | Subset of tools selected by the user (null means all tools) |                                                             |
| `tools`                                                     | List[[models.AgentTool](../models/agenttool.md)]            | :heavy_minus_sign:                                          | List of tools available in this toolset                     |                                                             |