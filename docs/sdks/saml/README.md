# Saml

## Overview

SAML 2.0 Single Sign-On integration with enterprise Identity Providers

### Available Operations

* [sign_in_via_saml](#sign_in_via_saml) - Initiate SAML sign-in flow
* [~~saml_sign_in_callback~~](#saml_sign_in_callback) - SAML sign-in callback :warning: **Deprecated**

## sign_in_via_saml

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

    res = pipeshub.saml.sign_in_via_saml(email="Daphney.Koss@hotmail.com")

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

## ~~saml_sign_in_callback~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Handle the SAML Identity Provider callback after user authentication. This endpoint receives the SAML assertion from the IdP.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="samlSignInCallback" method="post" path="/saml/signIn/callback" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    pipeshub.saml.saml_sign_in_callback()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.SamlSignInCallbackRequest](../../models/samlsignincallbackrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.SamlSignInCallbackBadRequestError | 400                                      | application/json                         |
| errors.UnauthorizedError                 | 401                                      | application/json                         |
| errors.PipeshubDefaultError              | 4XX, 5XX                                 | \*/\*                                    |