# AuthenticationConfiguration

## Overview

Configure authentication providers including Azure AD, Microsoft, Google OAuth, SAML SSO, and custom OAuth 2.0.

### Available Operations

* [set_azure_ad_auth_config](#set_azure_ad_auth_config) - Configure Azure AD authentication
* [get_azure_ad_auth_config](#get_azure_ad_auth_config) - Get Azure AD configuration
* [set_microsoft_auth_config](#set_microsoft_auth_config) - Configure Microsoft authentication
* [get_microsoft_auth_config](#get_microsoft_auth_config) - Get Microsoft authentication configuration
* [set_google_auth_config](#set_google_auth_config) - Configure Google authentication
* [get_google_auth_config](#get_google_auth_config) - Get Google authentication configuration
* [set_sso_auth_config](#set_sso_auth_config) - Configure SAML SSO authentication
* [get_sso_auth_config](#get_sso_auth_config) - Get SAML SSO configuration
* [set_o_auth_config](#set_o_auth_config) - Configure generic OAuth provider
* [get_generic_o_auth_config](#get_generic_o_auth_config) - Get generic OAuth configuration

## set_azure_ad_auth_config

Set up Azure Active Directory as an authentication provider for user login.

### Example Usage

<!-- UsageSnippet language="python" operationID="setAzureAdAuthConfig" method="post" path="/configurationManager/authConfig/azureAd" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.authentication_configuration.set_azure_ad_auth_config(security=models.SetAzureAdAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), client_id="12345678-1234-1234-1234-123456789abc", tenant_id="common")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.SetAzureAdAuthConfigSecurity](../../models/setazureadauthconfigsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `client_id`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | Azure AD application client ID                                                      | 12345678-1234-1234-1234-123456789abc                                                |
| `tenant_id`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Azure AD tenant ID (use 'common' for multi-tenant)                                  | common                                                                              |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_azure_ad_auth_config

Retrieve Azure AD authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAzureAdAuthConfig" method="get" path="/configurationManager/authConfig/azureAd" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.authentication_configuration.get_azure_ad_auth_config(security=models.GetAzureAdAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [models.GetAzureAdAuthConfigSecurity](../../getazureadauthconfigsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.AzureAdAuthConfig](../../models/azureadauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_microsoft_auth_config

Set up Microsoft account as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setMicrosoftAuthConfig" method="post" path="/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.authentication_configuration.set_microsoft_auth_config(security=models.SetMicrosoftAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), client_id="12345678-1234-1234-1234-123456789abc", tenant_id="common")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.SetMicrosoftAuthConfigSecurity](../../models/setmicrosoftauthconfigsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `client_id`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | Microsoft application client ID                                                         | 12345678-1234-1234-1234-123456789abc                                                    |
| `tenant_id`                                                                             | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Microsoft tenant ID                                                                     |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_microsoft_auth_config

Get Microsoft authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMicrosoftAuthConfig" method="get" path="/configurationManager/authConfig/microsoft" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.authentication_configuration.get_microsoft_auth_config(security=models.GetMicrosoftAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [models.GetMicrosoftAuthConfigSecurity](../../getmicrosoftauthconfigsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[models.MicrosoftAuthConfig](../../models/microsoftauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_google_auth_config

Set up Google OAuth as an authentication provider.

### Example Usage

<!-- UsageSnippet language="python" operationID="setGoogleAuthConfig" method="post" path="/configurationManager/authConfig/google" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.authentication_configuration.set_google_auth_config(security=models.SetGoogleAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), client_id="123456789-abc.apps.googleusercontent.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.SetGoogleAuthConfigSecurity](../../models/setgoogleauthconfigsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |                                                                                   |
| `client_id`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | Google OAuth client ID                                                            | 123456789-abc.apps.googleusercontent.com                                          |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_google_auth_config

Get Google authentication configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGoogleAuthConfig" method="get" path="/configurationManager/authConfig/google" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.authentication_configuration.get_google_auth_config(security=models.GetGoogleAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [models.GetGoogleAuthConfigSecurity](../../getgoogleauthconfigsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.GoogleAuthConfig](../../models/googleauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_sso_auth_config

Set up SAML 2.0 Single Sign-On with your identity provider (Okta, OneLogin, etc.).

### Example Usage

<!-- UsageSnippet language="python" operationID="setSsoAuthConfig" method="post" path="/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.authentication_configuration.set_sso_auth_config(security=models.SetSsoAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), entry_point="https://idp.example.com/sso/saml", certificate="<value>", email_key="email")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.SetSsoAuthConfigSecurity](../../models/setssoauthconfigsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `entry_point`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | Identity provider SSO URL                                                   | https://idp.example.com/sso/saml                                            |
| `certificate`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | X.509 certificate for signature validation (PEM format)                     |                                                                             |
| `email_key`                                                                 | *str*                                                                       | :heavy_check_mark:                                                          | SAML attribute name for user email                                          | email                                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_sso_auth_config

Get SAML SSO configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSsoAuthConfig" method="get" path="/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.authentication_configuration.get_sso_auth_config(security=models.GetSsoAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `security`                                                           | [models.GetSsoAuthConfigSecurity](../../getssoauthconfigsecurity.md) | :heavy_check_mark:                                                   | The security requirements to use for the request.                    |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.SSOAuthConfig](../../models/ssoauthconfig.md)**

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.authentication_configuration.set_o_auth_config(security=models.SetOAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), provider_name="Custom OAuth Provider", client_id="<id>", scope="openid profile email")

    # Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.SetOAuthConfigSecurity](../../models/setoauthconfigsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `provider_name`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | Display name for the OAuth provider                                     | Custom OAuth Provider                                                   |
| `client_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | OAuth client ID                                                         |                                                                         |
| `client_secret`                                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | OAuth client secret                                                     |                                                                         |
| `authorization_url`                                                     | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Authorization endpoint URL                                              |                                                                         |
| `token_endpoint`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Token endpoint URL                                                      |                                                                         |
| `user_info_endpoint`                                                    | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | User info endpoint URL                                                  |                                                                         |
| `scope`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | OAuth scopes to request                                                 | openid profile email                                                    |
| `redirect_uri`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | OAuth redirect URI                                                      |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_generic_o_auth_config

Get generic OAuth configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenericOAuthConfig" method="get" path="/configurationManager/authConfig/oauth" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.authentication_configuration.get_generic_o_auth_config(security=models.GetGenericOAuthConfigSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [models.GetGenericOAuthConfigSecurity](../../getgenericoauthconfigsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.GenericOAuthConfig](../../models/genericoauthconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |