# OrganizationAuthConfig

## Overview

Admin configuration of authentication methods including MFA steps and allowed providers

### Available Operations

* [get_auth_methods](#get_auth_methods) - Get organization authentication methods
* [update_auth_method](#update_auth_method) - Update organization authentication methods
* [~~set_up_auth_config~~](#set_up_auth_config) - Set up auth configuration :warning: **Deprecated**

## get_auth_methods

Retrieve the configured authentication methods for the organization.
<br><br>
<b>Response Structure:</b><br>
Returns an array of authentication steps, each containing:<br>
- <code>order</code>: Step number (1-3)<br>
- <code>allowedMethods</code>: Array of methods allowed for that step
<br><br>
<b>Example Response:</b><br>
<pre>
{
  "authMethods": [
    { "order": 1, "allowedMethods": [{ "type": "password" }, { "type": "google" }] },
    { "order": 2, "allowedMethods": [{ "type": "otp" }] }
  ]
}
</pre>
<br>
<b>Admin Access Required:</b> Only organization admins can view auth configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAuthMethods" method="get" path="/orgAuthConfig/authMethods" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organization_auth_config.get_auth_methods()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuthConfig](../../models/authconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_auth_method

Update the authentication methods configuration for an organization.
This allows admins to configure single or multi-factor authentication.
<br><br>
<b>Validation Rules:</b><br>
- Minimum 1 step, maximum 3 steps<br>
- Each step must have a unique order (1, 2, or 3)<br>
- No duplicate methods within the same step<br>
- No method can appear in multiple steps<br>
- Each step must have at least one allowed method
<br><br>
<b>Available Methods:</b><br>
- <code>password</code>: Email/password authentication<br>
- <code>otp</code>: One-time password via email<br>
- <code>google</code>: Google OAuth 2.0<br>
- <code>microsoft</code>: Microsoft OAuth 2.0<br>
- <code>azureAd</code>: Azure Active Directory<br>
- <code>samlSso</code>: SAML 2.0 Single Sign-On<br>
- <code>oauth</code>: Generic OAuth 2.0 provider
<br><br>
<b>Example - Single Factor (Password or Google):</b><br>
<pre>
{
  "authMethods": [
    { "order": 1, "allowedMethods": [{ "type": "password" }, { "type": "google" }] }
  ]
}
</pre>
<br>
<b>Example - Two Factor (Password + OTP):</b><br>
<pre>
{
  "authMethods": [
    { "order": 1, "allowedMethods": [{ "type": "password" }] },
    { "order": 2, "allowedMethods": [{ "type": "otp" }] }
  ]
}
</pre>
<br>
<b>Admin Access Required:</b> Only organization admins can update auth configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateAuthMethod" method="post" path="/orgAuthConfig/updateAuthMethod" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organization_auth_config.update_auth_method(auth_methods=[
        {
            "order": 195644,
            "allowed_methods": [
                {
                    "type": "samlSso",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `auth_methods`                                                      | List[[models.AuthStep](../../models/authstep.md)]                   | :heavy_check_mark:                                                  | List of authentication steps in order                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateAuthMethodResponse](../../models/updateauthmethodresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~set_up_auth_config~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Set up or initialize the organization's authentication configuration.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="setUpAuthConfig" method="post" path="/orgAuthConfig/" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organization_auth_config.set_up_auth_config(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.SetUpAuthConfigRequest](../../models/setupauthconfigrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SetUpAuthConfigResponse](../../models/setupauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |