# Agents

## Overview

Custom AI agents with specialized capabilities and tool integrations

### Available Operations

* [list_agents](#list_agents) - List agents
* [create_agent](#create_agent) - Create agent
* [list_agent_tools](#list_agent_tools) - List available tools
* [get_agent](#get_agent) - Get agent
* [update_agent](#update_agent) - Update agent
* [delete_agent](#delete_agent) - Delete agent
* [get_agent_permissions](#get_agent_permissions) - Get agent permissions
* [update_agent_permissions](#update_agent_permissions) - Update agent permissions
* [share_agent](#share_agent) - Share agent
* [unshare_agent](#unshare_agent) - Unshare an agent

## list_agents

Retrieve all agents available to the authenticated user.<br><br>
<b>Overview:</b><br>
Returns agents created by the user plus public agents in the organization.
Each agent has unique capabilities defined by its tools and knowledge scope.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgents" method="get" path="/api/v1/agents" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.list_agents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAgentsResponse](../../models/listagentsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_agent

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

<!-- UsageSnippet language="python" operationID="createAgent" method="post" path="/api/v1/agents/create" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.create_agent(name="Product Support Agent", models=[
        {
            "model_key": "gpt-4o",
            "model_name": "GPT-4o",
            "provider": "openai",
            "is_reasoning": False,
        },
    ], is_public=False, share_with_org=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `name`                                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | Agent display name                                                                              | Product Support Agent                                                                           |
| `models`                                                                                        | List[[models.CreateAgentModelUnion](../../models/createagentmodelunion.md)]                     | :heavy_check_mark:                                                                              | Agent model configuration entries                                                               | [<br/>{<br/>"modelKey": "gpt-4o",<br/>"modelName": "GPT-4o",<br/>"provider": "openai",<br/>"isReasoning": false<br/>}<br/>] |
| `description`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | What the agent does                                                                             |                                                                                                 |
| `system_prompt`                                                                                 | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | System instructions for the agent                                                               |                                                                                                 |
| `start_message`                                                                                 | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Initial greeting shown when conversation starts                                                 |                                                                                                 |
| `instructions`                                                                                  | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | Additional agent execution instructions                                                         |                                                                                                 |
| `toolsets`                                                                                      | List[[models.CreateAgentToolset](../../models/createagenttoolset.md)]                           | :heavy_minus_sign:                                                                              | Toolsets attached to the agent (instance-aware)                                                 |                                                                                                 |
| `knowledge`                                                                                     | List[[models.CreateAgentKnowledge](../../models/createagentknowledge.md)]                       | :heavy_minus_sign:                                                                              | Knowledge sources connected to the agent                                                        |                                                                                                 |
| `is_public`                                                                                     | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Make agent available to all org users                                                           |                                                                                                 |
| `share_with_org`                                                                                | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Share agent with the organization                                                               |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.CreateAgentResponse](../../models/createagentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_agent_tools

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

<!-- UsageSnippet language="python" operationID="listAgentTools" method="get" path="/api/v1/agents/tools/list" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.list_agent_tools()

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

## get_agent

Retrieve agent details by its unique key.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgent" method="get" path="/api/v1/agents/{agentKey}" -->
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
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_agent

Update an existing agent's configuration.<br><br>
<b>Permissions:</b><br>
Only the agent creator can update it.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgent" method="put" path="/api/v1/agents/{agentKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.update_agent(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `agent_key`                                                                 | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `name`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `description`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `system_prompt`                                                             | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `start_message`                                                             | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `instructions`                                                              | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | N/A                                                                         |
| `models`                                                                    | List[[models.UpdateAgentModelUnion](../../models/updateagentmodelunion.md)] | :heavy_minus_sign:                                                          | N/A                                                                         |
| `toolsets`                                                                  | List[[models.UpdateAgentToolset](../../models/updateagenttoolset.md)]       | :heavy_minus_sign:                                                          | N/A                                                                         |
| `knowledge`                                                                 | List[[models.UpdateAgentKnowledge](../../models/updateagentknowledge.md)]   | :heavy_minus_sign:                                                          | N/A                                                                         |
| `is_public`                                                                 | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | N/A                                                                         |
| `share_with_org`                                                            | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UpdateAgentResponse](../../models/updateagentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_agent

Delete an agent.<br><br>
<b>Warning:</b><br>
All conversations with this agent will become inaccessible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgent" method="delete" path="/api/v1/agents/{agentKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.agents.delete_agent(agent_key="<value>")

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

## get_agent_permissions

Get the current permission configuration for an agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentPermissions" method="get" path="/api/v1/agents/{agentKey}/permissions" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.get_agent_permissions(agent_key="<value>")

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

## update_agent_permissions

Update who can access and use the agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgentPermissions" method="put" path="/api/v1/agents/{agentKey}/permissions" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.agents.update_agent_permissions(agent_key="<value>")

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

## share_agent

Share an agent with specific users.

### Example Usage

<!-- UsageSnippet language="python" operationID="shareAgent" method="post" path="/api/v1/agents/{agentKey}/share" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.share_agent(agent_key="<value>", user_ids=[
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

## unshare_agent

Revoke sharing for an agent, removing access for specified users or teams.


### Example Usage

<!-- UsageSnippet language="python" operationID="unshareAgent" method="post" path="/api/v1/agents/{agentKey}/unshare" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agents.unshare_agent(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `team_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnshareAgentResponse](../../models/unshareagentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |