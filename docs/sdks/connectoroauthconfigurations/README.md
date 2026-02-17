# ConnectorOAuthConfigurations

## Overview

### Available Operations

* [set_share_point](#set_share_point) - Configure SharePoint connector
* [get_share_point](#get_share_point) - Get SharePoint configuration

## set_share_point

Set up Microsoft credentials for SharePoint connector.

### Example Usage

<!-- UsageSnippet language="python" operationID="setSharePointConfig" method="post" path="/configurationManager/connectors/sharepoint/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector_o_auth_configurations.set_share_point(client_id="<id>", client_secret="<value>", tenant_id="<id>", sharepoint_domain="<value>", has_admin_consent=False)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client ID                                     |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client secret                                 |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft/Azure tenant ID                                           |
| `sharepoint_domain`                                                 | *str*                                                               | :heavy_check_mark:                                                  | SharePoint domain (e.g., 'mycompany.sharepoint.com')                |
| `has_admin_consent`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether admin consent has been granted                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_share_point

Get SharePoint configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSharePointConfig" method="get" path="/configurationManager/connectors/sharepoint/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_o_auth_configurations.get_share_point()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SharePointConfig](../../models/sharepointconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |