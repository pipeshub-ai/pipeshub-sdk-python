# GetAgentConversationResponse

Agent conversation details


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `conversation`                                                       | [Optional[models.AgentConversation]](../models/agentconversation.md) | :heavy_minus_sign:                                                   | A conversation with a specific AI agent.<br/>                        |
| `filters`                                                            | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | Applied and available filters                                        |
| `meta`                                                               | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | Request metadata                                                     |