# ConnectorInstances

## Overview

### Available Operations

* [list](#list) - List connector instances
* [create](#create) - Create connector instance
* [list_active](#list_active) - List active connector instances
* [list_inactive](#list_inactive) - List inactive connector instances
* [list_configured](#list_configured) - List configured connector instances
* [list_active_agents](#list_active_agents) - List active agent connectors
* [get](#get) - Get connector instance
* [delete](#delete) - Delete connector instance
* [update_name](#update_name) - Update connector instance name

## list

Get all configured connector instances for your organization.<br><br>
<b>Overview:</b><br>
Returns instances created by users, filtered by scope and permissions.
Team-scope connectors are visible to all org users. Personal connectors
are only visible to their creators.<br><br>
<b>Instance States:</b><br>
<ul>
<li><b>isConfigured:</b> All required settings are complete</li>
<li><b>isAuthenticated:</b> OAuth flow complete or credentials valid</li>
<li><b>isActive:</b> Connector is enabled for sync/agent</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="listConnectorInstances" method="get" path="/connectors" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.list(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scope`                                                             | [Optional[models.ConnectorScope]](../../models/connectorscope.md)   | :heavy_minus_sign:                                                  | Filter by scope (team or personal)                                  | team                                                                |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search by instance name                                             |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListConnectorInstancesResponse](../../models/listconnectorinstancesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create a new connector instance from a registry type.<br><br>
<b>Overview:</b><br>
Creates a new connector instance that can then be configured and enabled.
The instance is created in an unconfigured state and needs authentication
and filter setup before it can be activated.<br><br>
<b>Scope Permissions:</b><br>
<ul>
<li><code>team</code> scope requires admin privileges</li>
<li><code>personal</code> scope available to all users</li>
</ul>
<b>Next Steps After Creation:</b><br>
<ol>
<li>Configure authentication via <code>PUT /{id}/config/auth</code></li>
<li>Complete OAuth flow if needed via <code>GET /{id}/oauth/authorize</code></li>
<li>Set up filters via <code>POST /{id}/filters</code></li>
<li>Enable connector via <code>POST /{id}/toggle</code></li>
</ol>


### Example Usage: confluence

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="confluence" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.create(connector_type="confluence", instance_name="My Confluence", scope="personal", auth_type="API_TOKEN", config={
        "auth": {
            "values": {
                "apiKey": "sk-xxxxx",
                "baseUrl": "https://api.example.com",
            },
            "oauth_config_id": "oauth_config_123",
        },
        "sync": {
            "scheduled_config": {
                "cron_expression": "0 */6 * * *",
                "timezone": "America/New_York",
            },
            "webhook_config": {
                "events": [
                    "file.created",
                    "file.modified",
                    "file.deleted",
                ],
            },
        },
        "filters": {
            "sync": {
                "values": {
                    "folders": [
                        "folder_id_1",
                        "folder_id_2",
                    ],
                    "fileTypes": [
                        "pdf",
                        "docx",
                        "xlsx",
                    ],
                    "includeShared": True,
                },
            },
        },
    }, base_url="https://confluence.mycompany.com")

    # Handle response
    print(res)

```
### Example Usage: googleDrive

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="googleDrive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.create(connector_type="google-drive", instance_name="Company Google Drive", scope="team", auth_type="OAUTH_ADMIN_CONSENT", config={
        "auth": {
            "values": {
                "apiKey": "sk-xxxxx",
                "baseUrl": "https://api.example.com",
            },
            "oauth_config_id": "oauth_config_123",
        },
        "sync": {
            "scheduled_config": {
                "cron_expression": "0 */6 * * *",
                "timezone": "America/New_York",
            },
            "webhook_config": {
                "events": [
                    "file.created",
                    "file.modified",
                    "file.deleted",
                ],
            },
        },
        "filters": {
            "sync": {
                "values": {
                    "folders": [
                        "folder_id_1",
                        "folder_id_2",
                    ],
                    "fileTypes": [
                        "pdf",
                        "docx",
                        "xlsx",
                    ],
                    "includeShared": True,
                },
            },
        },
    }, base_url="https://confluence.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | Connector type from registry (e.g., google-drive, confluence, slack)                                                                                                                                                                            | google-drive                                                                                                                                                                                                                                    |
| `instance_name`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | Display name for this connector instance                                                                                                                                                                                                        | Marketing Team Drive                                                                                                                                                                                                                            |
| `scope`                                                                                                                                                                                                                                         | [models.ConnectorScope](../../models/connectorscope.md)                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                              | Scope determines visibility and access control for connectors:<br><br/><ul><br/><li><code>team</code> - Available to all users in the organization (admin-only creation)</li><br/><li><code>personal</code> - Private to the creating user only</li><br/></ul><br/> | team                                                                                                                                                                                                                                            |
| `auth_type`                                                                                                                                                                                                                                     | [Optional[models.AuthType]](../../models/authtype.md)                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                              | Authentication type (required if connector supports multiple auth methods)                                                                                                                                                                      | OAUTH                                                                                                                                                                                                                                           |
| `config`                                                                                                                                                                                                                                        | [Optional[models.CreateConnectorRequestConfig]](../../models/createconnectorrequestconfig.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                              | Initial configuration (can also be set after creation)                                                                                                                                                                                          |                                                                                                                                                                                                                                                 |
| `base_url`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Base URL for self-hosted instances (e.g., Confluence Server, GitLab Self-Managed)                                                                                                                                                               | https://confluence.mycompany.com                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.CreateConnectorInstanceResponse](../../models/createconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_active

Get all active (enabled) connector instances.<br><br>
<b>Overview:</b><br>
Returns only instances where <code>isActive: true</code>.
These are connectors currently syncing data or available to AI agents.


### Example Usage

<!-- UsageSnippet language="python" operationID="listActiveConnectors" method="get" path="/connectors/active" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.list_active()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActiveConnectorsResponse](../../models/listactiveconnectorsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_inactive

Get all inactive (disabled) connector instances.

### Example Usage

<!-- UsageSnippet language="python" operationID="listInactiveConnectors" method="get" path="/connectors/inactive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.list_inactive()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListInactiveConnectorsResponse](../../models/listinactiveconnectorsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_configured

Get all connector instances that have completed configuration.<br><br>
<b>Overview:</b><br>
Returns instances where <code>isConfigured: true</code>.
These have all required settings but may not be active yet.


### Example Usage

<!-- UsageSnippet language="python" operationID="listConfiguredConnectors" method="get" path="/connectors/configured" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.list_configured(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`                                                                                                                                                                                                                                         | [Optional[models.ConnectorScope]](../../models/connectorscope.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                              | Scope determines visibility and access control for connectors:<br><br/><ul><br/><li><code>team</code> - Available to all users in the organization (admin-only creation)</li><br/><li><code>personal</code> - Private to the creating user only</li><br/></ul><br/> | team                                                                                                                                                                                                                                            |
| `page`                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `search`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.ListConfiguredConnectorsResponse](../../models/listconfiguredconnectorsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_active_agents

Get connector instances enabled for AI agent integration.<br><br>
<b>Overview:</b><br>
Returns connectors where <code>agentEnabled: true</code>.
These are available to AI agents for querying and actions.


### Example Usage

<!-- UsageSnippet language="python" operationID="listActiveAgentConnectors" method="get" path="/connectors/agents/active" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.list_active_agents(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`                                                                                                                                                                                                                                         | [Optional[models.ConnectorScope]](../../models/connectorscope.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                              | Scope determines visibility and access control for connectors:<br><br/><ul><br/><li><code>team</code> - Available to all users in the organization (admin-only creation)</li><br/><li><code>personal</code> - Private to the creating user only</li><br/></ul><br/> | team                                                                                                                                                                                                                                            |
| `page`                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `search`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.ListActiveAgentConnectorsResponse](../../models/listactiveagentconnectorsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a specific connector instance by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorInstance" method="get" path="/connectors/{connectorId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.get(connector_id="conn_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID                                               | conn_abc123                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetConnectorInstanceResponse](../../models/getconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete a connector instance and all associated data.<br><br>
<b>Warning:</b><br>
This permanently removes the connector configuration.
Synced records in knowledge bases are NOT deleted.<br><br>
<b>Permissions:</b><br>
<ul>
<li>Team scope: Requires admin</li>
<li>Personal scope: Only creator can delete</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConnectorInstance" method="delete" path="/connectors/{connectorId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.delete(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteConnectorInstanceResponse](../../models/deleteconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_name

Update the display name of a connector instance.<br><br>
<b>Note:</b> This only updates the display name, not the connector configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorName" method="put" path="/connectors/{connectorId}/name" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_instances.update_name(connector_id="<id>", instance_name="Sales Team Drive (Updated)")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique connector instance ID                                        |                                                                     |
| `instance_name`                                                     | *str*                                                               | :heavy_check_mark:                                                  | New display name for the connector instance                         | Sales Team Drive (Updated)                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateConnectorNameResponse](../../models/updateconnectornameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |