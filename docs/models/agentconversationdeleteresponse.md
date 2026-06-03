# AgentConversationDeleteResponse

Envelope returned by `DELETE /agents/{agentKey}/conversations/{conversationId}`.
When the conversation does not exist, belongs to a different agent, or
was already deleted, the API still returns HTTP 200 with
`conversation: null`.



## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `message`                                                              | [models.MessageEnum](../models/messageenum.md)                         | :heavy_check_mark:                                                     | N/A                                                                    |
| `conversation`                                                         | [models.StoredAgentConversation](../models/storedagentconversation.md) | :heavy_check_mark:                                                     | Stored agent conversation document returned by non-list endpoints.<br/> |