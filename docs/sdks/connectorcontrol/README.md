# ConnectorControl

## Overview

Enable/disable connectors for sync or agent functionality

### Available Operations

* [toggle_connector](#toggle_connector) - Toggle connector sync or agent

## toggle_connector

Flip a connector's sync or agent use: each call turns it on when it is off and
off when it is on. Read <code>isActive</code> / <code>isAgentActive</code> first. Turning sync on
starts the first sync.<br><br>
<b>Toggle Types:</b><br>
<ul>
<li><code>sync</code> - data synchronization</li>
<li><code>agent</code> - use by AI agents</li>
</ul>
<b>Before Sync Can Be Turned On:</b><br>
<ul>
<li>The connector is configured (<code>isConfigured: true</code>)</li>
<li>OAuth connectors: sign-in has completed</li>
<li>The connection test against the source passes</li>
<li>For agent: the connector supports agents (<code>supportsAgent: true</code>)</li>
<li>Local FS: must be enabled from the owner device via the desktop app, which sends <code>deviceId</code> and <code>deviceName</code>. The first enable claims that device as owner.</li>
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
| `connector_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | Connector instance ID                                                           |
| `type`                                                                          | [models.ConnectorToggleRequestType](../../models/connectortogglerequesttype.md) | :heavy_check_mark:                                                              | 'sync' flips data synchronization; 'agent' flips use by agents                  |
| `full_sync`                                                                     | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | When turning sync on, start from scratch                                        |
| `device_id`                                                                     | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Local FS only                                                                   |
| `device_name`                                                                   | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Local FS only                                                                   |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ToggleConnectorResponse](../../models/toggleconnectorresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorResponse              | 400, 401, 403, 404                | application/json                  |
| errors.LocalFsDesktopRefusalError | 409                               | application/json                  |
| errors.ErrorResponse              | 409                               | application/json                  |
| errors.ErrorResponse              | 500                               | application/json                  |
| errors.PipeshubDefaultError       | 4XX, 5XX                          | \*/\*                             |