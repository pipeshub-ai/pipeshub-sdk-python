# UpdateAgentRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `agent_key`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | Unique agent identifier                                                | customer-support-agent                                                 |
| `body`                                                                 | [Optional[models.AgentUpdateRequest]](../models/agentupdaterequest.md) | :heavy_minus_sign:                                                     | Partial agent configuration fields to update                           |                                                                        |