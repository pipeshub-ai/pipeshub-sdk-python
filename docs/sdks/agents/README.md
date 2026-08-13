# Agents

## Overview

Custom AI agents with specialized capabilities and tool integrations

### Available Operations

* [list_agents](#list_agents) - List agents
* [create_agent](#create_agent) - Create agent
* [get_agent](#get_agent) - Get agent
* [update_agent](#update_agent) - Update agent
* [delete_agent](#delete_agent) - Delete agent
* [list_agent_archived_conversations_grouped](#list_agent_archived_conversations_grouped) - List archived agent conversations grouped by agent
* [list_agent_conversation_archives](#list_agent_conversation_archives) - List archived conversations for an agent
* [upload_agent_conversation_chat_attachments](#upload_agent_conversation_chat_attachments) - Upload agent chat attachments
* [delete_agent_conversation_chat_attachment](#delete_agent_conversation_chat_attachment) - Delete an agent chat attachment
* [stream_agent_conversation](#stream_agent_conversation) - Create agent conversation with streaming response
* [stream_agent_conversation_message](#stream_agent_conversation_message) - Add message to agent conversation with streaming response
* [regenerate_agent_conversation_message](#regenerate_agent_conversation_message) - Regenerate agent conversation message
* [update_agent_conversation_message_feedback](#update_agent_conversation_message_feedback) - Submit feedback for an agent message
* [archive_agent_conversation](#archive_agent_conversation) - Archive an agent conversation
* [unarchive_agent_conversation](#unarchive_agent_conversation) - Unarchive an agent conversation
* [update_agent_conversation_title](#update_agent_conversation_title) - Update agent conversation title
* [delete_agent_conversation_by_id](#delete_agent_conversation_by_id) - Delete an agent conversation
* [get_agent_conversation_by_id](#get_agent_conversation_by_id) - Get agent conversation by ID
* [list_agent_conversations](#list_agent_conversations) - List agent conversations

## list_agents

Retrieve a paginated list of agents available to the authenticated user.

**Overview**

Returns agents accessible through direct, team, or org-level permissions.
Search is performed across agent name, description, and tags. Sorting and
pagination are applied by the AI backend and the resulting envelope is
forwarded unchanged by the Node gateway.

**Gateway contract**

The Node route supports only these query params: `page`, `limit`, `search`,
`sort_by`, and `sort_order`.

The Python backend also understands `isDeleted`, but this gateway route
does not forward it, so it is not part of the public API contract here.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgents" method="get" path="/agents" example="success" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.list_agents(page=1, limit=20, sort_by="updatedAtTimestamp", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                          | *Optional[int]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | 1-based page number.                                                                                                                            |
| `limit`                                                                                                                                         | *Optional[int]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | Maximum number of agents to return in the current page.                                                                                         |
| `search`                                                                                                                                        | *Optional[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | Case-insensitive search across agent name, description, and tags. Leading/trailing whitespace is trimmed; blank-after-trim values are rejected. |
| `sort_by`                                                                                                                                       | *Optional[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | Backend sort field. Leading/trailing whitespace is trimmed. Common value is `updatedAtTimestamp`.                                               |
| `sort_order`                                                                                                                                    | [Optional[models.ListAgentsSortOrder]](../../models/listagentssortorder.md)                                                                     | :heavy_minus_sign:                                                                                                                              | Sort direction.                                                                                                                                 |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.AgentListResponse](../../models/agentlistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_agent

Create a new custom AI agent.

**Overview:**
Agents are specialized AI assistants configured for specific tasks.
They can have custom system prompts, access to specific tools, and
be limited to certain knowledge bases.

**Agent Configuration:**
- **System prompt:** Instructions that define agent behavior
- **Tools:** Capabilities like web search, code execution, etc.
- **Knowledge bases:** Data sources the agent can access
- **Model config:** AI model settings (temperature, max tokens)

**Use Cases:**
- Customer support bot with product knowledge
- Code review assistant with repository access
- HR assistant with policy documents


### Example Usage

<!-- UsageSnippet language="python" operationID="createAgent" method="post" path="/agents/create" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.create_agent(name="Product Support Agent", share_with_org=False, is_service_account=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                 | Agent display name                                                                                                                                                                                                                                                                                                                                                                                 | Product Support Agent                                                                                                                                                                                                                                                                                                                                                                              |
| `description`                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | What the agent does                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `start_message`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Initial greeting shown when conversation starts                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `system_prompt`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | System instructions for the agent                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `instructions`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Additional agent execution instructions                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `models`                                                                                                                                                                                                                                                                                                                                                                                           | List[[models.AgentCreateModelEntryUnion](../../models/agentcreatemodelentryunion.md)]                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Agent model configuration entries. Optional — an agent created without<br/>any models (an empty array or an omitted field) uses the organization's<br/>default LLM at chat time. When at least one model entry IS provided, the<br/>gateway requires at least one object entry with `isReasoning: true`.<br/>String-only arrays are schema-valid but rejected at runtime with HTTP 400<br/>unless the array is empty.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `tags`                                                                                                                                                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `share_with_org`                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Share agent with the organization                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `is_service_account`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Create the agent as a service-account agent                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `toolsets`                                                                                                                                                                                                                                                                                                                                                                                         | List[[models.AgentCreateToolset](../../models/agentcreatetoolset.md)]                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Toolsets attached to the agent (instance-aware)                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `knowledge`                                                                                                                                                                                                                                                                                                                                                                                        | List[[models.AgentCreateKnowledge](../../models/agentcreateknowledge.md)]                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Knowledge sources connected to the agent                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `skills`                                                                                                                                                                                                                                                                                                                                                                                           | List[[models.AgentSkillAssignment](../../models/agentskillassignment.md)]                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Existing skills to assign to the agent                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `web_search`                                                                                                                                                                                                                                                                                                                                                                                       | [OptionalNullable[models.AgentCreateWebSearchUnion]](../../models/agentcreatewebsearchunion.md)                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Web-search attachment for an agent. Accepts either a provider string<br/>or an object with at least a `provider` field.<br/>                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `default_reasoning_effort`                                                                                                                                                                                                                                                                                                                                                                         | [OptionalNullable[models.AgentCreateRequestDefaultReasoningEffort]](../../models/agentcreaterequestdefaultreasoningeffort.md)                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Agent-level reasoning effort used when a chat request omits its own.                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                    |

### Response

**[models.AgentCreateResponse](../../models/agentcreateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_agent

Retrieve agent details by its unique key.

**Gateway not-found behavior:**
Unknown `agentKey`, lookup after soft-delete, and other AI-backend failures
that return 404 from the Python query service are surfaced by the Node
gateway as **HTTP 404** with an `ErrorResponse` body.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAgent" method="get" path="/agents/{agentKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.get_agent(agent_key="customer-support-agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique agent identifier                                             | customer-support-agent                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetAgentResponse](../../models/getagentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_agent

Apply a partial update to an existing agent configuration.

**Gateway contract**

The Node gateway validates the request body via Zod middleware before
forwarding to the Python agent service. The `agentKey` path param and
the request body are both validated. Query parameters are ignored by
the controller.

**Update semantics**

Only fields present in the request body are updated. `models` may be
omitted (the agent's existing models are kept), set to an empty array
(clears the agent's models so it falls back to the organization's
default LLM at chat time), or set to a non-empty array. When a
non-empty array is provided, the gateway Zod middleware requires at
least one object entry with `isReasoning: true`.

**Permissions**

The authenticated user must have `can_edit` on the agent (typically the
owner). Service-account and `shareWithOrg` transitions follow additional
Python business rules.

**Success response**

Returns a lightweight success envelope only. Use
`GET /agents/{agentKey}` to read the persisted agent after an update.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgent" method="put" path="/agents/{agentKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.update_agent(agent_key="customer-support-agent", name="Renamed Agent", share_with_org=False, is_service_account=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                    | Unique agent identifier                                                                                                                                                                                                                                                                                                                               | customer-support-agent                                                                                                                                                                                                                                                                                                                                |
| `name`                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Agent display name                                                                                                                                                                                                                                                                                                                                    | Renamed Agent                                                                                                                                                                                                                                                                                                                                         |
| `description`                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | What the agent does                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                       |
| `start_message`                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Initial greeting shown when conversation starts                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |
| `system_prompt`                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | System instructions for the agent                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                       |
| `instructions`                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Additional agent execution instructions                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                       |
| `models`                                                                                                                                                                                                                                                                                                                                              | List[[models.AgentCreateModelEntryUnion](../../models/agentcreatemodelentryunion.md)]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Agent model configuration entries. Optional. An empty array clears the<br/>agent's models so it falls back to the organization's default LLM.<br/>When a non-empty array is present, the Zod middleware requires at<br/>least one object entry with `isReasoning: true`. String-only arrays<br/>are schema-valid but rejected at runtime with HTTP 400 unless empty.<br/> |                                                                                                                                                                                                                                                                                                                                                       |
| `tags`                                                                                                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                       |
| `share_with_org`                                                                                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Share agent with the organization                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                       |
| `is_service_account`                                                                                                                                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Mark agent as a service account                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |
| `toolsets`                                                                                                                                                                                                                                                                                                                                            | List[[models.AgentCreateToolset](../../models/agentcreatetoolset.md)]                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Toolsets attached to the agent (instance-aware)                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |
| `knowledge`                                                                                                                                                                                                                                                                                                                                           | List[[models.AgentCreateKnowledge](../../models/agentcreateknowledge.md)]                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Knowledge sources connected to the agent                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                       |
| `skills`                                                                                                                                                                                                                                                                                                                                              | List[[models.AgentSkillAssignment](../../models/agentskillassignment.md)]                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Complete replacement set of skills assigned to the agent. Send<br/>an empty array to clear all skill assignments.<br/>                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                       |
| `web_search`                                                                                                                                                                                                                                                                                                                                          | [OptionalNullable[models.AgentCreateWebSearchUnion]](../../models/agentcreatewebsearchunion.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Web-search attachment for an agent. Accepts either a provider string<br/>or an object with at least a `provider` field.<br/>                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                       |
| `default_reasoning_effort`                                                                                                                                                                                                                                                                                                                            | [OptionalNullable[models.AgentUpdateRequestDefaultReasoningEffort]](../../models/agentupdaterequestdefaultreasoningeffort.md)                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Agent-level reasoning effort used when a chat request omits its own.                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                       |

### Response

**[models.AgentUpdateResponse](../../models/agentupdateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_agent

Soft-delete an agent (tombstone) in the graph database.

**Overview:**
The Python query service marks the agent instance deleted inside a transaction.
List and search endpoints exclude tombstoned agents. Toolsets, tools, and
knowledge linked to the agent are not removed by this call.

**Permissions:**
Only the agent owner may delete (`can_delete` on the permission check).

**Warning:**
All conversations with this agent will become inaccessible.

**Gateway not-found behavior:**
Unknown `agentKey`, deleting an already-deleted agent, and `GET /agents/{agentKey}`
after delete return **HTTP 404** with an `ErrorResponse` body.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgent" method="delete" path="/agents/{agentKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.delete_agent(agent_key="customer-support-agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique agent identifier (gateway Zod requires non-empty string).    | customer-support-agent                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AgentDeleteResponse](../../models/agentdeleteresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 404                    | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_agent_archived_conversations_grouped

Returns archived agent conversations for the current user, grouped by
`agentKey`, with pagination over agent groups. Excludes conversations
whose agent was soft-deleted upstream.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgentArchivedConversationsGrouped" method="get" path="/agents/conversations/show/archives" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.list_agent_archived_conversations_grouped(agent_page=1, agent_limit=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_page`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_limit`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentArchivedGroupsResponse](../../models/agentarchivedgroupsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_agent_conversation_archives

Paginated list of archived conversations for the given agent key.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAgentConversationArchives" method="get" path="/agents/{agentKey}/conversations/show/archives" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.list_agent_conversation_archives(agent_key="<value>", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                       | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `page`                                                                                                            | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `limit`                                                                                                           | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `sort_by`                                                                                                         | [Optional[models.ListAgentConversationArchivesSortBy]](../../models/listagentconversationarchivessortby.md)       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `sort_order`                                                                                                      | [Optional[models.ListAgentConversationArchivesSortOrder]](../../models/listagentconversationarchivessortorder.md) | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `search`                                                                                                          | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `start_date`                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `end_date`                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.AgentArchivedConversationListResponse](../../models/agentarchivedconversationlistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upload_agent_conversation_chat_attachments

Multipart upload of PDF, JPEG, or PNG files for agent chat. Same limits as assistant
chat (`POST /conversations/attachments/upload`): up to 10 files, 5 MiB each. Proxies to
the AI backend. Optional `conversationId` associates uploads with an existing agent thread.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadAgentConversationChatAttachments" method="post" path="/agents/{agentKey}/conversations/attachments/upload" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.upload_agent_conversation_chat_attachments(agent_key="<value>", files=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                 |
| `files`                                                                                                                                                                                                                                                                                                                                                                             | List[[models.UploadAgentConversationChatAttachmentsFile](../../models/uploadagentconversationchatattachmentsfile.md)]                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                  | One or more files; field name must be `files`. Accepted MIME types: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, `text/plain`, `text/markdown`, `text/mdx`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `text/csv`, `text/tab-separated-values`. Max 5 MiB each.<br/> |
| `conversation_id`                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                  | Optional existing agent conversation id. Empty string is treated as unset; any non-empty value must be a 24-character ObjectId.<br/>                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.ChatAttachmentUploadResponse](../../models/chatattachmentuploadresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_agent_conversation_chat_attachment

Deletes a previously uploaded attachment by proxying `DELETE` to the query service
(`/api/v1/chat/attachments/{recordId}`). The Node handler always ends the response **without
a JSON body** on success (empty body); the **status code** is the upstream status, or **204**
if none is returned.

On validation failure in the gateway (invalid / blank path params), the response is **400**
with a small JSON error object. Same fire-and-forget semantics as
`DELETE /conversations/attachments/{recordId}` on the client.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgentConversationChatAttachment" method="delete" path="/agents/{agentKey}/conversations/attachments/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.agents.delete_agent_conversation_chat_attachment(agent_key="<value>", record_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `agent_key`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | Agent key path parameter. Must be non-empty.                                   |
| `record_id`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | Attachment record id (from the upload response). Must be non-blank after trim. |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.DeleteAgentConversationChatAttachmentBadRequestError | 400                                                         | application/json                                            |
| errors.PipeshubDefaultError                                 | 4XX, 5XX                                                    | \*/\*                                                       |

## stream_agent_conversation

Start a new conversation with the specified agent and stream the AI
response as Server-Sent Events (SSE). The first user message is saved
and forwarded to the upstream agent backend; subsequent tokens, tool
calls, and lifecycle events are emitted on the open SSE connection.

AG-UI is the sole wire protocol. The request must include
`chatMode: quick`; see `AgentStreamSSEEvent` for the event vocabulary.


### Example Usage

<!-- UsageSnippet language="python" operationID="streamAgentConversation" method="post" path="/agents/{agentKey}/conversations/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.stream_agent_conversation(agent_key="<value>", query="what are some latest tech news?", chat_mode="quick", filters={
        "apps": [
            "2605c882-61d4-4aa2-b480-a68c957c151d",
            "ed6d6cc4-70bd-4838-9aeb-488e910c833a",
            "aeab9ddc-fb9b-47c8-ad98-bd4744e19555",
        ],
        "kb": [
            "8747da12-4724-4a95-ac92-827b88d79647",
        ],
    }, applied_filters={
        "apps": [
            {
                "id": "2605c882-61d4-4aa2-b480-a68c957c151d",
                "name": "US Headlines, abcnews",
                "node_type": "app",
                "connector": "RSS",
            },
            {
                "id": "ed6d6cc4-70bd-4838-9aeb-488e910c833a",
                "name": "ABC News RSS",
                "node_type": "app",
                "connector": "RSS",
            },
            {
                "id": "aeab9ddc-fb9b-47c8-ad98-bd4744e19555",
                "name": "Hacker news rss",
                "node_type": "app",
                "connector": "RSS",
            },
        ],
        "kb": [
            {
                "id": "8747da12-4724-4a95-ac92-827b88d79647",
                "name": "Siddhant Ota's Private",
                "node_type": "recordGroup",
                "connector": "KB",
            },
        ],
    }, model_key="5c1832f4-fa19-4167-b913-307fad3a6551", model_name="gpt-5.4-mini", model_friendly_name="GPT 5.4 mini", timezone="Asia/Kolkata", current_time=parse_datetime("2026-05-19T12:58:01+05:30"), tools=[])

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                        | Stable key identifying the agent that owns this conversation.                                                                                                                                                                                                             |
| `query`                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                        | User prompt for the first turn. Saved as the initial `user_query`<br/>message and sent to the agent backend.<br/>                                                                                                                                                         |
| `chat_mode`                                                                                                                                                                                                                                                               | [models.AgentStreamCreateConversationRequestChatMode](../../models/agentstreamcreateconversationrequestchatmode.md)                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                        | Required execution mode. Scoped agent conversations currently<br/>support only `quick`.<br/>                                                                                                                                                                              |
| `record_ids`                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Optional record ids to include as context for this turn. Each id<br/>must be a 24-character MongoDB ObjectId.<br/>                                                                                                                                                        |
| `filters`                                                                                                                                                                                                                                                                 | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Optional retrieval scope (`apps` / `kb`) for this turn. Each id must<br/>be a valid UUID. Omit for agent defaults; send `{ "apps": [], "kb": [] }`<br/>to force no knowledge sources for this turn.<br/>                                                                  |
| `applied_filters`                                                                                                                                                                                                                                                         | [Optional[models.AppliedFilters]](../../models/appliedfilters.md)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                        | UI filter state persisted on the saved user message. Not used for<br/>retrieval and not forwarded to the upstream agent backend.<br/>                                                                                                                                     |
| `attachments`                                                                                                                                                                                                                                                             | List[[models.ChatAttachmentRef](../../models/chatattachmentref.md)]                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Uploaded attachments to ground this turn. Each entry references a<br/>record id returned from the agent attachment upload endpoint.<br/>                                                                                                                                  |
| `model_key`                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                        | AI model configuration id for this turn. Omit to use the agent's<br/>default model.<br/>                                                                                                                                                                                  |
| `model_name`                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Provider model name (the underlying LLM identifier).                                                                                                                                                                                                                      |
| `model_friendly_name`                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Friendly UI label for the selected model.                                                                                                                                                                                                                                 |
| `timezone`                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Client IANA timezone, such as `America/New_York`. Helps the agent<br/>resolve relative date references in the prompt.<br/>                                                                                                                                                |
| `current_time`                                                                                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Client time in ISO 8601 / RFC 3339 format (UTC `Z` or numeric<br/>offset). Sent alongside `timezone` for time-aware answers.<br/>                                                                                                                                         |
| `tools`                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Allowed tool ids for this turn, such as `jira.create_issue`. Omit<br/>to let the agent use its default toolset; send `[]` to disable<br/>tools for this turn.<br/>                                                                                                        |
| `protocol`                                                                                                                                                                                                                                                                | [Optional[models.AgentStreamCreateConversationRequestProtocol]](../../models/agentstreamcreateconversationrequestprotocol.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                        | AG-UI is the only supported wire protocol. When present must be<br/>`"agui"`. Omitting the field is equivalent — the server always<br/>uses the AG-UI vocabulary (see `AgentStreamSSEEvent`). Kept in<br/>the schema for backward compatibility with callers that already<br/>send it.<br/> |
| `agent_capabilities`                                                                                                                                                                                                                                                      | [Optional[models.AgentCapabilities]](../../models/agentcapabilities.md)                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Per-request agent capability toggles. Only meaningful when `chatMode`<br/>selects an agent mode; ignored otherwise. Each field falls back to its<br/>own `default` below when omitted — a missing flag is not uniformly<br/>`true`. Omitting the whole object applies every default.<br/> |
| `retries`                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                       |

### Response

**[Union[eventstreaming.EventStream[models.AgentStreamSSEEvent], eventstreaming.EventStreamAsync[models.AgentStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream_agent_conversation_message

Append a user message to an existing agent conversation and stream the
assistant reply over SSE.

AG-UI is the sole wire protocol. The request must include
`chatMode: quick`; see `AgentMessageStreamSSEEvent` for the event
vocabulary.


### Example Usage

<!-- UsageSnippet language="python" operationID="streamAgentConversationMessage" method="post" path="/agents/{agentKey}/conversations/{conversationId}/messages/stream" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.stream_agent_conversation_message(agent_key="<value>", conversation_id="<value>", query="can you elaborate on the latest headlines?", chat_mode="quick", filters={
        "apps": [
            "2605c882-61d4-4aa2-b480-a68c957c151d",
            "ed6d6cc4-70bd-4838-9aeb-488e910c833a",
        ],
        "kb": [
            "8747da12-4724-4a95-ac92-827b88d79647",
        ],
    }, applied_filters={
        "apps": [
            {
                "id": "2605c882-61d4-4aa2-b480-a68c957c151d",
                "name": "US Headlines, abcnews",
                "node_type": "app",
                "connector": "RSS",
            },
            {
                "id": "ed6d6cc4-70bd-4838-9aeb-488e910c833a",
                "name": "ABC News RSS",
                "node_type": "app",
                "connector": "RSS",
            },
        ],
        "kb": [
            {
                "id": "8747da12-4724-4a95-ac92-827b88d79647",
                "name": "Siddhant Ota's Private",
                "node_type": "recordGroup",
                "connector": "KB",
            },
        ],
    }, model_key="5c1832f4-fa19-4167-b913-307fad3a6551", model_name="gpt-5.4-mini", model_friendly_name="GPT 5.4 mini", timezone="Asia/Kolkata", current_time=parse_datetime("2026-05-19T12:58:01+05:30"), tools=[])

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `agent_key`                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                            |
| `conversation_id`                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                            |
| `query`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | User follow-up prompt to append to the existing agent conversation.<br/>Saved as a new `user_query` message before the upstream AI stream<br/>starts.<br/>                                                                                                                     |
| `chat_mode`                                                                                                                                                                                                                                                                    | [models.AgentAddMessageStreamRequestChatMode](../../models/agentaddmessagestreamrequestchatmode.md)                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                             | Required execution mode. Scoped agent conversations currently<br/>support only `quick`.<br/>                                                                                                                                                                                   |
| `filters`                                                                                                                                                                                                                                                                      | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Optional retrieval scope (`apps` / `kb`) for this turn. Each id must<br/>be a valid UUID. Omit to let the agent use its stored defaults;<br/>send `{ "apps": [], "kb": [] }` to force no knowledge sources for this turn.<br/>                                                 |
| `applied_filters`                                                                                                                                                                                                                                                              | [Optional[models.AppliedFilters]](../../models/appliedfilters.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                             | UI filter state persisted on the saved user message. Not used for<br/>retrieval and not forwarded to the upstream agent backend.<br/>                                                                                                                                          |
| `attachments`                                                                                                                                                                                                                                                                  | List[[models.ChatAttachmentRef](../../models/chatattachmentref.md)]                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Uploaded attachments to ground this turn. Each entry references a<br/>record id returned from the agent attachment upload endpoint.<br/>                                                                                                                                       |
| `model_key`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | AI model configuration id override for this turn. Omit to use the<br/>agent's default model.<br/>                                                                                                                                                                              |
| `model_name`                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Provider model name (the underlying LLM identifier).                                                                                                                                                                                                                           |
| `model_friendly_name`                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Friendly UI label for the selected model.                                                                                                                                                                                                                                      |
| `timezone`                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Client IANA timezone, such as `America/New_York`. Helps the agent<br/>resolve relative date references in the prompt.<br/>                                                                                                                                                     |
| `current_time`                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Client time in ISO 8601 / RFC 3339 format (UTC `Z` or numeric<br/>offset). Sent alongside `timezone` for time-aware answers.<br/>                                                                                                                                              |
| `tools`                                                                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Allowed tool ids for this turn, such as `jira.create_issue`. Omit<br/>to let the agent use its default toolset; send `[]` to disable<br/>tools for this turn.<br/>                                                                                                             |
| `protocol`                                                                                                                                                                                                                                                                     | [Optional[models.AgentAddMessageStreamRequestProtocol]](../../models/agentaddmessagestreamrequestprotocol.md)                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                             | AG-UI is the only supported wire protocol. When present must be<br/>`"agui"`. Omitting the field is equivalent — the server always<br/>uses the AG-UI vocabulary (see `AgentMessageStreamSSEEvent`).<br/>Kept in the schema for backward compatibility with callers that<br/>already send it.<br/> |
| `agent_capabilities`                                                                                                                                                                                                                                                           | [Optional[models.AgentCapabilities]](../../models/agentcapabilities.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Per-request agent capability toggles. Only meaningful when `chatMode`<br/>selects an agent mode; ignored otherwise. Each field falls back to its<br/>own `default` below when omitted — a missing flag is not uniformly<br/>`true`. Omitting the whole object applies every default.<br/> |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |

### Response

**[Union[eventstreaming.EventStream[models.AgentMessageStreamSSEEvent], eventstreaming.EventStreamAsync[models.AgentMessageStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## regenerate_agent_conversation_message

Regenerate the AI response for a specific message in an agent
conversation and stream the new answer over Server-Sent Events.

**Constraints:**

- Only the last message in the conversation can be regenerated.
- The target message must be of type `bot_response`.

**Request body:**

`chatMode: quick` is required. Other fields are optional and reuse
the original model/context when omitted. The body supports:
- `filters`
- `chatMode`
- `modelKey`
- `modelName`
- `modelFriendlyName`
- `timezone`
- `currentTime`
- `tools`
- `protocol`
- `agentCapabilities`

**Streaming behavior:**

The response is delivered as an AG-UI `text/event-stream`. Stable
outcomes are `RUN_FINISHED` and `RUN_ERROR`; see
`AgentRegenerateSSEEvent`.

Additional agent/tool lifecycle events may be forwarded by the
backend and should be treated as informational updates.

Validation failures on params/body are returned as normal HTTP `400`
responses before the stream starts. Valid-shape requests that fail
conversation lookup or regenerate rules are reported as
`RUN_ERROR` events after stream initialization.


### Example Usage

<!-- UsageSnippet language="python" operationID="regenerateAgentConversationMessage" method="post" path="/agents/{agentKey}/conversations/{conversationId}/message/{messageId}/regenerate" -->
```python
import os
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.regenerate_agent_conversation_message(agent_key="<value>", conversation_id="<value>", message_id="<value>", chat_mode="quick", model_key="05438a37-68f2-4641-a8dc-6c47e63278ca", model_name="gpt-5.4-mini", model_friendly_name="mini", timezone="Asia/Calcutta", current_time=parse_datetime("2026-05-11T15:43:21+05:30"), tools=[
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
| `agent_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Stable key identifying the agent that owns this conversation.                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `conversation_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ID of the agent conversation containing the target message.                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `message_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ID of the bot-response message to regenerate.                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `chat_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [models.AgentRegenerateRequestChatMode](../../models/agentregeneraterequestchatmode.md)                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | App connector instance ids and knowledge-base / record-group ids that narrow retrieval<br/>for a turn. For **org assistant** chat streams, send explicit `apps` / `kb` lists.<br/>For **agent** chat streams, send explicit id lists, or **omit** `filters` (and `tools`)<br/>to let the service use the agent’s stored knowledge and tool configuration. Sending<br/>`{ "apps": [], "kb": [] }` on an agent stream means **no** knowledge sources for that<br/>turn (it is not “full org default”).<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Identifier of the AI model configuration to use for regeneration.<br/>Typically a UUID returned by the model-management endpoints. When<br/>omitted, the model used for the original message is reused.<br/>                                                                                                                                                                                                                                                                      | 05438a37-68f2-4641-a8dc-6c47e63278ca                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `model_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Provider model name (e.g. the underlying LLM identifier).                                                                                                                                                                                                                                                                                                                                                                                                                         | gpt-5.4-mini                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `model_friendly_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Friendly display name of the selected model.                                                                                                                                                                                                                                                                                                                                                                                                                                      | mini                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `timezone`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | IANA timezone identifier from the client. Used to provide<br/>time-aware context to the AI during regeneration.<br/>                                                                                                                                                                                                                                                                                                                                                              | Asia/Calcutta                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `current_time`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ISO 8601 / RFC 3339 datetime from the client (UTC `Z` or numeric<br/>offset). Used to anchor any relative time references in the query.<br/>                                                                                                                                                                                                                                                                                                                                      | 2026-05-11T15:43:21+05:30                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `tools`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional list of tool identifiers (fully-qualified action names<br/>such as `jira.create_issue`) the agent may invoke when<br/>regenerating. Applicable only in agent chat modes.<br/>                                                                                                                                                                                                                                                                                            | [<br/>"jira.create_issue",<br/>"confluence.search_content"<br/>]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `protocol`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Optional[models.AgentRegenerateRequestProtocol]](../../models/agentregeneraterequestprotocol.md)                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | AG-UI is the only supported wire protocol. When present must be<br/>`"agui"`. Omitting the field is equivalent — the server always<br/>uses the AG-UI vocabulary. Kept in the schema for backward<br/>compatibility with callers that already send it.<br/>                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `agent_capabilities`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.AgentCapabilities]](../../models/agentcapabilities.md)                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Per-request agent capability toggles. Only meaningful when `chatMode`<br/>selects an agent mode; ignored otherwise. Each field falls back to its<br/>own `default` below when omitted — a missing flag is not uniformly<br/>`true`. Omitting the whole object applies every default.<br/>                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[Union[eventstreaming.EventStream[models.AgentRegenerateSSEEvent], eventstreaming.EventStreamAsync[models.AgentRegenerateSSEEvent]]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_agent_conversation_message_feedback

Append structured feedback to a bot-response message in an agent
conversation. Uses the same request body shape as
`updateMessageFeedback` (helpfulness, categories, comments). Feedback
can only be submitted on `bot_response` messages.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgentConversationMessageFeedback" method="post" path="/agents/{agentKey}/conversations/{conversationId}/message/{messageId}/feedback" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.update_agent_conversation_message_feedback(agent_key="<value>", conversation_id="<value>", message_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                   | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Unique agent identifier (gateway Zod requires non-empty string).                                              |
| `conversation_id`                                                                                             | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Unique conversation identifier.                                                                               |
| `message_id`                                                                                                  | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Identifier of the bot-response message being rated.                                                           |
| `is_helpful`                                                                                                  | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Overall helpfulness signal (thumbs up/down).                                                                  |
| `categories`                                                                                                  | List[[models.MessageFeedbackSubmitRequestCategory](../../models/messagefeedbacksubmitrequestcategory.md)]     | :heavy_minus_sign:                                                                                            | Issue or positive categories that apply to the response.                                                      |
| `comments`                                                                                                    | [Optional[models.MessageFeedbackSubmitRequestComments]](../../models/messagefeedbacksubmitrequestcomments.md) | :heavy_minus_sign:                                                                                            | Free-text comments grouped by sentiment.                                                                      |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.MessageFeedbackUpdateResponse](../../models/messagefeedbackupdateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive_agent_conversation

Marks the conversation as archived for the authenticated owner.

### Example Usage

<!-- UsageSnippet language="python" operationID="archiveAgentConversation" method="post" path="/agents/{agentKey}/conversations/{conversationId}/archive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.archive_agent_conversation(agent_key="<value>", conversation_id="<value>")

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

**[models.AgentConversationArchiveResponse](../../models/agentconversationarchiveresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive_agent_conversation

Restores an archived agent conversation to the active list.

### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveAgentConversation" method="post" path="/agents/{agentKey}/conversations/{conversationId}/unarchive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.unarchive_agent_conversation(agent_key="<value>", conversation_id="<value>")

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

**[models.AgentConversationUnarchiveResponse](../../models/agentconversationunarchiveresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_agent_conversation_title

Updates the display title for an agent conversation owned by the caller.

The controller looks up the conversation by `_id`, `orgId`, `userId`,
`agentKey`, and `isDeleted: false`.

The request body uses the shared title validator (`1..200` chars), and
the controller trims the incoming title before saving it. A whitespace-only
title can therefore still return HTTP 400 even if the raw string is
non-empty.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgentConversationTitle" method="patch" path="/agents/{agentKey}/conversations/{conversationId}/title" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.update_agent_conversation_title(agent_key="<value>", conversation_id="<value>", title="ABC News Follow-up")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `title`                                                             | *str*                                                               | :heavy_check_mark:                                                  | New title for the conversation                                      | ABC News Follow-up                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AgentConversationTitleUpdateResponse](../../models/agentconversationtitleupdateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_agent_conversation_by_id

Soft-deletes an agent conversation owned by the authenticated user.

The controller scopes the lookup by `_id`, `orgId`, `userId`, and
`agentKey`. If no matching writable conversation is found, the route is
intentionally a no-op and still returns HTTP 200 with `conversation: null`.

This makes the operation idempotent:

- deleting a nonexistent conversation returns success with `null`
- deleting through a different `agentKey` returns success with `null`
- deleting an already deleted conversation returns success with `null`


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgentConversationById" method="delete" path="/agents/{agentKey}/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.delete_agent_conversation_by_id(agent_key="<value>", conversation_id="<value>")

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

**[models.AgentConversationDeleteResponse](../../models/agentconversationdeleteresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401                    | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_agent_conversation_by_id

Returns the conversation with paginated/sorted messages and filter metadata.

**Message Pagination:**

Messages are paginated newest-first: `page=1` returns the most recent
batch. Increment `page` to load older batches (used by the infinite-scroll
"load older messages" feature).

- `page`: Page number (default: 1)
- `limit`: Messages per page (default: 20, max: 100)


### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentConversationById" method="get" path="/agents/{agentKey}/conversations/{conversationId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.get_agent_conversation_by_id(agent_key="<value>", conversation_id="<value>", page=1, limit=20, sort_by="createdAt", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `conversation_id`                                                                                           | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `page`                                                                                                      | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | Page number for message pagination (1 = most recent batch)                                                  |
| `limit`                                                                                                     | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | Number of messages per page                                                                                 |
| `sort_by`                                                                                                   | [Optional[models.GetAgentConversationByIDSortBy]](../../models/getagentconversationbyidsortby.md)           | :heavy_minus_sign:                                                                                          | Field to sort messages by                                                                                   |
| `sort_order`                                                                                                | [Optional[models.GetAgentConversationByIDSortOrder]](../../models/getagentconversationbyidsortorder.md)     | :heavy_minus_sign:                                                                                          | Sort direction                                                                                              |
| `start_date`                                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                        | :heavy_minus_sign:                                                                                          | Filter messages created on or after this date                                                               |
| `end_date`                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                        | :heavy_minus_sign:                                                                                          | Filter messages created on or before this date                                                              |
| `message_type`                                                                                              | [Optional[models.GetAgentConversationByIDMessageType]](../../models/getagentconversationbyidmessagetype.md) | :heavy_minus_sign:                                                                                          | Filter messages by type                                                                                     |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.AgentConversationDetailResponse](../../models/agentconversationdetailresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_agent_conversations

Paginated list of conversations for the agent (owned and shared-with-me),
excluding archived threads.


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

    res = pipeshub.agents.list_agent_conversations(agent_key="<value>", page=1, limit=20, start_date="2026-05-26T00:00:00.000Z", end_date="2026-05-27T00:00:00.000Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | Agent identifier used to scope the conversation list.                                                                                                                                                                                          |                                                                                                                                                                                                                                                |
| `page`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | 1-based page number. Defaults to `1`.                                                                                                                                                                                                          |                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Page size. Defaults to `20`; maximum `100`.                                                                                                                                                                                                    |                                                                                                                                                                                                                                                |
| `sort_by`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Preferred sort field. Supported values are `createdAt`,<br/>`lastActivityAt`, and `title`.<br/><br/>The current gateway validator preserves legacy behavior: unsupported<br/>values are accepted but ignored, and the handler falls back to<br/>`lastActivityAt`.<br/> |                                                                                                                                                                                                                                                |
| `sort_order`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Preferred sort direction. Supported values are `asc` and `desc`.<br/><br/>The current gateway validator preserves legacy behavior: unsupported<br/>values are accepted but ignored, and the handler falls back to<br/>descending order.<br/>   |                                                                                                                                                                                                                                                |
| `search`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Case-insensitive search term applied to conversation `title` and<br/>`messages.content`. Maximum length is 1000 characters. HTML/XSS<br/>payloads and format specifiers are rejected.<br/>                                                     |                                                                                                                                                                                                                                                |
| `start_date`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Inclusive lower bound on `createdAt`. The handler accepts any<br/>JavaScript-parseable date string; invalid values return HTTP 400.<br/>                                                                                                       | 2026-05-26T00:00:00.000Z                                                                                                                                                                                                                       |
| `end_date`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Inclusive upper bound on `createdAt`. The handler accepts any<br/>JavaScript-parseable date string; invalid values return HTTP 400.<br/>                                                                                                       | 2026-05-27T00:00:00.000Z                                                                                                                                                                                                                       |
| `status`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | Optional status filter applied to the `sharedWithMeConversations`<br/>branch of the response. The main `conversations` list ignores this<br/>parameter.<br/>                                                                                   |                                                                                                                                                                                                                                                |
| `is_archived`                                                                                                                                                                                                                                  | [Optional[models.IsArchived]](../../models/isarchived.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                             | Optional archived flag applied to the `sharedWithMeConversations`<br/>branch before the route-level non-archived guard is enforced.<br/>Accepted values are `true` and `false`.<br/>                                                           |                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |                                                                                                                                                                                                                                                |

### Response

**[models.AgentConversationListResponse](../../models/agentconversationlistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |