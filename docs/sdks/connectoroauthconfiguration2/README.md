# ConnectorOauthConfiguration

## Overview

### Available Operations

* [get_google_workspace](#get_google_workspace) - Get Google Workspace OAuth configuration
* [set_atlassian_config](#set_atlassian_config) - Configure Atlassian OAuth
* [set_one_drive_config](#set_one_drive_config) - Configure OneDrive connector

## get_google_workspace

Get Google Workspace OAuth configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGoogleWorkspaceOauthConfig" method="get" path="/configurationManager/connectors/googleWorkspaceOauthConfig" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_oauth_configuration.get_google_workspace()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GoogleWorkspaceOAuthConfig](../../models/googleworkspaceoauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_atlassian_config

Set up OAuth credentials for Atlassian (Confluence/Jira) connector.

### Example Usage

<!-- UsageSnippet language="python" operationID="setAtlassianConfig" method="post" path="/configurationManager/connectors/atlassian/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector_oauth_configuration.set_atlassian_config(client_id="<id>", client_secret="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Atlassian OAuth client ID                                           |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Atlassian OAuth client secret                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_one_drive_config

Set up Microsoft credentials for OneDrive connector.

### Example Usage

<!-- UsageSnippet language="python" operationID="setOneDriveConfig" method="post" path="/configurationManager/connectors/onedrive/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector_oauth_configuration.set_one_drive_config(client_id="<id>", client_secret="<value>", tenant_id="<id>", has_admin_consent=False)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client ID                                     |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client secret                                 |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft/Azure tenant ID                                           |
| `has_admin_consent`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether admin consent has been granted                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |