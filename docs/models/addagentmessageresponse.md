# AddAgentMessageResponse

Message added


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `conversation`                                                       | [Optional[models.AgentConversation]](../models/agentconversation.md) | :heavy_minus_sign:                                                   | A conversation with a specific AI agent.<br/>                        |
| `records_used`                                                       | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Number of knowledge base records used                                |
| `meta`                                                               | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | Request metadata                                                     |