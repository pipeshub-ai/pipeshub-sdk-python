# ConnectorConfigurations

## Overview

### Available Operations

* [get](#get) - Get connector configuration
* [update_filters_sync](#update_filters_sync) - Update filters and sync configuration

## get

Get the current configuration for a connector instance.<br><br>
<b>Security:</b><br>
Sensitive data (credentials, OAuth tokens) are redacted from the response.
Only admins can see partial credential information.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorConfig" method="get" path="/connectors/{connectorId}/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_configurations.get(connector_id="<id>")

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

## update_filters_sync

Update filter selections and sync settings without touching auth.<br><br>
<b>Use Case:</b><br>
Use this to change what data is synced or adjust sync schedule
without re-authenticating.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorFiltersSyncConfig" method="put" path="/connectors/{connectorId}/config/filters-sync" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_configurations.update_filters_sync(connector_id="<id>", sync={
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