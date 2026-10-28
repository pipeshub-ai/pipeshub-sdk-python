# ConnectorInstances

## Overview

Create, manage, and delete connector instances for your organization

### Available Operations

* [list_connector_instances](#list_connector_instances) - List connector instances
* [create_connector_instance](#create_connector_instance) - Create connector instance
* [get_connector_instance](#get_connector_instance) - Get connector instance
* [delete_connector_instance](#delete_connector_instance) - Delete connector instance
* [get_connector_stats](#get_connector_stats) - Get connector statistics
* [resync_connector](#resync_connector) - Resync connector
* [stop_connector_sync](#stop_connector_sync) - Stop the running sync for a connector

## list_connector_instances

Get all configured connector instances for your organization.<br><br>
<b>Overview:</b><br>
Returns instances created by users, filtered by scope and permissions.
Team-scope connectors are visible to all org users. Personal connectors
are only visible to their creators, not even to admins. Knowledge bases
(instances of type <code>KB</code>) are not listed here.<br><br>
<b>Instance States:</b><br>
<ul>
<li><b>isConfigured:</b> All required settings are complete</li>
<li><b>isAuthenticated:</b> OAuth flow complete or credentials valid</li>
<li><b>isActive:</b> Connector is enabled for sync/agent</li>
<li><b>desktopOnline:</b> Owner device's desktop app connected (Local FS only)</li>
<li><b>ownerDeviceId / ownerDeviceName:</b> Desktop device that owns the connector, set on first enable (Local FS only)</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="listConnectorInstances" method="get" path="/connectors" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.list_connector_instances(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                   | Type                                                                                                                                                                                                        | Required                                                                                                                                                                                                    | Description                                                                                                                                                                                                 | Example                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`                                                                                                                                                                                                     | [Optional[models.ConnectorInstanceListScope]](../../models/connectorinstancelistscope.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                          | Filter by scope. Defaults to <code>team</code> when omitted.<br/>                                                                                                                                           | team                                                                                                                                                                                                        |
| `page`                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | Page number, 1-based                                                                                                                                                                                        |                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | Items per page                                                                                                                                                                                              |                                                                                                                                                                                                             |
| `search`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | Full-text search across instance name, type, and app group. The term<br/>is not echoed back in <code>pagination</code>.<br/>                                                                                |                                                                                                                                                                                                             |
| `is_authenticated`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Filter by authentication status.<br/><code>true</code> returns only authenticated instances;<br/><code>false</code> returns only unauthenticated ones.<br/>Omit to return all.<br/>                         |                                                                                                                                                                                                             |
| `is_active`                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Filter by active status.<br/><code>true</code> returns only active instances;<br/><code>false</code> returns only inactive ones.<br/>Omit to return all.<br/>                                               |                                                                                                                                                                                                             |
| `connector_type`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | Filter by exact connector type string (e.g. <code>Confluence</code>,<br/><code>GoogleDrive</code>). Case-sensitive. An empty or blank value<br/>is refused with `400` (the value is trimmed before it is checked).<br/> |                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                         |                                                                                                                                                                                                             |

### Response

**[models.ListConnectorInstancesResponse](../../models/listconnectorinstancesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_connector_instance

Create a connector instance from a registry type.<br><br>
<b>Body:</b><br>
Put the auth fields the registry schema lists for <code>authType</code> in <code>config.auth</code>,
flat, and the connector's own sync settings in <code>config.sync</code>. A connector that needs no
OAuth sign-in is configured on creation.<br><br>
<b>OAuth:</b><br>
An admin may send the OAuth app's credentials in <code>config.auth</code>: the app is saved and
linked. Anyone may send <code>config.auth.oauthConfigId</code> to use a saved app; non-admins must.
Send <code>baseUrl</code>: the provider redirects to <code>{baseUrl}/{redirectUri}</code>.<br><br>
<b>Scope Permissions:</b><br>
<ul>
<li><code>team</code> scope requires admin privileges</li>
<li><code>personal</code> scope available to all users</li>
</ul>
<b>Next Steps After Creation:</b><br>
<ol>
<li>OAuth only: <code>GET /{id}/oauth/authorize</code>, then <code>GET /oauth/callback</code></li>
<li>Optionally set sync and filters via <code>PUT /{id}/config/filters-sync</code></li>
<li>Turn sync on via <code>POST /{id}/toggle</code></li>
</ol>


### Example Usage: confluence

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="confluence" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="confluence", instance_name="My Confluence", scope="personal", auth_type="API_TOKEN", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            **{
                "baseUrl": "https://mycompany.atlassian.net",
                "email": "admin@mycompany.com",
                "apiToken": "ATATT3x...",
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: googleDrive

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="googleDrive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="google-drive", instance_name="Company Google Drive", scope="team", auth_type="OAUTH_ADMIN_CONSENT", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            **{
                "baseUrl": "https://mycompany.atlassian.net",
                "email": "admin@mycompany.com",
                "apiToken": "ATATT3x...",
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: jiraNewOAuthApp

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="jiraNewOAuthApp" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="Jira", instance_name="Engineering Jira", scope="team", auth_type="OAUTH", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            oauth_instance_name="Atlassian app",
            **{
                "clientId": "your-atlassian-client-id",
                "clientSecret": "your-atlassian-client-secret",
            },
        ),
    ), base_url="https://pipeshub.example.com")

    # Handle response
    print(res)

```
### Example Usage: jiraPersonal

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="jiraPersonal" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="Jira Cloud Personal", instance_name="My Jira", scope="personal", auth_type="API_TOKEN", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            **{
                "baseUrl": "https://mycompany.atlassian.net",
                "email": "admin@mycompany.com",
                "apiToken": "ATATT3x...",
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: jiraSavedOAuthApp

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="jiraSavedOAuthApp" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="Jira", instance_name="Engineering Jira", scope="team", auth_type="OAUTH", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            oauth_config_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        ),
    ), base_url="https://pipeshub.example.com")

    # Handle response
    print(res)

```
### Example Usage: oneDrive

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="oneDrive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="OneDrive", instance_name="Company OneDrive", scope="team", auth_type="OAUTH_ADMIN_CONSENT", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            **{
                "baseUrl": "https://mycompany.atlassian.net",
                "email": "admin@mycompany.com",
                "apiToken": "ATATT3x...",
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: postgresBasicAuth

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="postgresBasicAuth" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="PostgreSQL", instance_name="Analytics database", scope="team", auth_type="BASIC_AUTH", config=models.CreateConnectorRequestConfig(
        auth=models.ConnectorAuthConfig(
            **{
                "host": "db.example.com",
                "port": 5432,
                "database": "analytics",
                "username": "reader",
                "password": "your-password",
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: rss

<!-- UsageSnippet language="python" operationID="createConnectorInstance" method="post" path="/connectors" example="rss" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.create_connector_instance(connector_type="RSS", instance_name="Company blog", scope="team", config=models.CreateConnectorRequestConfig(
        sync=models.ConnectorSyncConfig(
            **{
                "feed_urls": "https://example.com/feed.xml",
                "max_articles_per_feed": 50,
            },
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | `type` from the registry                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                 |
| `instance_name`                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `scope`                                                                                                                                                                                                                                         | [models.ConnectorScope](../../models/connectorscope.md)                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                              | Scope determines visibility and access control for connectors:<br><br/><ul><br/><li><code>team</code> - Available to all users in the organization (admin-only creation)</li><br/><li><code>personal</code> - Private to the creating user only</li><br/></ul><br/> | team                                                                                                                                                                                                                                            |
| `auth_type`                                                                                                                                                                                                                                     | [Optional[models.ConnectorAuthType]](../../models/connectorauthtype.md)                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                              | One of the type's `supportedAuthTypes`; defaults to the first                                                                                                                                                                                   |                                                                                                                                                                                                                                                 |
| `config`                                                                                                                                                                                                                                        | [Optional[models.CreateConnectorRequestConfig]](../../models/createconnectorrequestconfig.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `base_url`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Origin of the page the OAuth provider redirects back to. The redirect URI is `{baseUrl}/{redirectUri}`; defaults to the PipesHub frontend URL.                                                                                                  |                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.CreateConnectorInstanceResponse](../../models/createconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_instance

Retrieve a specific connector instance by ID, together with the setup
form of its connector type (<code>config</code>).<br><br>
<b>Who can read an instance:</b><br>
<ul>
<li>Team scope: the creator and org admins. Other members get
<code>404</code>, although the lists show them the instance.</li>
<li>Personal scope: the creator only. An admin gets <code>404</code>.</li>
</ul>
The ID of a knowledge base is accepted too: a knowledge base is stored
as a connector instance of type <code>KB</code>.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorInstance" method="get" path="/connectors/{connectorId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.get_connector_instance(connector_id="conn_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID (`_key` of the instance)                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectorInstanceResponse](../../models/getconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_connector_instance

Start the deletion of a connector instance and all associated data.<br><br>
<b>Asynchronous:</b><br>
The request is answered with <code>202</code> as soon as the instance is
marked <code>DELETING</code>; its sync is stopped and its records,
vectors and configuration are removed in the background.<br><br>
<b>Permissions:</b><br>
<ul>
<li>The creator can delete their own instance</li>
<li>An org admin can delete any instance, including another user's
personal one (which the admin cannot read)</li>
<li>Anyone else gets <code>404</code></li>
</ul>
<b>In use:</b><br>
Refused with <code>409</code> while an agent uses the instance as a
knowledge source.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConnectorInstance" method="delete" path="/connectors/{connectorId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.delete_connector_instance(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID (`_key` of the instance)                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteConnectorInstanceResponse](../../models/deleteconnectorinstanceresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_stats

Retrieve record counts of a connector instance, in total and per record
type, broken down by indexing status. The ID of a knowledge base is
accepted too (a knowledge base is stored as a connector instance of type
<code>KB</code>); its stats report <code>origin: COLLECTION</code>.<br><br>
<b>Who can read them:</b> the creator of the instance and, for a team
instance, org admins. Stats use the same read gate as
<code>GET /connectors/{connectorId}</code>: anyone else, including an
admin reading another user's personal instance, gets <code>404</code>
("This connector was removed, or you no longer have access. ..."), so
the instance's existence is not confirmed.

An OAuth token holding `kb:read` instead of `connector:read` passes the scope check too.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorStats" method="get" path="/connectors/{connectorId}/stats" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.get_connector_stats(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                 | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                            | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | Connector instance ID (`_key` of the instance) or knowledge base ID.<br/>Unlike the other instance routes, the ID is not checked against a<br/>pattern: an ID no instance has is answered `404`.<br/> |
| `retries`                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                       |

### Response

**[models.ConnectorStats](../../models/connectorstats.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## resync_connector

Trigger a resync of records from a connector instance.

**Overview:**

Fetches content from the external source and updates local records. Use when you suspect data is out of sync.

Only a connector in the caller's list of active connectors
(`GET /connectors/active`, knowledge bases included) can be resynced.
Any other ID, including one that does not exist, is refused with `400`.
The reply only acknowledges that the resync event was published.

Fields of the body other than `connectorName` and `fullSync` are dropped without an error.

**Warning:** This can be resource-intensive for large connectors.

The scope check also accepts `kb:write` in place of `connector:write`.


### Example Usage

<!-- UsageSnippet language="python" operationID="resyncConnector" method="post" path="/connectors/{connectorId}/resync" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.resync_connector(connector_id="<id>", connector_name="GOOGLE_DRIVE", full_sync=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                            | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Connector instance ID. An ID that decodes to a path separator or<br/>another unsafe segment is refused with `400` before the token is checked.<br/>       |                                                                                                                                                           |
| `connector_name`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The connector's type as the registry lists it, for example `RSS` or<br/>`Jira`. It names the sync event; the connector synced is always the<br/>one in the path.<br/> | RSS                                                                                                                                                       |
| `full_sync`                                                                                                                                               | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | When true, triggers a full sync instead of incremental.                                                                                                   |                                                                                                                                                           |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ResyncConnectorResponse](../../models/resyncconnectorresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorResponse              | 400, 401, 403                     | application/json                  |
| errors.LocalFsDesktopRefusalError | 409                               | application/json                  |
| errors.ErrorResponse              | 409                               | application/json                  |
| errors.ErrorResponse              | 500, 503                          | application/json                  |
| errors.PipeshubDefaultError       | 4XX, 5XX                          | \*/\*                             |

## stop_connector_sync

Ask the in-flight sync for a connector instance to stop.

**Overview:**

Returns as soon as the request is recorded; the sync halts at its next
interruptible point, which for a connector inside a long provider call
is when that call returns. `stopped` reports whether a sync was actually
running, and `false` is a normal answer rather than a failure.

Deliberately not refused while the connector is busy or locked: this is
the endpoint that has to work precisely then, including against a lock a
crashed process left behind. When nothing is running it also repairs a
stale SYNCING or FULL_SYNCING status, unless the service cannot tell a
live sync on another worker from a stale one, in which case it changes
nothing and says so.


### Example Usage

<!-- UsageSnippet language="python" operationID="stopConnectorSync" method="post" path="/connectors/{connectorId}/sync/stop" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_instances.stop_connector_sync(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StopConnectorSyncResponse](../../models/stopconnectorsyncresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |