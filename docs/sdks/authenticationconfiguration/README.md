# AuthenticationConfiguration

## Overview

Configure authentication providers including Microsoft, Google OAuth, SAML SSO, and custom OAuth 2.0.

### Available Operations

* [set_microsoft_auth_config](#set_microsoft_auth_config) - Configure Microsoft authentication
* [get_microsoft_auth_config](#get_microsoft_auth_config) - Get Microsoft authentication configuration
* [set_google_auth_config](#set_google_auth_config) - Configure Google authentication
* [get_google_auth_config](#get_google_auth_config) - Get Google authentication configuration
* [set_sso_auth_config](#set_sso_auth_config) - Configure SAML SSO authentication
* [get_sso_auth_config](#get_sso_auth_config) - Get SAML SSO configuration
* [set_o_auth_config](#set_o_auth_config) - Configure generic OAuth provider
* [get_generic_o_auth_config](#get_generic_o_auth_config) - Get generic OAuth configuration

## set_microsoft_auth_config

Set up Microsoft account as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setMicrosoftAuthConfig" method="post" path="/api/v1/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.authentication_configuration.set_microsoft_auth_config(authority="https://login.microsoftonline.com/{tenantId}")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Microsoft application client ID                                     |                                                                     |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Microsoft tenant ID                                                 |                                                                     |
| `authority`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Microsoft authority URL                                             | https://login.microsoftonline.com/{tenantId}                        |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_microsoft_auth_config

Get Microsoft authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMicrosoftAuthConfig" method="get" path="/api/v1/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.authentication_configuration.get_microsoft_auth_config()

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

## set_google_auth_config

Set up Google OAuth as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setGoogleAuthConfig" method="post" path="/api/v1/configurationManager/authConfig/google" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.authentication_configuration.set_google_auth_config()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Google OAuth client ID                                              |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_google_auth_config

Get Google authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGoogleAuthConfig" method="get" path="/api/v1/configurationManager/authConfig/google" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.authentication_configuration.get_google_auth_config()

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

## set_sso_auth_config

Set up SAML 2.0 Single Sign-On with your identity provider (Okta, OneLogin, etc.).

### Example Usage

<!-- UsageSnippet language="python" operationID="setSsoAuthConfig" method="post" path="/api/v1/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.authentication_configuration.set_sso_auth_config()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `certificate`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | X.509 certificate for signature validation (PEM format)             |
| `entry_point`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Identity provider SSO URL                                           |
| `email_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | SAML attribute name for user email                                  |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_sso_auth_config

Get SAML SSO configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSsoAuthConfig" method="get" path="/api/v1/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.authentication_configuration.get_sso_auth_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SSOAuthConfig](../../models/ssoauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_o_auth_config

Set up a custom OAuth 2.0 authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setOAuthConfig" method="post" path="/api/v1/configurationManager/authConfig/oauth" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.authentication_configuration.set_o_auth_config(scope="openid email profile")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Display name for the OAuth provider                                 |
| `client_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth client ID                                                     |
| `client_secret`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth client secret                                                 |
| `authorization_url`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Authorization endpoint URL                                          |
| `token_endpoint`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Token endpoint URL                                                  |
| `user_info_endpoint`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | User info endpoint URL                                              |
| `scope`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth scopes to request                                             |
| `redirect_uri`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth redirect URI                                                  |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_generic_o_auth_config

Get generic OAuth configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenericOAuthConfig" method="get" path="/api/v1/configurationManager/authConfig/oauth" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.authentication_configuration.get_generic_o_auth_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenericOAuthConfig](../../models/genericoauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |