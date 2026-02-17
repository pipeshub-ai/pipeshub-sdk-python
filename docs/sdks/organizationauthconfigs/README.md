# OrganizationAuthConfigs

## Overview

### Available Operations

* [create](#create) - Create organization authentication configuration
* [get_methods](#get_methods) - Get organization authentication methods

## create

Create initial organization authentication configuration during onboarding.
This endpoint creates a new organization with admin user and default auth settings.
<br><br>
<b>Note:</b> This is typically called during the initial setup process.


### Example Usage

<!-- UsageSnippet language="python" operationID="createOrgAuthConfig" method="post" path="/orgAuthConfig/" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.organization_auth_configs.create(contact_email="Tiana.Muller@hotmail.com", registered_name="<value>", admin_full_name="<value>", send_email=False)

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

**[models.CreateOrgAuthConfigResponse](../../models/createorgauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_methods

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.organization_auth_configs.get_methods()

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