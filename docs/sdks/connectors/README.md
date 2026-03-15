# Connectors

## Overview

### Available Operations

* [resync](#resync) - Resync connector

## resync

Trigger a full resync of all records from a connector.<br><br>
<b>Overview:</b><br>
Fetches all content from the external source and updates local records. Use when you suspect data is out of sync.<br><br>
<b>Warning:</b> This can be resource-intensive for large connectors.


### Example Usage

<!-- UsageSnippet language="python" operationID="resyncConnector" method="post" path="/knowledgeBase/resync/connector" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connectors.resync(connector_name="GOOGLE_DRIVE", connector_id="<id>", full_sync=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Connector type name                                                 | GOOGLE_DRIVE                                                        |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID                                               | conn-abc123                                                         |
| `full_sync`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether to perform a full sync                                      |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ResyncConnectorResponse](../../models/resyncconnectorresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |