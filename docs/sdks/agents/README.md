# Agents

## Overview

Custom AI agents with specialized capabilities and tool integrations

### Available Operations

* [get_all](#get_all) - List agents
* [create](#create) - Create agent
* [get_tools](#get_tools) - List available tools
* [get](#get) - Get agent
* [update](#update) - Update agent
* [delete](#delete) - Delete agent
* [get_permissions](#get_permissions) - Get agent permissions
* [update_permissions](#update_permissions) - Update agent permissions
* [share](#share) - Share agent
* [unshare](#unshare) - Revoke agent access

## get_all

Retrieve all agents available to the authenticated user.<br><br>
<b>Overview:</b><br>
Returns agents created by the user plus public agents in the organization.
Each agent has unique capabilities defined by its tools and knowledge scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgents" method="get" path="/agents" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.get_all()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Agent]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create a new custom AI agent.<br><br>
<b>Overview:</b><br>
Agents are specialized AI assistants configured for specific tasks.
They can have custom system prompts, access to specific tools, and
be limited to certain knowledge bases.<br><br>
<b>Agent Configuration:</b><br>
<ul>
<li><b>System prompt:</b> Instructions that define agent behavior</li>
<li><b>Tools:</b> Capabilities like web search, code execution, etc.</li>
<li><b>Knowledge bases:</b> Data sources the agent can access</li>
<li><b>Model config:</b> AI model settings (temperature, max tokens)</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Customer support bot with product knowledge</li>
<li>Code review assistant with repository access</li>
<li>HR assistant with policy documents</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createAgent" method="post" path="/agents/create" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.create(name="Product Support Agent", is_public=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `name`                                                                        | *str*                                                                         | :heavy_check_mark:                                                            | Agent display name                                                            | Product Support Agent                                                         |
| `description`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | What the agent does                                                           |                                                                               |
| `system_prompt`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | System instructions for the agent                                             |                                                                               |
| `tools`                                                                       | List[*str*]                                                                   | :heavy_minus_sign:                                                            | Tool keys the agent can use                                                   |                                                                               |
| `knowledge_bases`                                                             | List[*str*]                                                                   | :heavy_minus_sign:                                                            | Knowledge base IDs to access                                                  |                                                                               |
| `llm_config`                                                                  | [Optional[models.CreateAgentLlmConfig]](../../models/createagentllmconfig.md) | :heavy_minus_sign:                                                            | N/A                                                                           |                                                                               |
| `is_public`                                                                   | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Make agent available to all org users                                         |                                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_tools

Get all tools that can be assigned to agents.<br><br>
<b>Overview:</b><br>
Tools extend agent capabilities beyond basic Q&A. Each tool
has specific inputs and outputs defined by its schema.<br><br>
<b>Common Tools:</b><br>
<ul>
<li><b>web-search:</b> Search the internet</li>
<li><b>code-interpreter:</b> Execute code snippets</li>
<li><b>file-reader:</b> Read uploaded files</li>
<li><b>api-caller:</b> Make external API requests</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgentTools" method="get" path="/agents/tools/list" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.get_tools()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AgentTool]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve agent details by its unique key.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgent" method="get" path="/agents/{agentKey}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.get(agent_key="customer-support-agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique agent identifier                                             | customer-support-agent                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update an existing agent's configuration.<br><br>
<b>Permissions:</b><br>
Only the agent creator can update it.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgent" method="put" path="/agents/{agentKey}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.update(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `agent_key`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `name`                                                                        | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `description`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `system_prompt`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `tools`                                                                       | List[*str*]                                                                   | :heavy_minus_sign:                                                            | N/A                                                                           |
| `knowledge_bases`                                                             | List[*str*]                                                                   | :heavy_minus_sign:                                                            | N/A                                                                           |
| `llm_config`                                                                  | [Optional[models.UpdateAgentLlmConfig]](../../models/updateagentllmconfig.md) | :heavy_minus_sign:                                                            | N/A                                                                           |
| `is_public`                                                                   | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete an agent.<br><br>
<b>Warning:</b><br>
All conversations with this agent will become inaccessible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgent" method="delete" path="/agents/{agentKey}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.agents.delete(agent_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_permissions

Get the current permission configuration for an agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentPermissions" method="get" path="/agents/{agentKey}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.get_permissions(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAgentPermissionsResponse](../../models/getagentpermissionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_permissions

Update who can access and use the agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgentPermissions" method="put" path="/agents/{agentKey}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.agents.update_permissions(agent_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                       | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `is_public`                                                                                       | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `shared_with`                                                                                     | List[[models.UpdateAgentPermissionsSharedWith](../../models/updateagentpermissionssharedwith.md)] | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## share

Share an agent with specific users.

### Example Usage

<!-- UsageSnippet language="python" operationID="shareAgent" method="post" path="/agents/{agentKey}/share" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.share(agent_key="<value>", user_ids=[
        "507f1f77bcf86cd799439011",
    ], access_level="read")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              | Example                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                              | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | N/A                                                                                                                                      |                                                                                                                                          |
| `user_ids`                                                                                                                               | List[*str*]                                                                                                                              | :heavy_check_mark:                                                                                                                       | IDs of users to share with                                                                                                               | [<br/>"507f1f77bcf86cd799439011"<br/>]                                                                                                   |
| `access_level`                                                                                                                           | [Optional[models.ShareRequestAccessLevel]](../../models/sharerequestaccesslevel.md)                                                      | :heavy_minus_sign:                                                                                                                       | Permission level for shared users:<br/><ul><br/><li><code>read</code> - Can view only</li><br/><li><code>write</code> - Can add messages</li><br/></ul><br/> |                                                                                                                                          |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |                                                                                                                                          |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unshare

Remove sharing access from specified users.

### Example Usage

<!-- UsageSnippet language="python" operationID="unshareAgent" method="post" path="/agents/{agentKey}/unshare" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.agents.unshare(agent_key="<value>", user_ids=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |