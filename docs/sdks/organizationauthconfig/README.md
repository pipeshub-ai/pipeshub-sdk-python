# OrganizationAuthConfig

## Overview

### Available Operations

* [update_method](#update_method) - Update organization authentication methods

## update_method

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.organization_auth_config.update_method(auth_methods=[
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