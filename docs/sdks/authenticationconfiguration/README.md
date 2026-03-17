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

    res = pipeshub.authentication_configuration.set_microsoft_auth_config(client_id="<id>", tenant_id="common", enable_jit=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Microsoft application client ID                                     |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Microsoft tenant ID                                                 |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetMicrosoftAuthConfigResponse](../../models/setmicrosoftauthconfigresponse.md)**

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

    res = pipeshub.authentication_configuration.set_google_auth_config(client_id="<id>", enable_jit=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Google OAuth client ID                                              |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetGoogleAuthConfigResponse](../../models/setgoogleauthconfigresponse.md)**

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

    res = pipeshub.authentication_configuration.set_sso_auth_config(certificate="<value>", entry_point="https://unwieldy-sprinkles.name", email_key="<value>", enable_jit=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `certificate`                                                       | *str*                                                               | :heavy_check_mark:                                                  | X.509 certificate for signature validation (PEM format)             |
| `entry_point`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identity provider SSO URL                                           |
| `email_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | SAML attribute name for user email                                  |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetSsoAuthConfigResponse](../../models/setssoauthconfigresponse.md)**

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

    res = pipeshub.authentication_configuration.set_o_auth_config(provider_name="<value>", client_id="<id>", client_secret="<value>", authorization_url="https://squeaky-ad.org", token_endpoint="https://rapid-cruelty.name/", user_info_endpoint="https://far-flung-habit.net", scope="openid email profile", redirect_uri="https://questionable-straw.biz", enable_jit=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_name`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Display name for the OAuth provider                                 |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | OAuth client ID                                                     |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | OAuth client secret                                                 |
| `authorization_url`                                                 | *str*                                                               | :heavy_check_mark:                                                  | Authorization endpoint URL                                          |
| `token_endpoint`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Token endpoint URL                                                  |
| `user_info_endpoint`                                                | *str*                                                               | :heavy_check_mark:                                                  | User info endpoint URL                                              |
| `scope`                                                             | *str*                                                               | :heavy_check_mark:                                                  | OAuth scopes to request                                             |
| `redirect_uri`                                                      | *str*                                                               | :heavy_check_mark:                                                  | OAuth redirect URI                                                  |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time user provisioning                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetOAuthConfigResponse](../../models/setoauthconfigresponse.md)**

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