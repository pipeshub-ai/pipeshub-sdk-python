# CreateAgentResponse

Agent created


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `status`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  | success                                                              |
| `message`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  | Agent created successfully                                           |
| `agent`                                                              | [Optional[models.AgentListItem]](../models/agentlistitem.md)         | :heavy_minus_sign:                                                   | Agent summary returned in list endpoints (models as compact strings) |                                                                      |
| `warnings`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | Warnings from agent creation (e.g., failed toolset connections)      |                                                                      |