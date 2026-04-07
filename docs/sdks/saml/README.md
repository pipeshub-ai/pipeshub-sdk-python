# Saml

## Overview

### Available Operations

* [sign_in](#sign_in) - Initiate SAML sign-in flow
* [callback](#callback) - SAML sign-in callback
* [update_app_config](#update_app_config) - Reload SAML application configuration (Internal)

## sign_in

Initiate SAML Single Sign-On authentication by redirecting to the Identity Provider (IDP).
<br><br>
<b>Usage:</b><br>
1. Call <code>/userAccount/initAuth</code> to get a session token<br>
2. If <code>samlSso</code> is in the allowed methods, redirect the user to this endpoint<br>
3. User authenticates with their IDP<br>
4. IDP redirects back to <code>/saml/signIn/callback</code> with SAML response<br>
5. Callback completes authentication and returns tokens
<br><br>
<b>Note:</b> This is a browser redirect endpoint, not a typical API call.
The user's browser should be redirected to this URL.
<br><br>
<b>Prerequisites:</b><br>
- Organization must have SAML SSO configured via <code>/saml/updateAppConfig</code><br>
- User must belong to an organization with SAML enabled


### Example Usage

<!-- UsageSnippet language="python" operationID="signInViaSAML" method="get" path="/saml/signIn" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.saml.sign_in(email="Daphney.Koss@hotmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `email`                                                                                                                          | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | User's email address                                                                                                             |
| `session_token`                                                                                                                  | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | Session token from `/userAccount/initAuth`. Optional but recommended<br/>for maintaining authentication state across the SAML flow.<br/> |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.SignInViaSAMLResponse](../../models/signinviasamlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## callback

Handles the callback from the SAML Identity Provider (IDP)
after successful user authentication.

This endpoint is invoked by the IDP and not directly by clients.

Flow:
1. IDP posts SAMLResponse and RelayState
2. Server validates the SAML assertion signature
3. Server extracts user identity
4. Server completes authentication
5. Redirects to frontend with authentication result

RelayState contains the session token or state used to resume
the authentication process.


### Example Usage

<!-- UsageSnippet language="python" operationID="samlSignInCallback" method="post" path="/saml/signIn/callback" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.saml.callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.SamlSignInCallbackRequest](../../models/samlsignincallbackrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.SamlSignInCallbackResponse](../../models/samlsignincallbackresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400, 401, 404               | application/json            |
| errors.AuthError            | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_app_config

Internal endpoint to reload SAML configuration from the configuration manager.
This is called by other services when SAML settings are updated.<br><br>
<b>Purpose:</b><br>
When SAML configuration is updated in the Configuration Manager, this endpoint
is called to reload the settings into the authentication service without restart.<br><br>
<b>Effects:</b><br>
<ul>
<li>Reloads AppConfig from configuration files</li>
<li>Rebinds authentication controllers with new config</li>
<li>Updates SAML passport strategy settings</li>
</ul>
<b>Note:</b> This is an internal service-to-service endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateSamlAppConfig" method="post" path="/saml/updateAppConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub() as pipeshub:

    res = pipeshub.saml.update_app_config(security=models.UpdateSamlAppConfigSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [models.UpdateSamlAppConfigSecurity](../../updatesamlappconfigsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.UpdateSamlAppConfigResponse](../../models/updatesamlappconfigresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.UpdateSamlAppConfigBadRequestError | 400                                       | application/json                          |
| errors.PipeshubDefaultError               | 4XX, 5XX                                  | \*/\*                                     |