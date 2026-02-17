# AuthenticationConfiguration

## Overview

### Available Operations

* [set_microsoft](#set_microsoft) - Configure Microsoft authentication
* [get_microsoft](#get_microsoft) - Get Microsoft authentication configuration
* [set_google](#set_google) - Configure Google authentication
* [get_google](#get_google) - Get Google authentication configuration
* [set_o_auth_config](#set_o_auth_config) - Configure generic OAuth provider

## set_microsoft

Set up Microsoft account as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setMicrosoftAuthConfig" method="post" path="/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.authentication_configuration.set_microsoft(client_id="12345678-1234-1234-1234-123456789abc", tenant_id="common")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client ID                                     | 12345678-1234-1234-1234-123456789abc                                |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Microsoft tenant ID                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_microsoft

Get Microsoft authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMicrosoftAuthConfig" method="get" path="/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.authentication_configuration.get_microsoft()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MicrosoftAuthConfig](../../models/microsoftauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_google

Set up Google OAuth as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setGoogleAuthConfig" method="post" path="/configurationManager/authConfig/google" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.authentication_configuration.set_google(client_id="123456789-abc.apps.googleusercontent.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Google OAuth client ID                                              | 123456789-abc.apps.googleusercontent.com                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_google

Get Google authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGoogleAuthConfig" method="get" path="/configurationManager/authConfig/google" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.authentication_configuration.get_google()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GoogleAuthConfig](../../models/googleauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_o_auth_config

Set up a custom OAuth 2.0 authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setOAuthConfig" method="post" path="/configurationManager/authConfig/oauth" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.authentication_configuration.set_o_auth_config(provider_name="Custom OAuth Provider", client_id="<id>", scope="openid profile email")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_name`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Display name for the OAuth provider                                 | Custom OAuth Provider                                               |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | OAuth client ID                                                     |                                                                     |
| `client_secret`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth client secret                                                 |                                                                     |
| `authorization_url`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Authorization endpoint URL                                          |                                                                     |
| `token_endpoint`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Token endpoint URL                                                  |                                                                     |
| `user_info_endpoint`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | User info endpoint URL                                              |                                                                     |
| `scope`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth scopes to request                                             | openid profile email                                                |
| `redirect_uri`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth redirect URI                                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |