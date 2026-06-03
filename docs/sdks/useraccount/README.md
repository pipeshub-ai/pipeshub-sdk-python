# UserAccount

## Overview

User authentication including multi-step MFA, password reset, OTP login, and token management

### Available Operations

* [init_auth](#init_auth) - Initialize authentication session
* [authenticate](#authenticate) - Authenticate user with credentials
* [refresh_token](#refresh_token) - Refresh access token
* [reset_password](#reset_password) - Reset password

## init_auth

Start a server-side authentication session and discover which sign-in methods are
configured for the organization. This is the first step in the multi-step login flow.

**Request body (optional)**

- You may omit the body, send an empty JSON object `{}`, or send `{ "email": "..." }`.
- `email` in the body is optional and kept for legacy reasons; omitting it does not prevent
  initialization. The web client typically calls this endpoint without a body and sends
  `email` on `/authenticate` instead.
- When provided, `email` is stored on the session for correlation with subsequent steps.

**Flow:**

1. Call this endpoint (optional JSON body as above).
2. Receive a session token in the `x-session-token` response header.
3. Send that token on subsequent `/authenticate` requests (`x-session-token` header).
4. Use `allowedMethods` and `authProviders` from the response to render the login UI.

**Session token**

- Returned as header `x-session-token`.
- Required for `/authenticate` (and related steps) until it expires.

**Multi-factor authentication**

If the organization has MFA, complete multiple authentication steps; each step may
return the next step's allowed methods.


### Example Usage

<!-- UsageSnippet language="python" operationID="initAuth" method="post" path="/userAccount/initAuth" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.init_auth(request={
        "email": "user@example.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.InitAuthRequest](../../models/initauthrequest.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InitAuthResponseResponse](../../models/initauthresponseresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400                         | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## authenticate

Authenticate a user using the specified method and credentials.
Requires a valid session token from `/initAuth`.

**Credential Formats by Method:**

- `password`: `{ "credentials": { "password": "your-password" } }`
- `otp`: `{ "credentials": { "otp": "123456" } }` (6-digit code, valid for 10 minutes)
- `google`: `{ "credentials": "google-id-token-string" }`
- `microsoft`: `{ "credentials": { "accessToken": "...", "idToken": "..." } }`
- `azureAd`: `{ "credentials": { "accessToken": "...", "idToken": "..." } }`
- `oauth`: `{ "credentials": { "accessToken": "...", "idToken": "..." } }`
- `samlSso`: Handled via redirect flow (use `/saml/signIn` instead)

**Multi-Step Response:**

If organization uses MFA, successful authentication returns:
- `status: "success"` with `nextStep` and `allowedMethods` for next step

**Fully Authenticated Response:**

After completing all steps:
- `message: "Fully authenticated"` with `accessToken` (1hr) and `refreshToken` (7d)

**Security:**

- Account locks after 5 consecutive failed attempts
- CAPTCHA may be required if enabled (pass `cf-turnstile-response`)


### Example Usage

<!-- UsageSnippet language="python" operationID="authenticate" method="post" path="/userAccount/authenticate" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.authenticate(x_session_token="<value>", method="oauth", credentials={
        "password": "o_5N_tt72qMx3WV",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `x_session_token`                                                    | *str*                                                                | :heavy_check_mark:                                                   | Session token received from `/initAuth` endpoint                     |
| `method`                                                             | [models.Method](../../models/method.md)                              | :heavy_check_mark:                                                   | Authentication method to use                                         |
| `credentials`                                                        | [models.Credentials](../../models/credentials.md)                    | :heavy_check_mark:                                                   | Credentials based on the authentication method                       |
| `email`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional email for verification (used with some OAuth methods)       |
| `cf_turnstile_response`                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Cloudflare Turnstile CAPTCHA token (optional, if CAPTCHA is enabled) |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.AuthenticateResponse](../../models/authenticateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404, 410          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## refresh_token

Get a new access token using a valid refresh token.

**Usage:**

- Pass the refresh token as a Bearer token in the Authorization header
- Returns a new access token and basic user information

**Token Lifetimes:**

- Access token: 24 hours (configurable via `ACCESS_TOKEN_EXPIRY` environment variable)
- Refresh token: 30 days (configurable via `REFRESH_TOKEN_EXPIRY` environment variable)

**Best Practices:**

- Call this endpoint before the access token expires
- Store the new access token and continue using it for authenticated requests
- If refresh fails with 401, redirect user to login flow


### Example Usage

<!-- UsageSnippet language="python" operationID="refreshToken" method="post" path="/userAccount/refresh/token" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.refresh_token(security=models.RefreshTokenSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.RefreshTokenSecurity](../../refreshtokensecurity.md)        | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RefreshTokenResponse](../../models/refreshtokenresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reset_password

Reset the password for the currently authenticated user.

**Overview:**

Allows a logged-in user to change their password by providing the current password and a new password.


### Example Usage

<!-- UsageSnippet language="python" operationID="resetPassword" method="post" path="/userAccount/password/reset" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_account.reset_password(current_password="fR5Alu28cPCa984", new_password="vcFGz9GLaOB88kV")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `current_password`                                                                     | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `new_password`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `cf_turnstile_response`                                                                | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Cloudflare Turnstile CAPTCHA token (required when Turnstile is configured server-side) |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[models.AuthenticatedPasswordResetResponse](../../models/authenticatedpasswordresetresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |