# AuthConfig

## Overview

### Available Operations

* [set_azure_ad](#set_azure_ad) - Configure Azure AD authentication
* [set_sso](#set_sso) - Configure SAML SSO authentication
* [get_sso](#get_sso) - Get SAML SSO configuration

## set_azure_ad

Set up Azure Active Directory as an authentication provider for user login.

### Example Usage

<!-- UsageSnippet language="python" operationID="setAzureAdAuthConfig" method="post" path="/configurationManager/authConfig/azureAd" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.auth_config.set_azure_ad(client_id="12345678-1234-1234-1234-123456789abc", tenant_id="common")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Azure AD application client ID                                      | 12345678-1234-1234-1234-123456789abc                                |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Azure AD tenant ID (use 'common' for multi-tenant)                  | common                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_sso

Set up SAML 2.0 Single Sign-On with your identity provider (Okta, OneLogin, etc.).

### Example Usage

<!-- UsageSnippet language="python" operationID="setSsoAuthConfig" method="post" path="/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.auth_config.set_sso(entry_point="https://idp.example.com/sso/saml", certificate="<value>", email_key="email")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entry_point`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Identity provider SSO URL                                           | https://idp.example.com/sso/saml                                    |
| `certificate`                                                       | *str*                                                               | :heavy_check_mark:                                                  | X.509 certificate for signature validation (PEM format)             |                                                                     |
| `email_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | SAML attribute name for user email                                  | email                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_sso

Get SAML SSO configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSsoAuthConfig" method="get" path="/configurationManager/authConfig/sso" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.auth_config.get_sso()

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