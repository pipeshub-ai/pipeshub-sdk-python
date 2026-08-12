# RegenerateAgentConversationMessageRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `agent_key`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Stable key identifying the agent that owns this conversation.        |
| `conversation_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | ID of the agent conversation containing the target message.          |
| `message_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | ID of the bot-response message to regenerate.                        |
| `body`                                                               | [models.AgentRegenerateRequest](../models/agentregeneraterequest.md) | :heavy_check_mark:                                                   | Regeneration payload requiring `chatMode: quick`.<br/>               |