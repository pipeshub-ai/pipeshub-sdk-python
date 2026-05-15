# OrganizationAuthConfig

## Overview

### Available Operations

* [get_auth_methods](#get_auth_methods) - Get organization authentication methods
* [update_auth_method](#update_auth_method) - Update organization authentication methods
* [set_up_auth_config](#set_up_auth_config) - Set up auth configuration

## get_auth_methods

Retrieve the configured authentication methods for the organization.

**Response Structure:**

Returns an array of authentication steps, each containing:
- `order`: Step number (1-3)
- `allowedMethods`: Array of methods allowed for that step

**Example Response:**

```json
{
  "authMethods": [
    { "order": 1, "allowedMethods": [{ "type": "password" }, { "type": "google" }] },
    { "order": 2, "allowedMethods": [{ "type": "otp" }] }
  ]
}
```

**Admin Access Required:** Only organization admins can view auth configuration.


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
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_auth_method

Update the authentication methods configuration for an organization.
This allows admins to configure single or multi-factor authentication.

**Validation Rules:**
- Minimum 1 step, maximum 3 steps
- Each step must have a unique order (1, 2, or 3)
- No duplicate methods within the same step
- No method can appear in multiple steps
- Each step must have at least one allowed method

**Available Methods:**
- `password`: Email/password authentication
- `otp`: One-time password via email
- `google`: Google OAuth 2.0
- `microsoft`: Microsoft OAuth 2.0
- `azureAd`: Azure Active Directory
- `samlSso`: SAML 2.0 Single Sign-On
- `oauth`: Generic OAuth 2.0 provider

**Example - Single Factor (Password or Google):**

```json
{
  "authMethod": [
    { "order": 1, "allowedMethods": [{ "type": "password" }, { "type": "google" }] }
  ]
}
```

**Example - Two Factor (Password + OTP):**

```json
{
  "authMethod": [
    { "order": 1, "allowedMethods": [{ "type": "password" }] },
    { "order": 2, "allowedMethods": [{ "type": "otp" }] }
  ]
}
```

**Admin Access Required:** Only organization admins can update auth configuration.


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

    res = pipeshub.organization_auth_config.update_auth_method(auth_method=[
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
| `auth_method`                                                       | List[[models.AuthStep](../../models/authstep.md)]                   | :heavy_check_mark:                                                  | Authentication steps to set for the organization (1-3 steps)        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateAuthMethodResponse](../../models/updateauthmethodresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_up_auth_config

Set up or initialize the organization's authentication configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="setUpAuthConfig" method="post" path="/orgAuthConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organization_auth_config.set_up_auth_config(contact_email="Buster_Waelchi@yahoo.com", registered_name="<value>", admin_full_name="<value>", send_email=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `contact_email`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Organization contact email                                          |
| `registered_name`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Organization registered name                                        |
| `admin_full_name`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Admin user full name                                                |
| `send_email`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether to send welcome email                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrgAuthConfigSetupResponse](../../models/orgauthconfigsetupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |