# AgentTemplates

## Overview

### Available Operations

* [list](#list) - List agent templates
* [create](#create) - Create agent template
* [get_template](#get_template) - Get agent template
* [update](#update) - Update agent template
* [delete](#delete) - Delete agent template

## list

Retrieve all available agent templates.<br><br>
<b>Overview:</b><br>
Agent templates provide pre-configured starting points for creating
custom AI agents. Templates include system prompts, recommended tools,
and configuration schemas.<br><br>
<b>Template Types:</b><br>
<ul>
<li>Public templates available to all organization users</li>
<li>Private templates created by individual users</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgentTemplates" method="get" path="/agents/template" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_templates.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAgentTemplatesResponse](../../models/listagenttemplatesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create a new reusable agent template.<br><br>
<b>Overview:</b><br>
Templates define the base configuration for agents including
system prompts, tool recommendations, and customization options.<br><br>
<b>Template Components:</b><br>
<ul>
<li><b>System prompt:</b> Default instructions for agents</li>
<li><b>Recommended tools:</b> Suggested tool integrations</li>
<li><b>Config schema:</b> JSON Schema for customization options</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createAgentTemplate" method="post" path="/agents/template" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_templates.create(name="Customer Support Agent", description="A template for customer support agents", system_prompt="You are a helpful customer support assistant.", category="Support", is_public=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `name`                                                                                              | *str*                                                                                               | :heavy_check_mark:                                                                                  | Template name                                                                                       | Customer Support Agent                                                                              |
| `description`                                                                                       | *str*                                                                                               | :heavy_check_mark:                                                                                  | What agents from this template do                                                                   | A template for customer support agents                                                              |
| `system_prompt`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | System instructions for the template                                                                | You are a helpful customer support assistant.                                                       |
| `category`                                                                                          | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Template category                                                                                   | Support                                                                                             |
| `recommended_tools`                                                                                 | List[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | Suggested tool keys                                                                                 |                                                                                                     |
| `config_schema`                                                                                     | [Optional[models.CreateAgentTemplateConfigSchema]](../../models/createagenttemplateconfigschema.md) | :heavy_minus_sign:                                                                                  | JSON Schema for customization                                                                       |                                                                                                     |
| `is_public`                                                                                         | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Make template available organization-wide                                                           |                                                                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

### Response

**[models.CreateAgentTemplateResponse](../../models/createagenttemplateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_template

Retrieve a specific agent template by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentTemplate" method="get" path="/agents/template/{templateId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_templates.get_template(template_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Template identifier                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAgentTemplateResponse](../../models/getagenttemplateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update an existing agent template.<br><br>
<b>Permissions:</b><br>
Only the template creator can update it.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAgentTemplate" method="put" path="/agents/template/{templateId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.agent_templates.update(template_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                       | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `name`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `description`                                                                                       | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `category`                                                                                          | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `system_prompt`                                                                                     | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `recommended_tools`                                                                                 | List[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `config_schema`                                                                                     | [Optional[models.UpdateAgentTemplateConfigSchema]](../../models/updateagenttemplateconfigschema.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `is_public`                                                                                         | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.UpdateAgentTemplateResponse](../../models/updateagenttemplateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete an agent template.<br><br>
<b>Note:</b><br>
Existing agents created from this template are not affected.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAgentTemplate" method="delete" path="/agents/template/{templateId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.agent_templates.delete(template_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |