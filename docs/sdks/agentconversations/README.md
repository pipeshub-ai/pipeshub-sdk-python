# AgentConversations

## Overview

Conversations with custom AI agents including streaming and feedback

### Available Operations

* [list_agent_conversations](#list_agent_conversations) - List agent conversations
* [create_agent_conversation](#create_agent_conversation) - Create agent conversation
* [stream_agent_conversation](#stream_agent_conversation) - Create agent conversation with streaming
* [get_agent_conversation](#get_agent_conversation) - Get agent conversation
* [delete_agent_conversation](#delete_agent_conversation) - Delete agent conversation
* [add_agent_message](#add_agent_message) - Add message to agent conversation
* [stream_agent_message](#stream_agent_message) - Add message with streaming
* [regenerate_agent_answer](#regenerate_agent_answer) - Regenerate agent response

## list_agent_conversations

Get all conversations with a specific agent.<br><br>
<b>Overview:</b><br>
Returns conversations the user has had with this particular agent.
Agent conversations maintain the agent's context and capabilities.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgentConversations" method="get" path="/agents/{agentKey}/conversations" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.list_agent_conversations(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Agent identifier                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAgentConversationsResponse](../../models/listagentconversationsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_agent_conversation

Start a new conversation with an agent.<br><br>
<b>Overview:</b><br>
Creates a conversation using the agent's configuration including
its system prompt, tools, and knowledge base access.


### Example Usage

<!-- UsageSnippet language="python" operationID="createAgentConversation" method="post" path="/agents/{agentKey}/conversations" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.create_agent_conversation(agent_key="<value>", query="What are the key findings from our Q4 financial report?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", chat_mode="balanced")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `agent_key`                                                                                                                    | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |
| `query`                                                                                                                        | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | The user's question or prompt to start the conversation.<br/>Supports natural language queries of any complexity.<br/>         | What are the key findings from our Q4 financial report?                                                                        |
| `record_ids`                                                                                                                   | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Limit the AI's knowledge scope to specific records/documents.<br/>When provided, only these records will be searched for context.<br/> | [<br/>"507f1f77bcf86cd799439011",<br/>"507f1f77bcf86cd799439012"<br/>]                                                         |
| `departments`                                                                                                                  | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Filter by department IDs to scope the search                                                                                   |                                                                                                                                |
| `filters`                                                                                                                      | [Optional[models.Filters]](../../models/filters.md)                                                                            | :heavy_minus_sign:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |
| `model_key`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Identifier for the AI model configuration to use.<br/>Available models depend on organization settings.<br/>                   | gpt-4-turbo                                                                                                                    |
| `model_name`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Display name of the AI model                                                                                                   | GPT-4 Turbo                                                                                                                    |
| `chat_mode`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Chat mode affecting response behavior.<br/>Different modes optimize for different use cases.<br/>                              | balanced                                                                                                                       |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.AgentConversation](../../models/agentconversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream_agent_conversation

Start a new agent conversation with SSE streaming response.<br><br>
<b>Overview:</b><br>
Same as POST /agents/{agentKey}/conversations but with real-time streaming.


### Example Usage

<!-- UsageSnippet language="python" operationID="streamAgentConversation" method="post" path="/agents/{agentKey}/conversations/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.stream_agent_conversation(agent_key="<value>", query="What are the key findings from our Q4 financial report?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", chat_mode="balanced")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `agent_key`                                                                                                                    | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |
| `query`                                                                                                                        | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | The user's question or prompt to start the conversation.<br/>Supports natural language queries of any complexity.<br/>         | What are the key findings from our Q4 financial report?                                                                        |
| `record_ids`                                                                                                                   | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Limit the AI's knowledge scope to specific records/documents.<br/>When provided, only these records will be searched for context.<br/> | [<br/>"507f1f77bcf86cd799439011",<br/>"507f1f77bcf86cd799439012"<br/>]                                                         |
| `departments`                                                                                                                  | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Filter by department IDs to scope the search                                                                                   |                                                                                                                                |
| `filters`                                                                                                                      | [Optional[models.Filters]](../../models/filters.md)                                                                            | :heavy_minus_sign:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |
| `model_key`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Identifier for the AI model configuration to use.<br/>Available models depend on organization settings.<br/>                   | gpt-4-turbo                                                                                                                    |
| `model_name`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Display name of the AI model                                                                                                   | GPT-4 Turbo                                                                                                                    |
| `chat_mode`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Chat mode affecting response behavior.<br/>Different modes optimize for different use cases.<br/>                              | balanced                                                                                                                       |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[Union[eventstreaming.EventStream[models.SSEEvent], eventstreaming.EventStreamAsync[models.SSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_agent_conversation

Retrieve a specific agent conversation by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentConversation" method="get" path="/agents/{agentKey}/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.get_agent_conversation(agent_key="<value>", conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentConversation](../../models/agentconversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_agent_conversation

Delete a conversation with an agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgentConversation" method="delete" path="/agents/{agentKey}/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.agent_conversations.delete_agent_conversation(agent_key="<value>", conversation_id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_agent_message

Add a follow-up message to an agent conversation.

### Example Usage

<!-- UsageSnippet language="python" operationID="addAgentMessage" method="post" path="/agents/{agentKey}/conversations/{conversationId}/messages" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.add_agent_message(agent_key="<value>", conversation_id="<value>", query="Can you elaborate on the revenue trends?")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The follow-up question or message content                           | Can you elaborate on the revenue trends?                            |
| `filters`                                                           | [Optional[models.Filters]](../../models/filters.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `model_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Override the model for this specific message                        |                                                                     |
| `model_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Display name of the model                                           |                                                                     |
| `chat_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Chat mode for this message                                          |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AgentConversation](../../models/agentconversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream_agent_message

Add a message to agent conversation with SSE streaming response.

### Example Usage

<!-- UsageSnippet language="python" operationID="streamAgentMessage" method="post" path="/agents/{agentKey}/conversations/{conversationId}/messages/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.stream_agent_message(agent_key="<value>", conversation_id="<value>", query="Can you elaborate on the revenue trends?")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The follow-up question or message content                           | Can you elaborate on the revenue trends?                            |
| `filters`                                                           | [Optional[models.Filters]](../../models/filters.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `model_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Override the model for this specific message                        |                                                                     |
| `model_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Display name of the model                                           |                                                                     |
| `chat_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Chat mode for this message                                          |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Union[eventstreaming.EventStream[models.SSEEvent], eventstreaming.EventStreamAsync[models.SSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## regenerate_agent_answer

Regenerate the agent's response for a specific message.<br><br>
<b>Overview:</b><br>
Similar to conversation regeneration but uses the agent's configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="regenerateAgentAnswer" method="post" path="/agents/{agentKey}/conversations/{conversationId}/message/{messageId}/regenerate" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_conversations.regenerate_agent_answer(agent_key="<value>", conversation_id="<value>", message_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filters`                                                           | [Optional[models.Filters]](../../models/filters.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentConversation](../../models/agentconversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |