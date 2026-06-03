# GetAgentResponse

Success envelope returned by `GET /agents/{agentKey}`.

The Node gateway forwards the backend response as an envelope with a
top-level status/message and the detailed agent projection nested under
`agent`.



## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `status`                                                                                              | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   | success                                                                                               |
| `message`                                                                                             | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   | Agent retrieved successfully                                                                          |
| `agent`                                                                                               | [models.Agent](../models/agent.md)                                                                    | :heavy_check_mark:                                                                                    | Detailed agent projection returned by agent detail-style endpoints such<br/>as `GET /agents/{agentKey}`.<br/> |                                                                                                       |