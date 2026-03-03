# ConnectorConfiguration

## Overview

Configure authentication, sync settings, and filters for connectors

### Available Operations

* [get_connector_config](#get_connector_config) - Get connector configuration
* [update_connector_config](#update_connector_config) - Update connector configuration
* [update_connector_auth_config](#update_connector_auth_config) - Update authentication configuration
* [update_connector_filters_sync_config](#update_connector_filters_sync_config) - Update filters and sync configuration

## get_connector_config

Get the current configuration for a connector instance.<br><br>
<b>Security:</b><br>
Sensitive data (credentials, OAuth tokens) are redacted from the response.
Only admins can see partial credential information.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorConfig" method="get" path="/connectors/{connectorId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.get_connector_config(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectorConfigResponse](../../models/getconnectorconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_connector_config

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_config(connector_id="<id>", auth={
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

## update_connector_auth_config

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_auth_config(connector_id="<id>", auth={
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

## update_connector_filters_sync_config

Update filter selections and sync settings without touching auth.<br><br>
<b>Use Case:</b><br>
Use this to change what data is synced or adjust sync schedule
without re-authenticating.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorFiltersSyncConfig" method="put" path="/connectors/{connectorId}/config/filters-sync" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_filters_sync_config(connector_id="<id>", sync={
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
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `connector_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `sync`                                                                                  | [Optional[models.ConnectorSyncConfig]](../../models/connectorsyncconfig.md)             | :heavy_minus_sign:                                                                      | Synchronization configuration for a connector instance                                  |
| `filters`                                                                               | [Optional[models.ConnectorFiltersConfig]](../../models/connectorfiltersconfig.md)       | :heavy_minus_sign:                                                                      | Filter configuration to control what data is synced (sync filters and indexing filters) |
| `base_url`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.UpdateConnectorFiltersSyncConfigResponse](../../models/updateconnectorfilterssyncconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |