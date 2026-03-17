# GetAgentConversationResponse

Agent conversation details


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `conversation`                                                                           | [Optional[models.AgentConversation]](../models/agentconversation.md)                     | :heavy_minus_sign:                                                                       | A conversation with a specific AI agent (full detail with messages).<br/>                |
| `filters`                                                                                | [Optional[models.GetAgentConversationFilters]](../models/getagentconversationfilters.md) | :heavy_minus_sign:                                                                       | Applied and available filters                                                            |
| `meta`                                                                                   | [Optional[models.GetAgentConversationMeta]](../models/getagentconversationmeta.md)       | :heavy_minus_sign:                                                                       | N/A                                                                                      |