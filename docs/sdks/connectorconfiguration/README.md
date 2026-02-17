# ConnectorConfiguration

## Overview

### Available Operations

* [update_config](#update_config) - Update connector configuration
* [update_auth_config](#update_auth_config) - Update authentication configuration
* [get_google_workspace_credentials](#get_google_workspace_credentials) - Get Google Workspace credentials status

## update_config

Update authentication, sync, and filter configuration.<br><br>
<b>Prerequisites:</b><br>
Connector must be <b>disabled</b> before updating configuration.
Disable it first using <code>POST /{id}/toggle</code>.<br><br>
<b>Partial Updates:</b><br>
Only provide the sections you want to update. Omitted sections
are not modified.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorConfig" method="put" path="/connectors/{connectorId}/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_configuration.update_config(connector_id="<id>", auth={
        "values": {
            "apiKey": "sk-xxxxx",
            "baseUrl": "https://api.example.com",
        },
        "oauth_config_id": "oauth_config_123",
    }, sync={
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
    }, filters={
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
    }, base_url="https://confluence.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `connector_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `auth`                                                                                  | [Optional[models.ConnectorAuthConfig]](../../models/connectorauthconfig.md)             | :heavy_minus_sign:                                                                      | Authentication configuration for a connector instance                                   |                                                                                         |
| `sync`                                                                                  | [Optional[models.ConnectorSyncConfig]](../../models/connectorsyncconfig.md)             | :heavy_minus_sign:                                                                      | Synchronization configuration for a connector instance                                  |                                                                                         |
| `filters`                                                                               | [Optional[models.ConnectorFiltersConfig]](../../models/connectorfiltersconfig.md)       | :heavy_minus_sign:                                                                      | Filter configuration to control what data is synced (sync filters and indexing filters) |                                                                                         |
| `base_url`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Base URL for self-hosted instances                                                      | https://confluence.mycompany.com                                                        |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.UpdateConnectorConfigResponse](../../models/updateconnectorconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_auth_config

Update only the authentication configuration.<br><br>
<b>Use Case:</b><br>
Use this when you need to update credentials without changing
sync or filter settings. Useful for credential rotation.<br><br>
<b>Prerequisites:</b><br>
Connector must be disabled. This endpoint clears OAuth state,
requiring re-authentication for OAuth connectors.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorAuthConfig" method="put" path="/connectors/{connectorId}/config/auth" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_configuration.update_auth_config(connector_id="<id>", auth={
        "values": {
            "apiKey": "sk-xxxxx",
            "baseUrl": "https://api.example.com",
        },
        "oauth_config_id": "oauth_config_123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `auth`                                                              | [models.ConnectorAuthConfig](../../models/connectorauthconfig.md)   | :heavy_check_mark:                                                  | Authentication configuration for a connector instance               |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Base URL (if changed with auth update)                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateConnectorAuthConfigResponse](../../models/updateconnectorauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_google_workspace_credentials

Check if Google Workspace credentials are configured.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGoogleWorkspaceCredentials" method="get" path="/configurationManager/connectors/googleWorkspaceCredentials" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_configuration.get_google_workspace_credentials()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GoogleWorkspaceCredentials](../../models/googleworkspacecredentials.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |