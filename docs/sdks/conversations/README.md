# Conversations

## Overview

### Available Operations

* [stream_chat](#stream_chat) - Create conversation with streaming response
* [get_all_conversations](#get_all_conversations) - List all conversations
* [get_archived_conversations](#get_archived_conversations) - List archived conversations
* [search_archived_conversations](#search_archived_conversations) - Search archived conversations
* [get_conversation_by_id](#get_conversation_by_id) - Get conversation by ID
* [delete_conversation_by_id](#delete_conversation_by_id) - Delete conversation
* [add_message_stream](#add_message_stream) - Add message to a conversation with streaming response
* [update_conversation_title](#update_conversation_title) - Update conversation title
* [archive_conversation](#archive_conversation) - Archive conversation
* [unarchive_conversation](#unarchive_conversation) - Unarchive conversation
* [regenerate_answer](#regenerate_answer) - Regenerate AI response
* [update_message_feedback](#update_message_feedback) - Submit feedback on AI response

## stream_chat

Start a new conversation and stream the AI response over Server-Sent
Events (SSE). Behaves like `POST /conversations` but emits tokens,
tool activity, and status updates incrementally instead of returning
a single JSON response at the end.

**Lifecycle**

1. The server validates `query`, persists an in-progress
   conversation, then opens the SSE stream with HTTP `200`.
2. A `connected` event is emitted immediately with the new
   `conversationId` so the client can link the stream (sidebar,
   parallel tabs, deep links) without an extra request.
3. AI-backend events stream through (token chunks, tool calls,
   status, etc.).
4. On success a single `complete` event is emitted carrying the
   full persisted conversation.
5. On failure an `error` event is emitted and the conversation is
   marked FAILED before the stream closes.

**Event vocabulary**

Three events have stable, server-defined `data` shapes:

- `connected` — `{ "message": string, "conversationId": string,
  "title": string }`
- `complete` — `{ "conversation": Conversation,
  "meta": { "requestId": string, "timestamp": string,
  "duration": number } }`
- `error` — `{ "error": string, "details"?: string }`

The forwarded events are `status`, `answer_chunk`, `tool_calls`,
`restreaming`, `metadata`, and `tool_execution_complete`. Their
payloads come from the Python query service and may evolve. Note
that raw `tool_call` / `tool_success` / `tool_error` / `tool_result`
events emitted by the LLM tool runtime are rewrapped as `status` by
the upstream wrapper before they reach this route, so clients on
`/conversations/stream` never see those names directly. Clients
should ignore unknown event names rather than treating them as
errors.

**Agent mode**

When `chatMode` selects an agent mode (for example `agent:auto`),
the optional `tools` list restricts which tools the agent may
invoke for this turn. Outside agent modes the `tools` field is
ignored.


### Example Usage

<!-- UsageSnippet language="python" operationID="streamChat" method="post" path="/conversations/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.stream_chat(query="What are the key findings from our Q4 financial report?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", model_friendly_name="GPT-4 Turbo", chat_mode="balanced", timezone="America/New_York", current_time=parse_datetime("2026-04-12T16:00:00+05:30"), tools=[
        "jira.create_issue",
        "confluence.search_content",
    ])

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The user's question or prompt to start the conversation.<br/>Supports natural language queries of any complexity.<br/>                                                                                                                                                                                                                                                                                                                                                            | What are the key findings from our Q4 financial report?                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `record_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Limit the AI's knowledge scope to specific records/documents.<br/>When provided, only these records will be searched for context.<br/>                                                                                                                                                                                                                                                                                                                                            | [<br/>"507f1f77bcf86cd799439011",<br/>"507f1f77bcf86cd799439012"<br/>]                                                                                                                                                                                                                                                                                                                                                                                                            |
| `departments`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Filter by department IDs to scope the search                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | App connector instance ids and knowledge-base / record-group ids that narrow retrieval<br/>for a turn. For **org assistant** chat streams, send explicit `apps` / `kb` lists.<br/>For **agent** chat streams, send explicit id lists, or **omit** `filters` (and `tools`)<br/>to let the service use the agent’s stored knowledge and tool configuration. Sending<br/>`{ "apps": [], "kb": [] }` on an agent stream means **no** knowledge sources for that<br/>turn (it is not “full org default”).<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `applied_filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AppliedFilters]](../../models/appliedfilters.md)                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Rich filter state selected by the user, used for display and persistence only.<br/>This mirrors the active selection shown in the UI and is distinct from the<br/>machine-readable `filters` field used for retrieval scoping.<br/>                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Identifier for the AI model configuration to use.<br/>Available models depend on organization settings.<br/>                                                                                                                                                                                                                                                                                                                                                                      | gpt-4-turbo                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `model_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Display name of the AI model                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GPT-4 Turbo                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `model_friendly_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Friendly display name of the selected model                                                                                                                                                                                                                                                                                                                                                                                                                                       | GPT-4 Turbo                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `chat_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chat mode affecting response behavior.<br/>Different modes optimize for different use cases.<br/>                                                                                                                                                                                                                                                                                                                                                                                 | balanced                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `timezone`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | IANA timezone identifier from the client (top-level field).<br/>Used to provide time-aware context to the AI.<br/>                                                                                                                                                                                                                                                                                                                                                                | America/New_York                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `current_time`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ISO 8601 / RFC 3339 datetime from the client (top-level field; UTC `Z` or numeric offset).<br/>                                                                                                                                                                                                                                                                                                                                                                                   | 2026-04-12 16:00:00 +0530 +0530                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tools`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional list of tool identifiers (fully-qualified action names such as<br/>"jira.create_issue") that the AI agent is permitted to invoke for this<br/>request. When omitted the agent may use any configured tool. Applicable<br/>only when chatMode is an agent mode (e.g. "agent:auto").<br/>                                                                                                                                                                                  | [<br/>"jira.create_issue",<br/>"confluence.search_content"<br/>]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[Union[eventstreaming.EventStream[models.AssistantStreamSSEEvent], eventstreaming.EventStreamAsync[models.AssistantStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_all_conversations

Retrieve paginated conversations for the authenticated user.

**Overview:**

Use the optional `source` query parameter to choose which list to return:
`owned` — only conversations you own (`userId` matches the current user).
`shared` — conversations where you have recipient access
(`isShared` and your user appears in `sharedWith`), without the owner-only branch.
Defaults to `owned` when omitted. Each call returns one list; call twice if you need both.

**Filtering:**

- Only non-archived conversations are returned by default
- Use `/conversations/show/archives` for archived conversations

**Sorting:**

Conversations are sorted by last activity timestamp (most recent first) by default.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllConversations" method="get" path="/conversations" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.get_all_conversations(source="owned")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`                                                                                                                                          | [Optional[models.QueryParamSource]](../../models/queryparamsource.md)                                                                             | :heavy_minus_sign:                                                                                                                                | `owned` — owner list (`userId` filter only).<br/>`shared` — explicit share grant list (`isShared` + `sharedWith`).<br/>Defaults to `owned` when omitted.<br/> |
| `page`                                                                                                                                            | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Page number (1-based). Defaults to 1.                                                                                                             |
| `limit`                                                                                                                                           | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Page size. Defaults to 20; capped by the server (max 100).                                                                                        |
| `sort_by`                                                                                                                                         | [Optional[models.GetAllConversationsSortByEnum]](../../models/getallconversationssortbyenum.md)                                                   | :heavy_minus_sign:                                                                                                                                | Sort field. Invalid values fall back to `lastActivityAt`.                                                                                         |
| `sort_order`                                                                                                                                      | [Optional[models.GetAllConversationsSortOrderEnum]](../../models/getallconversationssortorderenum.md)                                             | :heavy_minus_sign:                                                                                                                                | Sort direction. Defaults to `desc` unless set to `asc`.                                                                                           |
| `conversation_id`                                                                                                                                 | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | When set, restricts results to that conversation ID (if visible under the chosen `source`).                                                       |
| `search`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Case-insensitive match on title and message content (max 1000 characters).                                                                        |
| `start_date`                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                              | :heavy_minus_sign:                                                                                                                                | Filter by `createdAt` ≥ this ISO date.                                                                                                            |
| `end_date`                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                              | :heavy_minus_sign:                                                                                                                                | Filter by `createdAt` ≤ this ISO date.                                                                                                            |
| `shared`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | When set, filters by `isShared`. Accepts case-insensitive<br/>`true`/`false`, or `1`/`0`.<br/>                                                    |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.GetAllConversationsResponse](../../models/getallconversationsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_archived_conversations

Retrieve all archived conversations for the authenticated user.

**Overview:**

Archived conversations are hidden from the main list but preserved for reference.
This endpoint returns only conversations where `isArchived: true` and `archivedBy`
is set. Results include conversations the caller owns and those shared with them.

**Filtering and sorting:**

Results can be narrowed using `search`, `shared`, `startDate`, `endDate`, and
`conversationId`. Sorting is controlled by `sortBy` and `sortOrder`. Pagination
is controlled by `page` and `limit`.

**Unarchiving:**

Use `PATCH /conversations/{conversationId}/unarchive` to restore a conversation
to the active list.


### Example Usage

<!-- UsageSnippet language="python" operationID="getArchivedConversations" method="get" path="/conversations/show/archives" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.get_archived_conversations(page=1, limit=20, sort_by="lastActivityAt", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Page number (1-indexed)                                                                                         |
| `limit`                                                                                                         | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Items per page                                                                                                  |
| `sort_by`                                                                                                       | [Optional[models.GetArchivedConversationsSortByEnum]](../../models/getarchivedconversationssortbyenum.md)       | :heavy_minus_sign:                                                                                              | Field to sort by                                                                                                |
| `sort_order`                                                                                                    | [Optional[models.GetArchivedConversationsSortOrderEnum]](../../models/getarchivedconversationssortorderenum.md) | :heavy_minus_sign:                                                                                              | Sort direction                                                                                                  |
| `search`                                                                                                        | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Case-insensitive substring match against title and message content (max 1000 chars)                             |
| `shared`                                                                                                        | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Filter by shared status                                                                                         |
| `start_date`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                            | :heavy_minus_sign:                                                                                              | Include conversations created on or after this timestamp                                                        |
| `end_date`                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                            | :heavy_minus_sign:                                                                                              | Include conversations created on or before this timestamp                                                       |
| `conversation_id`                                                                                               | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Restrict results to a single conversation by identifier                                                         |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.GetArchivedConversationsResponse](../../models/getarchivedconversationsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## search_archived_conversations

Search across all archived conversations (assistant and agent) for the authenticated user.

**Overview:**

Performs a case-insensitive substring match against conversation titles and message content
across both assistant (`Conversation`) and agent (`AgentConversation`) archived collections.
Results are merged server-side and sorted by `lastActivityAt` descending.

**Search parameter:**

The `search` query parameter is required, must be a non-empty string, and is capped at
1000 characters. Requests that omit it or exceed the cap return `400`.

**Pagination:**

Results are paginated using `page` and `limit`. The response includes a `pagination`
block with total counts and a `summary` block that breaks matches down by source.

**Item shape:**

Each item is a conversation list entry (no `messages` payload — that field is omitted
for performance) tagged with `source`, plus computed `isOwner`, `accessLevel`,
`archivedAt`, and `archivedBy`. `agentKey` is present only when `source` is `agent`.


### Example Usage

<!-- UsageSnippet language="python" operationID="searchArchivedConversations" method="get" path="/conversations/show/archives/search" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.search_archived_conversations(search="<value>", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `search`                                                                              | *str*                                                                                 | :heavy_check_mark:                                                                    | Search term to match against conversation titles and message content (max 1000 chars) |
| `page`                                                                                | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Page number (1-indexed)                                                               |
| `limit`                                                                               | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Items per page                                                                        |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SearchArchivedConversationsResponse](../../models/searcharchivedconversationsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_conversation_by_id

Retrieve a specific conversation with its full message history.

**Overview:**

Returns the complete conversation including all messages, citations,
feedback, and metadata. Messages can be paginated for long conversations.

**Message Pagination:**

For conversations with many messages, use pagination parameters:

- `page`: Page number (default: 1)
- `limit`: Messages per page (default: 10)
- `sortBy`: Sort field (default: createdAt)
- `sortOrder`: 'asc' or 'desc' (default: desc)

**Access Control:**

Users can access conversations they own or that have been shared with them.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConversationById" method="get" path="/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.get_conversation_by_id(conversation_id="507f1f77bcf86cd799439011", page=1, limit=20, sort_by="createdAt", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                     | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Unique conversation identifier                                                                        | 507f1f77bcf86cd799439011                                                                              |
| `page`                                                                                                | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Page number for message pagination                                                                    |                                                                                                       |
| `limit`                                                                                               | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Number of messages per page                                                                           |                                                                                                       |
| `sort_by`                                                                                             | [Optional[models.GetConversationByIDSortByEnum]](../../models/getconversationbyidsortbyenum.md)       | :heavy_minus_sign:                                                                                    | Field to sort messages by                                                                             |                                                                                                       |
| `sort_order`                                                                                          | [Optional[models.GetConversationByIDSortOrderEnum]](../../models/getconversationbyidsortorderenum.md) | :heavy_minus_sign:                                                                                    | Sort direction                                                                                        |                                                                                                       |
| `search`                                                                                              | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Case-insensitive search across conversation title and message content                                 |                                                                                                       |
| `start_date`                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Filter messages created on or after this date (ISO 8601)                                              |                                                                                                       |
| `end_date`                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                  | :heavy_minus_sign:                                                                                    | Filter messages created on or before this date (ISO 8601)                                             |                                                                                                       |
| `shared`                                                                                              | *Optional[bool]*                                                                                      | :heavy_minus_sign:                                                                                    | Filter by shared status of the conversation                                                           |                                                                                                       |
| `message_type`                                                                                        | [Optional[models.QueryParamMessageType]](../../models/queryparammessagetype.md)                       | :heavy_minus_sign:                                                                                    | Filter messages by type                                                                               |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.GetConversationByIDResponse](../../models/getconversationbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_conversation_by_id

Delete a conversation by its ID.

**Overview:**

Performs a soft delete by setting `isDeleted: true`. The conversation is
removed from listings but preserved in the database. All citations
referenced by messages in the conversation are also soft-deleted.

**Permissions:**

The conversation initiator can always delete. Users the conversation has
been shared with may delete it only when their `sharedWith.accessLevel`
is `write`.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConversationById" method="delete" path="/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.delete_conversation_by_id(conversation_id="<value>")

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

## add_message_stream

Add a follow-up message to an existing conversation and stream the
assistant's response over Server-Sent Events.

Functionally equivalent to `POST /conversations/{conversationId}/messages`
but the response is delivered as an SSE stream so clients can render
the answer incrementally.

The wire vocabulary is described by `AssistantMessageStreamSSEEvent`.
It is the same event set as `/conversations/stream`; only the
`connected` and `complete` payloads differ because the conversation
already exists when this route is called.


### Example Usage

<!-- UsageSnippet language="python" operationID="addMessageStream" method="post" path="/conversations/{conversationId}/messages/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.add_message_stream(conversation_id="<value>", query="Can you elaborate on the revenue trends?", timezone="America/New_York", current_time=parse_datetime("2026-04-12T16:00:00+05:30"), tools=[
        "jira.create_issue",
        "confluence.search_content",
    ])

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Identifier of the conversation to append the message to. The<br/>conversation must belong to the caller and must not be deleted.<br/>                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The follow-up question or message content                                                                                                                                                                                                                                                                                                                                                                                                                                         | Can you elaborate on the revenue trends?                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | App connector instance ids and knowledge-base / record-group ids that narrow retrieval<br/>for a turn. For **org assistant** chat streams, send explicit `apps` / `kb` lists.<br/>For **agent** chat streams, send explicit id lists, or **omit** `filters` (and `tools`)<br/>to let the service use the agent’s stored knowledge and tool configuration. Sending<br/>`{ "apps": [], "kb": [] }` on an agent stream means **no** knowledge sources for that<br/>turn (it is not “full org default”).<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `applied_filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AppliedFilters]](../../models/appliedfilters.md)                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Rich filter state selected by the user, used for display and persistence only.<br/>This mirrors the active selection shown in the UI and is distinct from the<br/>machine-readable `filters` field used for retrieval scoping.<br/>                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Override the model for this specific message                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Display name of the model                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_friendly_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Friendly display name of the model                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `chat_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chat mode for this message                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `timezone`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | IANA timezone identifier from the client (top-level field).<br/>Used to provide time-aware context to the AI.<br/>                                                                                                                                                                                                                                                                                                                                                                | America/New_York                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `current_time`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ISO 8601 / RFC 3339 datetime from the client (top-level field; UTC `Z` or numeric offset).<br/>                                                                                                                                                                                                                                                                                                                                                                                   | 2026-04-12 16:00:00 +0530 +0530                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tools`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional list of tool identifiers the agent may invoke for this<br/>follow-up message. Semantics are identical to the create-conversation<br/>tools field.<br/>                                                                                                                                                                                                                                                                                                                   | [<br/>"jira.create_issue",<br/>"confluence.search_content"<br/>]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[Union[eventstreaming.EventStream[models.AssistantMessageStreamSSEEvent], eventstreaming.EventStreamAsync[models.AssistantMessageStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_conversation_title

Update the title of a conversation.

**Overview:**

Conversation titles are auto-generated from the first query by default.
Use this endpoint to set a custom, more descriptive title.

**Title limits:**

- Minimum: 1 character
- Maximum: 200 characters

**Permissions:**

The conversation must exist, belong to the calling user's organization,
be owned by the caller (matched on `userId`), and not be soft-deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConversationTitle" method="patch" path="/conversations/{conversationId}/title" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.update_conversation_title(conversation_id="<value>", title="Q4 Sales Analysis Discussion")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Unique conversation identifier                                      |                                                                     |
| `title`                                                             | *str*                                                               | :heavy_check_mark:                                                  | New conversation title                                              | Q4 Sales Analysis Discussion                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateConversationTitleResponse](../../models/updateconversationtitleresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive_conversation

Archive a conversation to hide it from the main list.

**Overview:**

Archived conversations are preserved but hidden from the default conversation list.
Use archiving to clean up your workspace without permanently deleting conversations.

**Access:**

The caller must be the conversation's initiator, or be listed in `sharedWith`
with `accessLevel: write`. Already-archived conversations return `400`.

**Retrieval:**

View archived conversations using `GET /conversations/show/archives`.
Restore one with `PATCH /conversations/{conversationId}/unarchive`.


### Example Usage

<!-- UsageSnippet language="python" operationID="archiveConversation" method="patch" path="/conversations/{conversationId}/archive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.archive_conversation(conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Conversation identifier                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ArchiveConversationResponse](../../models/archiveconversationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive_conversation

Restore an archived conversation.

- Path params: `conversationId`
- Query params: none
- Body: none


### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveConversation" method="patch" path="/conversations/{conversationId}/unarchive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.unarchive_conversation(conversation_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Conversation identifier                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnarchiveConversationResponse](../../models/unarchiveconversationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## regenerate_answer

Regenerate the AI response for a specific message and stream the new
answer over Server-Sent Events.

**Overview:**

If you're not satisfied with an AI response, use this endpoint to generate
a new answer. The original user query is re-processed and a new bot
response replaces the previous one in place.

**Constraints:**

- Only the *last* message of the conversation can be regenerated.
- The target message must be of type `bot_response`.

**Use Cases:**

- Response was incomplete or unclear
- Want to try a different AI model
- New documents have been indexed since original response

**Model Override:**

Specify `modelKey` to use a different model for regeneration.

**Streaming:**

The response is delivered as an SSE (`text/event-stream`) stream. The
exact event vocabulary depends on `chatMode`:

- For non-agent modes (e.g. `internal_search`, `web_search`) the
  request is dispatched to the assistant chat backend.
- For agent modes (e.g. `agent:auto`) the request is dispatched to
  the agent backend with a placeholder agent built from the caller's
  workspace, which can additionally emit `tool_result` and
  `tool_execution_complete` events.

See `SSEEvent` for the full union of event names this endpoint can
emit across both backends.


### Example Usage

<!-- UsageSnippet language="python" operationID="regenerateAnswer" method="post" path="/conversations/{conversationId}/message/{messageId}/regenerate" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.regenerate_answer(conversation_id="<value>", message_id="<value>", model_key="05438a37-68f2-4641-a8dc-6c47e63278ca", model_name="gpt-5.4-mini", model_friendly_name="mini", chat_mode="internal_search", timezone="Asia/Calcutta", current_time=parse_datetime("2026-05-11T15:43:21+05:30"), tools=[
        "jira.create_issue",
        "confluence.search_content",
    ])

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `message_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ID of the message to regenerate response for                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | App connector instance ids and knowledge-base / record-group ids that narrow retrieval<br/>for a turn. For **org assistant** chat streams, send explicit `apps` / `kb` lists.<br/>For **agent** chat streams, send explicit id lists, or **omit** `filters` (and `tools`)<br/>to let the service use the agent’s stored knowledge and tool configuration. Sending<br/>`{ "apps": [], "kb": [] }` on an agent stream means **no** knowledge sources for that<br/>turn (it is not “full org default”).<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Identifier of the AI model configuration to use for regeneration.<br/>Typically a UUID returned by the model-management endpoints. When<br/>omitted, the model used for the original message is reused.<br/>                                                                                                                                                                                                                                                                      | 05438a37-68f2-4641-a8dc-6c47e63278ca                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `model_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Provider model name (e.g. the underlying LLM identifier).                                                                                                                                                                                                                                                                                                                                                                                                                         | gpt-5.4-mini                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `model_friendly_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Friendly display name of the selected model.                                                                                                                                                                                                                                                                                                                                                                                                                                      | mini                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `chat_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Chat mode used for regeneration (for example `internal_search`,<br/>`web_search`, or an agent mode such as `agent:auto`).<br/>                                                                                                                                                                                                                                                                                                                                                    | internal_search                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `timezone`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | IANA timezone identifier from the client. Used to provide<br/>time-aware context to the AI during regeneration.<br/>                                                                                                                                                                                                                                                                                                                                                              | Asia/Calcutta                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `current_time`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ISO 8601 / RFC 3339 datetime from the client (UTC `Z` or numeric<br/>offset). Used to anchor any relative time references in the query.<br/>                                                                                                                                                                                                                                                                                                                                      | 2026-05-11 15:43:21 +0530 +0530                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tools`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional list of tool identifiers (fully-qualified action names<br/>such as `jira.create_issue`) the agent may invoke when<br/>regenerating. Applicable only in agent chat modes.<br/>                                                                                                                                                                                                                                                                                            | [<br/>"jira.create_issue",<br/>"confluence.search_content"<br/>]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[Union[eventstreaming.EventStream[models.SSEEvent], eventstreaming.EventStreamAsync[models.SSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_message_feedback

Append a feedback entry to a bot-response message.

**Overview**

Feedback helps improve AI response quality over time. You can record an
overall helpfulness signal, per-aspect ratings, issue categories, and
free-text comments. Each call appends a new entry to the message;
previous entries are preserved.

**Feedback options**

- `isHelpful` — overall thumbs up/down.
- `ratings` — 1–5 scores keyed by an aspect name you choose
  (e.g. `accuracy`, `relevance`, `completeness`, `clarity`).
- `categories` — issue or positive categories from a fixed list.
- `comments` — free-text `positive`, `negative`, and `suggestions`.
- `metrics` — optional client-side telemetry
  (`userInteractionTime`, `feedbackSessionId`).

**Restrictions**

Feedback can only be submitted on `bot_response` messages — user
queries and system messages are rejected with `400`.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessageFeedback" method="post" path="/conversations/{conversationId}/message/{messageId}/feedback" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.update_message_feedback(conversation_id="<value>", message_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                     | Type                                                                                                                                                                          | Required                                                                                                                                                                      | Description                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                                                                                             | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | Unique conversation identifier.                                                                                                                                               |
| `message_id`                                                                                                                                                                  | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | Identifier of the bot-response message being rated.                                                                                                                           |
| `is_helpful`                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                            | Overall helpfulness signal (thumbs up/down).                                                                                                                                  |
| `ratings`                                                                                                                                                                     | Dict[str, *float*]                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                            | Per-aspect ratings. Keys are arbitrary aspect names chosen<br/>by the client (typically `accuracy`, `relevance`,<br/>`completeness`, `clarity`); values are scores in the range<br/>1–5.<br/> |
| `categories`                                                                                                                                                                  | List[[models.CategoryRequest](../../models/categoryrequest.md)]                                                                                                               | :heavy_minus_sign:                                                                                                                                                            | Issue or positive categories that apply to the response.                                                                                                                      |
| `comments`                                                                                                                                                                    | [Optional[models.CommentsRequest]](../../models/commentsrequest.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                            | Free-text comments grouped by sentiment.                                                                                                                                      |
| `metrics`                                                                                                                                                                     | [Optional[models.MetricsRequest]](../../models/metricsrequest.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                            | Optional client-supplied telemetry.                                                                                                                                           |
| `retries`                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                           |

### Response

**[models.UpdateMessageFeedbackResponse](../../models/updatemessagefeedbackresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |