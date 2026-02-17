# ConnectorRegistry

## Overview

### Available Operations

* [list](#list) - List available connector types
* [get_schema](#get_schema) - Get connector configuration schema

## list

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_registry.list(scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scope`                                                             | [Optional[models.ConnectorScope]](../../models/connectorscope.md)   | :heavy_minus_sign:                                                  | Filter by scope type                                                | team                                                                |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Items per page                                                      |                                                                     |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search term for connector names                                     |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetConnectorRegistryResponse](../../models/getconnectorregistryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_schema

Get the configuration schema for a specific connector type.<br><br>
<b>Overview:</b><br>
Returns JSON Schema definitions for authentication, sync settings, and
filter options. Use this to dynamically build configuration forms.<br><br>
<b>Schema Sections:</b><br>
<ul>
<li><b>authSchema:</b> Fields for authentication (credentials, tokens)</li>
<li><b>syncSchema:</b> Sync settings (schedule, incremental options)</li>
<li><b>filterSchema:</b> Filter field definitions</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorSchema" method="get" path="/connectors/registry/{connectorType}/schema" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_registry.get_schema(connector_type="google-drive")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Connector type identifier                                           | google-drive                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetConnectorSchemaResponse](../../models/getconnectorschemaresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |