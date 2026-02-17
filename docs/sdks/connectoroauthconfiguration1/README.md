# ConnectorOAuthConfiguration

## Overview

### Available Operations

* [create_google_workspace_credentials](#create_google_workspace_credentials) - Upload Google Workspace credentials
* [set_google_workspace](#set_google_workspace) - Configure Google Workspace OAuth
* [get_atlassian_config](#get_atlassian_config) - Get Atlassian OAuth configuration
* [get_one_drive_config](#get_one_drive_config) - Get OneDrive configuration

## create_google_workspace_credentials

Upload Google Workspace credentials (service account JSON for business, or OAuth tokens for individual users). File must be valid JSON.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGoogleWorkspaceCredentials" method="post" path="/configurationManager/connectors/googleWorkspaceCredentials" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector_o_auth_configuration.create_google_workspace_credentials(user_type="individual", google_workspace_credentials={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_type`                                                                                                                                     | [models.CreateGoogleWorkspaceCredentialsUserType](../../models/creategoogleworkspacecredentialsusertype.md)                                     | :heavy_check_mark:                                                                                                                              | Type: 'business' for service account, 'individual' for user OAuth                                                                               |
| `google_workspace_credentials`                                                                                                                  | [models.CreateGoogleWorkspaceCredentialsGoogleWorkspaceCredentials](../../models/creategoogleworkspacecredentialsgoogleworkspacecredentials.md) | :heavy_check_mark:                                                                                                                              | JSON credentials file                                                                                                                           |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_google_workspace

Set up OAuth credentials for Google Workspace connector. Required for user authentication with Google Drive, Gmail, etc.

### Example Usage

<!-- UsageSnippet language="python" operationID="setGoogleWorkspaceOauthConfig" method="post" path="/configurationManager/connectors/googleWorkspaceOauthConfig" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector_o_auth_configuration.set_google_workspace(client_id="<id>", client_secret="<value>", enable_real_time_updates=False)

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `client_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Google OAuth client ID                                                |
| `client_secret`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | Google OAuth client secret                                            |
| `enable_real_time_updates`                                            | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable Google Pub/Sub for real-time updates                           |
| `topic_name`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Google Pub/Sub topic name (required if enableRealTimeUpdates is true) |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_atlassian_config

Get Atlassian OAuth configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtlassianConfig" method="get" path="/configurationManager/connectors/atlassian/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_o_auth_configuration.get_atlassian_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AtlassianConfig](../../models/atlassianconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_one_drive_config

Get OneDrive configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOneDriveConfig" method="get" path="/configurationManager/connectors/onedrive/config" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_o_auth_configuration.get_one_drive_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OneDriveConfig](../../models/onedriveconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |