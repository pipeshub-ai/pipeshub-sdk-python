# ConnectorControl

## Overview

Enable/disable connectors for sync or agent functionality

### Available Operations

* [toggle_connector](#toggle_connector) - Toggle connector sync or agent

## toggle_connector

Enable or disable a connector for sync or agent functionality.<br><br>
<b>Toggle Types:</b><br>
<ul>
<li><code>sync</code> - Enable/disable data synchronization</li>
<li><code>agent</code> - Enable/disable AI agent integration</li>
</ul>
<b>Prerequisites for Enabling:</b><br>
<ul>
<li>Connector must be configured (<code>isConfigured: true</code>)</li>
<li>For OAuth connectors: Must be authenticated (<code>isAuthenticated: true</code>)</li>
<li>For agent: Connector must support agent (<code>supportsAgent: true</code>)</li>
</ul>
<b>Permissions:</b><br>
<ul>
<li>Team scope: Requires admin</li>
<li>Personal scope: Only creator can toggle</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="toggleConnector" method="post" path="/connectors/{connectorId}/toggle" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_control.toggle_connector(connector_id="<id>", type_="sync")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `connector_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `type`                                                                          | [models.ConnectorToggleRequestType](../../models/connectortogglerequesttype.md) | :heavy_check_mark:                                                              | Toggle type: 'sync' for data synchronization, 'agent' for AI agent integration  |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ToggleConnectorResponse](../../models/toggleconnectorresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |