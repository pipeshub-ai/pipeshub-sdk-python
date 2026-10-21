# ConnectorRegistry

## Overview

Browse available connector types and their configuration schemas

### Available Operations

* [get_connector_registry](#get_connector_registry) - List available connector types
* [get_connector_schema](#get_connector_schema) - Get connector configuration schema
* [test_connector_connection](#test_connector_connection) - Test connector credentials before saving
* [get_connector_egress_ips](#get_connector_egress_ips) - Get the IP addresses connectors connect from

## get_connector_registry

Get all available connector types from the registry.<br><br>
<b>Overview:</b><br>
The registry contains all connector types that can be configured as instances.
Each type has specific authentication requirements, supported scopes, and capabilities.<br><br>
<b>Connector Types Include:</b><br>
<ul>
<li><b>Google Workspace:</b> Drive, Gmail, Calendar, etc.</li>
<li><b>Microsoft 365:</b> OneDrive, Outlook, SharePoint, etc.</li>
<li><b>Cloud Storage:</b> Dropbox, Box, AWS S3</li>
<li><b>Collaboration:</b> Slack, Confluence, Notion, Jira</li>
<li><b>Databases:</b> PostgreSQL, MySQL, MongoDB</li>
</ul>
<b>Filtering:</b><br>
Use <code>scope</code> to filter by team or personal connectors.
Use <code>search</code> for full-text search across connector names.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorRegistry" method="get" path="/connectors/registry" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_registry.get_connector_registry(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `scope`                                                                           | [Optional[models.ConnectorRegistryScope]](../../models/connectorregistryscope.md) | :heavy_minus_sign:                                                                | Which connector types to list. Defaults to `team`.                                | team                                                                              |
| `page`                                                                            | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | Page number                                                                       |                                                                                   |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | Items per page                                                                    |                                                                                   |
| `search`                                                                          | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Search term for connector names                                                   |                                                                                   |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |

### Response

**[models.GetConnectorRegistryResponse](../../models/getconnectorregistryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_schema

The configuration form for one connector type.<br><br>
<b>Sections:</b><br>
<ul>
<li><b>auth:</b> <code>supportedAuthTypes</code>, and per auth type in <code>schemas</code> the
fields to send in <code>config.auth</code> (by <code>name</code>) plus, for OAuth, the
<code>redirectUri</code> path</li>
<li><b>sync:</b> <code>supportedStrategies</code>, <code>scheduledConfig</code> defaults, and the
connector's own settings in <code>customFields</code> (sent in <code>config.sync</code> by
<code>name</code>)</li>
<li><b>filters:</b> the <code>sync</code> and <code>indexing</code> filter fields; a field with
<code>optionSourceType: dynamic</code> gets its values from
<code>GET /connectors/{connectorId}/filters/{filterKey}/options</code></li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorSchema" method="get" path="/connectors/registry/{connectorType}/schema" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_registry.get_connector_schema(connector_type="Jira")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Connector type: `type` from GET /connectors/registry                | Jira                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetConnectorSchemaResponse](../../models/getconnectorschemaresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## test_connector_connection

Try the auth settings from a connector's setup form without creating or
changing an instance.<br><br>
<b>Overview:</b><br>
Only connector types whose schema has <code>supportsConnectionCheck: true</code>
can be tested. A failed check is not an error: the response is
<code>200</code> with <code>success: false</code> and a <code>message</code>
to show the user (for example a wrong password, an unknown database, or a
timeout because a firewall blocks PipesHub's IP address).<br><br>
<b>Editing an instance:</b><br>
Pass <code>connectorId</code> to lay the settings over the instance's saved
ones, as <code>PUT /connectors/{connectorId}/config/auth</code> does. The
caller must be allowed to update that instance.


### Example Usage

<!-- UsageSnippet language="python" operationID="testConnectorConnection" method="post" path="/connectors/registry/{connectorType}/test-connection" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_registry.test_connector_connection(connector_type="PostgreSQL", auth={
        "host": "db.example.com",
        "port": "5432",
        "database": "analytics",
        "username": "reader",
        "password": "your-password",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                           | Type                                                                                                                                                                                                                | Required                                                                                                                                                                                                            | Description                                                                                                                                                                                                         | Example                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                  | Connector type identifier                                                                                                                                                                                           | PostgreSQL                                                                                                                                                                                                          |
| `auth`                                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                  | Auth values, keyed by the fields of the connector's auth schema                                                                                                                                                     | {<br/>"host": "db.example.com",<br/>"port": "5432",<br/>"database": "analytics",<br/>"username": "reader",<br/>"password": "your-password"<br/>}                                                                    |
| `connector_id`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | Instance being edited; its saved auth values fill in fields left out.<br/>A secret sent as `••••••••` (the mask the config routes return) keeps the<br/>stored value; any other value that is sent replaces the saved one.<br/> |                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                 |                                                                                                                                                                                                                     |

### Response

**[models.TestConnectorConnectionResponse](../../models/testconnectorconnectionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_egress_ips

Public IP addresses PipesHub's connectors use to reach external systems, for
users to allow in a database's or API's firewall.<br><br>
Set by the deployment through <code>CONNECTOR_EGRESS_IPS</code>; otherwise
looked up by the connector service and cached. The list is empty when the
address cannot be determined, or when the deployment sets
<code>CONNECTOR_EGRESS_IPS=none</code>.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorEgressIps" method="get" path="/connectors/network/egress-ips" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_registry.get_connector_egress_ips()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectorEgressIpsResponse](../../models/getconnectoregressipsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 403                    | application/json            |
| errors.ErrorResponse        | 503                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |