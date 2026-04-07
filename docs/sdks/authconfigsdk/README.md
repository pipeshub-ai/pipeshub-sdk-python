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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.auth_config.set_azure_ad(client_id="12345678-1234-1234-1234-123456789abc", tenant_id="common")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Azure AD application client ID                                      | 12345678-1234-1234-1234-123456789abc                                |
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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.auth_config.set_sso(entry_point="https://unwieldy-sprinkles.name", email_key="<value>", enable_jit=True, saml_platform="Okta")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entry_point`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Identity provider SSO URL                                           | https://idp.example.com/sso/saml                                    |
| `certificate`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | X.509 certificate for signature validation (PEM format)             |                                                                     |
| `email_key`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | SAML attribute name for user email                                  | email                                                               |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Enable Just-In-Time (JIT) user provisioning                         | true                                                                |
| `saml_platform`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Name of the SAML platform or provider (e.g., Okta, Azure AD)        | Okta                                                                |
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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.auth_config.get_sso()

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