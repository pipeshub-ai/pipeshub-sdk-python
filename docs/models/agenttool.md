# AgentTool

A tool available within a toolset


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `key`                                            | *Optional[str]*                                  | :heavy_minus_sign:                               | Unique key of the tool                           |                                                  |
| `name`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | Short name of the tool                           | create_issue                                     |
| `full_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Fully qualified tool name (toolsetName.toolName) | github.create_issue                              |
| `toolset_name`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | Name of the parent toolset                       | github                                           |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Human-readable description of what the tool does | Create a new issue in a repository.              |