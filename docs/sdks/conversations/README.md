# Conversations

## Overview

AI-powered conversational chat management with citations and follow-up questions

### Available Operations

* [create](#create) - Create a new AI conversation
* [create_with_streaming](#create_with_streaming) - Create conversation with streaming response
* [list](#list) - List all conversations
* [list_archived](#list_archived) - List archived conversations
* [get_by_id](#get_by_id) - Get conversation by ID
* [delete](#delete) - Delete conversation
* [add_message](#add_message) - Add message to conversation
* [add_message_stream](#add_message_stream) - Add message with streaming response
* [share](#share) - Share conversation with users
* [unshare](#unshare) - Revoke conversation access
* [update_title](#update_title) - Update conversation title
* [archive](#archive) - Archive conversation
* [unarchive](#unarchive) - Unarchive conversation
* [regenerate](#regenerate) - Regenerate AI response
* [submit_feedback](#submit_feedback) - Submit feedback on AI response

## create

Start a new conversation with PipesHub's AI assistant.<br><br>
<b>Overview:</b><br>
This endpoint creates a new conversation session and processes the initial query.
The AI searches your organization's knowledge bases for relevant information and
generates a response with citations to source documents.<br><br>
<b>How It Works:</b><br>
<ol>
<li>Your query is analyzed and converted to semantic embeddings</li>
<li>Relevant content is retrieved from indexed knowledge bases</li>
<li>The AI generates a response using the retrieved context</li>
<li>Citations link back to source documents for verification</li>
<li>Follow-up questions are suggested based on the conversation</li>
</ol>
<b>Filtering Options:</b><br>
<ul>
<li><b>recordIds:</b> Limit search to specific documents</li>
<li><b>filters.apps:</b> Search only specific connector apps</li>
<li><b>filters.kb:</b> Search only specific knowledge bases</li>
</ul>
<b>Model Selection:</b><br>
Use <code>modelKey</code> to select different AI models configured for your organization.
Each model may have different capabilities, speed, and accuracy trade-offs.


### Example Usage: filtered

<!-- UsageSnippet language="python" operationID="createConversation" method="post" path="/conversations/create" example="filtered" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.create(query="Summarize the Q4 sales report", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], filters={
        "kb": [
            "550e8400-e29b-41d4-a716-446655440000",
        ],
    }, model_key="gpt-4-turbo", model_name="GPT-4 Turbo", chat_mode="balanced")

    # Handle response
    print(res)

```
### Example Usage: simple

<!-- UsageSnippet language="python" operationID="createConversation" method="post" path="/conversations/create" example="simple" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.create(query="What is our company's vacation policy?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", chat_mode="balanced")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `query`                                                                                                                        | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | The user's question or prompt to start the conversation.<br/>Supports natural language queries of any complexity.<br/>         | What are the key findings from our Q4 financial report?                                                                        |
| `record_ids`                                                                                                                   | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Limit the AI's knowledge scope to specific records/documents.<br/>When provided, only these records will be searched for context.<br/> | [<br/>"507f1f77bcf86cd799439011",<br/>"507f1f77bcf86cd799439012"<br/>]                                                         |
| `departments`                                                                                                                  | List[*str*]                                                                                                                    | :heavy_minus_sign:                                                                                                             | Filter by department IDs to scope the search                                                                                   |                                                                                                                                |
| `filters`                                                                                                                      | [Optional[models.Filters]](../../models/filters.md)                                                                            | :heavy_minus_sign:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |
| `model_key`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Identifier for the AI model configuration to use.<br/>Available models depend on organization settings.<br/>                   | gpt-4-turbo                                                                                                                    |
| `model_name`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Display name of the AI model                                                                                                   | GPT-4 Turbo                                                                                                                    |
| `chat_mode`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Chat mode affecting response behavior.<br/>Different modes optimize for different use cases.<br/>                              | balanced                                                                                                                       |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_with_streaming

Start a new conversation with real-time streaming response using Server-Sent Events (SSE).<br><br>
<b>Overview:</b><br>
This endpoint works like <code>/conversations/create</code> but streams the AI response
in real-time as it's generated, providing a more interactive user experience.<br><br>
<b>SSE Event Types:</b><br>
<ul>
<li><code>connected</code> - Connection established, processing started</li>
<li><code>chunk</code> - Partial response text (stream these to show typing effect)</li>
<li><code>citation</code> - Citation reference found during generation</li>
<li><code>complete</code> - Final message with full response, citations, and follow-up questions</li>
<li><code>error</code> - Error occurred during processing</li>
</ul>
<b>Client Implementation:</b><br>
<code>
const eventSource = new EventSource('/conversations/stream');<br>
eventSource.onmessage = (event) => {<br>
&nbsp;&nbsp;const data = JSON.parse(event.data);<br>
&nbsp;&nbsp;// Handle different event types<br>
};
</code><br><br>
<b>Error Handling:</b><br>
If an error occurs mid-stream, an <code>error</code> event is sent and the stream closes.
The conversation is marked as FAILED with the error reason stored.


### Example Usage

<!-- UsageSnippet language="python" operationID="streamChat" method="post" path="/conversations/stream" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.create_with_streaming(query="What are the key findings from our Q4 financial report?", record_ids=[
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

## list

Retrieve all conversations for the authenticated user.<br><br>
<b>Overview:</b><br>
Returns a list of all conversations owned by or shared with the current user.
Conversations are returned with their messages, status, and metadata.<br><br>
<b>Filtering:</b><br>
<ul>
<li>Only non-archived conversations are returned by default</li>
<li>Use <code>/conversations/show/archives</code> for archived conversations</li>
</ul>
<b>Sorting:</b><br>
Conversations are sorted by last activity timestamp (most recent first).


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllConversations" method="get" path="/conversations" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Conversation]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_archived

Retrieve all archived conversations for the authenticated user.<br><br>
<b>Overview:</b><br>
Archived conversations are hidden from the main list but preserved for reference.
This endpoint returns only conversations where <code>isArchived: true</code>.<br><br>
<b>Unarchiving:</b><br>
Use <code>PATCH /conversations/{id}/unarchive</code> to restore a conversation
to the active list.


### Example Usage

<!-- UsageSnippet language="python" operationID="getArchivedConversations" method="get" path="/conversations/show/archives" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.list_archived()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Conversation]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_id

Retrieve a specific conversation with its full message history.<br><br>
<b>Overview:</b><br>
Returns the complete conversation including all messages, citations,
feedback, and metadata. Messages can be paginated for long conversations.<br><br>
<b>Message Pagination:</b><br>
For conversations with many messages, use pagination parameters:
<ul>
<li><code>page</code>: Page number (default: 1)</li>
<li><code>limit</code>: Messages per page (default: 10)</li>
<li><code>sortBy</code>: Sort field (default: createdAt)</li>
<li><code>sortOrder</code>: 'asc' or 'desc' (default: desc)</li>
</ul>
<b>Access Control:</b><br>
Users can access conversations they own or that have been shared with them.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConversationById" method="get" path="/conversations/{conversationId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.get_by_id(conversation_id="507f1f77bcf86cd799439011", page=1, limit=10, sort_by="createdAt", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                             | *str*                                                                                         | :heavy_check_mark:                                                                            | Unique conversation identifier                                                                | 507f1f77bcf86cd799439011                                                                      |
| `page`                                                                                        | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | Page number for message pagination                                                            |                                                                                               |
| `limit`                                                                                       | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | Number of messages per page                                                                   |                                                                                               |
| `sort_by`                                                                                     | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Field to sort messages by                                                                     |                                                                                               |
| `sort_order`                                                                                  | [Optional[models.GetConversationByIDSortOrder]](../../models/getconversationbyidsortorder.md) | :heavy_minus_sign:                                                                            | Sort direction                                                                                |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.GetConversationByIDResponse](../../models/getconversationbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete a conversation by its ID.<br><br>
<b>Overview:</b><br>
Performs a soft delete by setting <code>isDeleted: true</code>.
The conversation is removed from listings but preserved in the database.<br><br>
<b>Permissions:</b><br>
Only the conversation owner (initiator) can delete it.
Shared users cannot delete conversations.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConversationById" method="delete" path="/conversations/{conversationId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.delete(conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Unique conversation identifier                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteConversationByIDResponse](../../models/deleteconversationbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_message

Add a follow-up message to an existing conversation.<br><br>
<b>Overview:</b><br>
Continues an existing conversation by adding a new user query.
The AI maintains context from previous messages when generating the response.<br><br>
<b>Context Handling:</b><br>
<ul>
<li>Previous messages provide context for the new query</li>
<li>Citations from earlier messages may be referenced</li>
<li>The AI can refer back to previous topics discussed</li>
</ul>
<b>Model Override:</b><br>
You can specify a different model for this message using <code>modelKey</code>.
This allows switching models mid-conversation if needed.


### Example Usage

<!-- UsageSnippet language="python" operationID="addMessage" method="post" path="/conversations/{conversationId}/messages" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.add_message(conversation_id="<value>", query="Can you elaborate on the revenue trends?")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Unique conversation identifier                                      |                                                                     |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The follow-up question or message content                           | Can you elaborate on the revenue trends?                            |
| `filters`                                                           | [Optional[models.Filters]](../../models/filters.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `model_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Override the model for this specific message                        |                                                                     |
| `model_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Display name of the model                                           |                                                                     |
| `chat_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Chat mode for this message                                          |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_message_stream

Add a follow-up message to an existing conversation with real-time SSE streaming.<br><br>
<b>Overview:</b><br>
Same as <code>POST /conversations/{id}/messages</code> but with streaming response.
Provides real-time feedback as the AI generates its response.<br><br>
<b>SSE Events:</b><br>
See <code>/conversations/stream</code> for event type documentation.


### Example Usage

<!-- UsageSnippet language="python" operationID="addMessageStream" method="post" path="/conversations/{conversationId}/messages/stream" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.add_message_stream(conversation_id="<value>", query="Can you elaborate on the revenue trends?")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
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

## share

Share a conversation with other users in your organization.<br><br>
<b>Overview:</b><br>
Allows the conversation owner to grant access to other users.
Shared users can view the conversation and optionally add messages.<br><br>
<b>Access Levels:</b><br>
<ul>
<li><code>read</code> - Can view conversation and messages (default)</li>
<li><code>write</code> - Can view and add new messages</li>
</ul>
<b>Permissions:</b><br>
Only the conversation initiator (owner) can share. Users must belong
to the same organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="shareConversation" method="post" path="/conversations/{conversationId}/share" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.share(conversation_id="<value>", user_ids=[
        "507f1f77bcf86cd799439011",
    ], access_level="read")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              | Example                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                                                        | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | N/A                                                                                                                                      |                                                                                                                                          |
| `user_ids`                                                                                                                               | List[*str*]                                                                                                                              | :heavy_check_mark:                                                                                                                       | IDs of users to share with                                                                                                               | [<br/>"507f1f77bcf86cd799439011"<br/>]                                                                                                   |
| `access_level`                                                                                                                           | [Optional[models.ShareRequestAccessLevel]](../../models/sharerequestaccesslevel.md)                                                      | :heavy_minus_sign:                                                                                                                       | Permission level for shared users:<br/><ul><br/><li><code>read</code> - Can view only</li><br/><li><code>write</code> - Can add messages</li><br/></ul><br/> |                                                                                                                                          |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |                                                                                                                                          |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unshare

Remove sharing access from users.<br><br>
<b>Overview:</b><br>
Removes specified users from the conversation's sharedWith list.
Those users will no longer be able to access the conversation.<br><br>
<b>Permissions:</b><br>
Only the conversation owner can revoke access.


### Example Usage

<!-- UsageSnippet language="python" operationID="unshareConversation" method="post" path="/conversations/{conversationId}/unshare" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.unshare(conversation_id="<value>", user_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | User IDs to remove access from                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_title

Update the title of a conversation.<br><br>
<b>Overview:</b><br>
Conversation titles are auto-generated from the first query by default.
Use this endpoint to set a custom, more descriptive title.<br><br>
<b>Title Limits:</b><br>
<ul>
<li>Minimum: 1 character</li>
<li>Maximum: 200 characters</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConversationTitle" method="patch" path="/conversations/{conversationId}/title" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.update_title(conversation_id="<value>", title="Q4 Sales Analysis Discussion")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `title`                                                             | *str*                                                               | :heavy_check_mark:                                                  | New conversation title                                              | Q4 Sales Analysis Discussion                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive

Archive a conversation to hide it from the main list.<br><br>
<b>Overview:</b><br>
Archived conversations are preserved but hidden from the default conversation list.
Use archiving to clean up your workspace without permanently deleting conversations.<br><br>
<b>Retrieval:</b><br>
View archived conversations using <code>GET /conversations/show/archives</code>.


### Example Usage

<!-- UsageSnippet language="python" operationID="archiveConversation" method="patch" path="/conversations/{conversationId}/archive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.archive(conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive

Restore an archived conversation to the active list.<br><br>
<b>Overview:</b><br>
Removes the archived flag, making the conversation visible in the main list again.


### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveConversation" method="patch" path="/conversations/{conversationId}/unarchive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.unarchive(conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## regenerate

Regenerate the AI response for a specific message.<br><br>
<b>Overview:</b><br>
If you're not satisfied with an AI response, use this endpoint to generate
a new answer. The AI will re-process the original query and may produce
a different response.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Response was incomplete or unclear</li>
<li>Want to try a different AI model</li>
<li>New documents have been indexed since original response</li>
</ul>
<b>Model Override:</b><br>
Specify <code>modelKey</code> to use a different model for regeneration.


### Example Usage

<!-- UsageSnippet language="python" operationID="regenerateAnswer" method="post" path="/conversations/{conversationId}/message/{messageId}/regenerate" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.regenerate(conversation_id="<value>", message_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the message to regenerate response for                        |
| `filters`                                                           | [Optional[models.Filters]](../../models/filters.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Override model for regeneration                                     |
| `model_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_mode`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## submit_feedback

Provide feedback on an AI-generated response.<br><br>
<b>Overview:</b><br>
Feedback helps improve AI response quality over time. You can rate
various aspects of the response and provide detailed comments.<br><br>
<b>Feedback Options:</b><br>
<ul>
<li><b>isHelpful:</b> Overall thumbs up/down</li>
<li><b>ratings:</b> 1-5 scale for accuracy, relevance, completeness, clarity</li>
<li><b>categories:</b> Issue categories (incorrect info, too verbose, etc.)</li>
<li><b>comments:</b> Free-text positive/negative feedback and suggestions</li>
<li><b>citationFeedback:</b> Rate individual citations</li>
</ul>
<b>Restrictions:</b><br>
Feedback can only be submitted on <code>bot_response</code> messages,
not on user queries or system messages.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessageFeedback" method="post" path="/conversations/{conversationId}/message/{messageId}/feedback" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.submit_feedback(conversation_id="<value>", message_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `is_helpful`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Overall helpfulness rating                                          |
| `ratings`                                                           | [Optional[models.Ratings]](../../models/ratings.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `categories`                                                        | List[[models.Category](../../models/category.md)]                   | :heavy_minus_sign:                                                  | Categories of issues identified                                     |
| `comments`                                                          | [Optional[models.Comments]](../../models/comments.md)               | :heavy_minus_sign:                                                  | N/A                                                                 |
| `citation_feedback`                                                 | List[[models.CitationFeedback](../../models/citationfeedback.md)]   | :heavy_minus_sign:                                                  | Feedback on individual citations                                    |
| `follow_up_questions_helpful`                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Were the suggested follow-up questions helpful                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Conversation](../../models/conversation.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |