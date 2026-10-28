# UserAccount

## Overview

User authentication including multi-step MFA, password reset, OTP login, and token management

### Available Operations

* [init_auth](#init_auth) - Initialize authentication session
* [authenticate](#authenticate) - Authenticate user with credentials
* [refresh_token](#refresh_token) - Refresh access token
* [get_password_status](#get_password_status) - Get password status
* [send_password_setup_email](#send_password_setup_email) - Email a link to set a first password
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

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorResponse          | 400                           | application/json              |
| errors.RateLimitErrorResponse | 429                           | application/json              |
| errors.ErrorResponse          | 500                           | application/json              |
| errors.PipeshubDefaultError   | 4XX, 5XX                      | \*/\*                         |

## authenticate

Authenticate a user using the specified method and credentials.
Requires a valid session token from `/initAuth`.

**Credential Formats by Method:**

- `password`: `{ "credentials": { "password": "your-password" } }`
- `otp`: `{ "credentials": { "otp": "123456" } }` (6-digit code, valid for 10 minutes)
- `google`: `{ "credentials": "google-id-token-string" }`. The object form
  `{ "credentials": { "credential": "..." } }` passes the first token check, but by code
  reading the second check is handed the whole object, so it ends in `500`
- `microsoft`: `{ "credentials": { "idToken": "..." } }` (only `idToken` is read)

SAML (`samlSso`), generic OAuth (`oauth`) and Azure AD (`azureAd`) sign-in were removed in 1.0;
this endpoint answers `400` for them. Azure AD accounts sign in with `microsoft`.

**Multi-Step Response:**

If organization uses MFA, successful authentication returns:
- `status: "success"` with `nextStep` and `allowedMethods` for next step

**Fully Authenticated Response:**

After completing all steps:
- `message: "Fully authenticated"` with `accessToken` (1hr) and `refreshToken` (7d)

**Security:**

- Account locks for 24 hours after 10 consecutive failed attempts, and the owner is
  sent an email saying so. While it is locked, sign-in is refused with the same answer
  as a wrong password or code, even when the password or code is right
- CAPTCHA may be required if enabled (pass `cf-turnstile-response`)
- An email with no account gets the same status and message as a real account given
  a wrong password (`400`) or a wrong, missing or expired sign-in code (`401`)
- The session token is single-use for the final step: once tokens are returned the
  session is gone, and sending it again answers `401`

**Order of checks:** the session token is checked before the body, so a request
without a valid `x-session-token` answers `401` whatever its body holds.


### Example Usage

<!-- UsageSnippet language="python" operationID="authenticate" method="post" path="/userAccount/authenticate" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.authenticate(x_session_token="<value>", method="microsoft", credentials={
        "password": "o_5N_tt72qMx3WV",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_session_token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Session token received from `/initAuth` endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `method`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [models.Method](../../models/method.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Authentication method to use. It must be one the session's current step allows;<br/>any other value, known or not, is answered `400`.<br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| `credentials`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [models.Credentials](../../models/credentials.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Credentials based on the authentication method; the shape each method needs is<br/>listed above. The validator only checks that this is a non-empty string or an<br/>object whose `password`, `otp`, `token`, `code`, `accessToken` and `idToken`,<br/>when present, are strings; other fields of the object are passed through. An<br/>object without the field its method needs is refused later as a failed sign-in,<br/>not as a validation error: `microsoft` without `idToken` answers `400`, and a Google<br/>token that is not a JWT answers `500`.<br/> |
| `email`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The account's email. Used when the session was started without one<br/>(`/initAuth` with no `email`); when neither carries an email, password and<br/>code sign-in answer `500`. Ignored by the external-provider methods, which<br/>take the email from the provider.<br/>                                                                                                                                                                                                                                                          |
| `cf_turnstile_response`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Cloudflare Turnstile CAPTCHA token (optional, if CAPTCHA is enabled)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Response

**[models.AuthenticateResponse](../../models/authenticateresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorResponse          | 400, 401                      | application/json              |
| errors.RateLimitErrorResponse | 429                           | application/json              |
| errors.ErrorResponse          | 500                           | application/json              |
| errors.PipeshubDefaultError   | 4XX, 5XX                      | \*/\*                         |

## refresh_token

Get a new access token using a valid refresh token.

**Usage:**

- Pass the refresh token as a Bearer token in the Authorization header
- Returns a new access token and basic user information
- The request body and query string are not read

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
| errors.ErrorResponse        | 400, 401                    | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_password_status

Returns whether the authenticated user has a password set. Users who signed in only through SSO do not.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPasswordStatus" method="get" path="/userAccount/password/status" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_account.get_password_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPasswordStatusResponse](../../models/getpasswordstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## send_password_setup_email

Sends the authenticated user a single-use link, to the email on their account, for setting a first password.
For users who have no password yet, for example those who signed in with Google. Users who already have one change it with `POST /userAccount/password/reset`.


### Example Usage

<!-- UsageSnippet language="python" operationID="sendPasswordSetupEmail" method="post" path="/userAccount/password/setup/email" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_account.send_password_setup_email()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SendPasswordSetupEmailResponse](../../models/sendpasswordsetupemailresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 404, 429          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reset_password

Reset the password for the currently authenticated user.

**Overview:**

Allows a logged-in user to change their password by providing the current password and a new password.

**Order of checks:** the access token is read before the body, so a request without
an `Authorization` header answers `400` whatever its body holds. Body fields other
than the three below are dropped by the validator, and the query string is not read.

**Effect on sessions:** the change ends refresh tokens issued before it. The response
carries a new access token.


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

| Parameter                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `current_password`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                  | The password the account has now. The validator treats it as optional; the handler then refuses a missing or empty value with `400`.                                                                                                                |
| `new_password`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                  | The new password: at least 8 characters with an uppercase letter, a<br/>lowercase letter, a digit and one of `#?!@$%^&*-`, at most 72 bytes, and<br/>different from the current one. A value that breaks these rules is<br/>refused by the handler with `400`.<br/> |
| `cf_turnstile_response`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                  | Cloudflare Turnstile CAPTCHA token (required when Turnstile is configured server-side)                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                 |

### Response

**[models.AuthenticatedPasswordResetResponse](../../models/authenticatedpasswordresetresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorResponse          | 400, 401, 404                 | application/json              |
| errors.RateLimitErrorResponse | 429                           | application/json              |
| errors.ErrorResponse          | 500                           | application/json              |
| errors.PipeshubDefaultError   | 4XX, 5XX                      | \*/\*                         |