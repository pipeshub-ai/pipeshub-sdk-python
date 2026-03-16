# CreateAgentResponse

Agent created


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `status`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      | success                                                                  |
| `message`                                                                | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      | Agent created successfully                                               |
| `agent`                                                                  | [Optional[models.AgentCreateResponse]](../models/agentcreateresponse.md) | :heavy_minus_sign:                                                       | Agent object returned from create endpoint                               |                                                                          |
| `warnings`                                                               | List[*str*]                                                              | :heavy_minus_sign:                                                       | Warnings from agent creation (e.g., failed toolset connections)          |                                                                          |