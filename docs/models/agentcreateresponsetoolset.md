# AgentCreateResponseToolset


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | [models.AgentCreateToolsetName](../models/agentcreatetoolsetname.md)         | :heavy_check_mark:                                                           | Registered toolset name (lowercase) accepted by the create-agent gateway.    |
| `display_name`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | Human-readable toolset product label (for example `Jira` or `Slack`).        |
| `key`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `tools`                                                                      | List[[models.AgentCreateResponseTool](../models/agentcreateresponsetool.md)] | :heavy_check_mark:                                                           | N/A                                                                          |