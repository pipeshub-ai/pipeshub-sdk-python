# AgentAddMessageResponse

Envelope returned by
`POST /agents/{agentKey}/conversations/{conversationId}/messages`:
the updated agent conversation, the number of citation records used
to ground the answer for this turn, and request metadata.



## Fields

| Field                                                                                                                             | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `conversation`                                                                                                                    | [models.AgentConversation](../models/agentconversation.md)                                                                        | :heavy_check_mark:                                                                                                                | A conversation with a specific AI agent. Similar to regular conversations<br/>but tied to an agent's configuration and capabilities.<br/> |
| `records_used`                                                                                                                    | *int*                                                                                                                             | :heavy_check_mark:                                                                                                                | Number of citation records used to ground the answer generated for this turn.                                                     |
| `meta`                                                                                                                            | [models.AgentAddMessageResponseMeta](../models/agentaddmessageresponsemeta.md)                                                    | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |