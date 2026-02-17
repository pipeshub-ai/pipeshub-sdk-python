# UserAccount

## Overview

### Available Operations

* [init_auth](#init_auth) - Initialize authentication session
* [authenticate](#authenticate) - Authenticate user with credentials
* [generate_otp](#generate_otp) - Generate and send OTP for login
* [reset_password](#reset_password) - Reset password (authenticated user)
* [forgot_password](#forgot_password) - Request password reset email
* [reset_password_token](#reset_password_token) - Reset password with email token
* [check_password_set](#check_password_set) - Check if user has password set (Internal)
* [refresh](#refresh) - Refresh access token
* [logout](#logout) - Logout current session

## init_auth

Initialize an authentication session for a user by email address.
This is the first step in the multi-step authentication flow.
<br><br>
<b>Flow:</b><br>
1. Call this endpoint with the user's email<br>
2. Receive a session token in the <code>x-session-token</code> response header<br>
3. Use the session token in subsequent <code>/authenticate</code> calls<br>
4. The response includes <code>allowedMethods</code> for the first authentication step
<br><br>
<b>Session Token:</b><br>
- Stored in response header <code>x-session-token</code><br>
- Required for all subsequent authentication requests<br>
- Expires after a configured timeout period
<br><br>
<b>Multi-Factor Authentication:</b><br>
If the organization has MFA configured, you'll need to complete multiple
authentication steps. Each step completion returns the next step's allowed methods.


### Example Usage

<!-- UsageSnippet language="python" operationID="initAuth" method="post" path="/userAccount/initAuth" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | User email address (RFC 5321 compliant)                             | user@example.com                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.InitAuthResponseResponse](../../models/initauthresponseresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400, 403, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## authenticate

Authenticate a user using the specified method and credentials.
Requires a valid session token from <code>/initAuth</code>.
<br><br>
<b>Credential Formats by Method:</b><br>
- <code>password</code>: <code>{ "credentials": { "password": "your-password" } }</code><br>
- <code>otp</code>: <code>{ "credentials": { "otp": "123456" } }</code> (6-digit code, valid for 10 minutes)<br>
- <code>google</code>: <code>{ "credentials": "google-id-token-string" }</code><br>
- <code>microsoft</code>: <code>{ "credentials": { "accessToken": "...", "idToken": "..." } }</code><br>
- <code>azureAd</code>: <code>{ "credentials": { "accessToken": "...", "idToken": "..." } }</code><br>
- <code>oauth</code>: <code>{ "credentials": { "accessToken": "...", "idToken": "..." } }</code><br>
- <code>samlSso</code>: Handled via redirect flow (use <code>/saml/signIn</code> instead)
<br><br>
<b>Multi-Step Response:</b><br>
If organization uses MFA, successful authentication returns:<br>
- <code>status: "success"</code> with <code>nextStep</code> and <code>allowedMethods</code> for next step
<br><br>
<b>Fully Authenticated Response:</b><br>
After completing all steps:<br>
- <code>message: "Fully authenticated"</code> with <code>accessToken</code> (1hr) and <code>refreshToken</code> (7d)
<br><br>
<b>Security:</b><br>
- Account locks after 5 consecutive failed attempts<br>
- CAPTCHA may be required if enabled (pass <code>cf-turnstile-response</code>)


### Example Usage

<!-- UsageSnippet language="python" operationID="authenticate" method="post" path="/userAccount/authenticate" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.authenticate(x_session_token="<value>", method="oauth", credentials={
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
| errors.AuthError            | 400, 401, 403, 404, 410     | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## generate_otp

Generate and send a 6-digit one-time password (OTP) to the user's email.
Use this endpoint before authenticating with the <code>otp</code> method.
<br><br>
<b>OTP Details:</b><br>
- 6 digits numeric code<br>
- Valid for <b>10 minutes</b> after generation<br>
- Sent to user's registered email address
<br><br>
<b>Rate Limiting:</b><br>
- Multiple OTP requests may be rate-limited<br>
- Wait for the current OTP to expire before requesting a new one
<br><br>
<b>CAPTCHA:</b><br>
If Cloudflare Turnstile is enabled, include <code>cf-turnstile-response</code> in the request body.


### Example Usage

<!-- UsageSnippet language="python" operationID="generateLoginOtp" method="post" path="/userAccount/login/otp/generate" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.generate_otp(email="Garland.Sipes42@hotmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Email address to send OTP to                                        |
| `cf_turnstile_response`                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cloudflare Turnstile CAPTCHA token (optional)                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenerateLoginOtpResponse](../../models/generateloginotpresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400, 403, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reset_password

Reset password for an authenticated user. Requires the current password for verification.
<br><br>
<b>Password Requirements:</b><br>
- Minimum 8 characters<br>
- At least 1 uppercase letter (A-Z)<br>
- At least 1 lowercase letter (a-z)<br>
- At least 1 number (0-9)<br>
- At least 1 special character (#?!@$%^&*-)
<br><br>
<b>Security Notes:</b><br>
- A new access token is returned (old tokens are invalidated)<br>
- CAPTCHA may be required if enabled (pass <code>cf-turnstile-response</code>)


### Example Usage

<!-- UsageSnippet language="python" operationID="resetPassword" method="post" path="/userAccount/password/reset" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.user_account.reset_password(current_password="fR5Alu28cPCa984", new_password="vcFGz9GLaOB88kV")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                               | Type                                                                                                                                                                                                    | Required                                                                                                                                                                                                | Description                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `current_password`                                                                                                                                                                                      | *str*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | Current password for verification                                                                                                                                                                       |
| `new_password`                                                                                                                                                                                          | *str*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | New password. Must meet the following requirements:<br/>- Minimum 8 characters<br/>- At least 1 uppercase letter<br/>- At least 1 lowercase letter<br/>- At least 1 number<br/>- At least 1 special character (#?!@$%^&*-)<br/> |
| `cf_turnstile_response`                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                      | Cloudflare Turnstile CAPTCHA token (optional)                                                                                                                                                           |
| `retries`                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                     |

### Response

**[models.PasswordResetResponse](../../models/passwordresetresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## forgot_password

Send a password reset link to the user's email.
The link contains a time-limited token that can be used to reset the password.
<br><br>
<b>Note:</b> This endpoint always returns 200 even if the email doesn't exist (to prevent email enumeration).


### Example Usage

<!-- UsageSnippet language="python" operationID="forgotPassword" method="post" path="/userAccount/password/forgot" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.forgot_password(email="Barton.Gutkowski68@yahoo.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Email address to send reset link to                                 |
| `cf_turnstile_response`                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cloudflare Turnstile CAPTCHA token (optional)                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ForgotPasswordResponse](../../models/forgotpasswordresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reset_password_token

Reset password using a token received via email from the forgot password flow.
<br><br>
<b>Password Requirements:</b><br>
- Minimum 8 characters<br>
- At least 1 uppercase letter<br>
- At least 1 lowercase letter<br>
- At least 1 number<br>
- At least 1 special character (#?!@$%^&*-)
<br><br>
<b>Security Notes:</b><br>
- Token is single-use and expires after a set time<br>
- A new access token is returned upon successful reset


### Example Usage

<!-- UsageSnippet language="python" operationID="resetPasswordWithToken" method="post" path="/userAccount/password/reset/token" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.reset_password_token(security=models.ResetPasswordWithTokenSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), password="H9GEHoL829GXj06")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.ResetPasswordWithTokenSecurity](../../models/resetpasswordwithtokensecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `password`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | New password (must meet password requirements)<br/>                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.PasswordResetResponse](../../models/passwordresetresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## check_password_set

Internal endpoint to check if a user has a password configured.
Used by other services to determine authentication capabilities.
<br><br>
<b>Note:</b> This is an internal service-to-service endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="checkPasswordStatus" method="get" path="/userAccount/internal/password/check" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.check_password_set(security=models.CheckPasswordStatusSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [models.CheckPasswordStatusSecurity](../../checkpasswordstatussecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.CheckPasswordStatusResponse](../../models/checkpasswordstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## refresh

Get a new access token using a valid refresh token.
<br><br>
<b>Usage:</b><br>
- Pass the refresh token as a Bearer token in the Authorization header<br>
- Returns a new access token (1 hour expiry) and basic user information
<br><br>
<b>Token Lifetimes:</b><br>
- Access token: 1 hour<br>
- Refresh token: 7 days
<br><br>
<b>Best Practices:</b><br>
- Call this endpoint before the access token expires<br>
- Store the new access token and continue using it for authenticated requests<br>
- If refresh fails with 401, redirect user to login flow


### Example Usage

<!-- UsageSnippet language="python" operationID="refreshToken" method="post" path="/userAccount/refresh/token" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.refresh(security=models.RefreshTokenSecurity(
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
| errors.AuthError            | 401, 404                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## logout

Log out the current user session and invalidate tokens.
<br><br>
<b>Effects:</b><br>
- Invalidates the current access token<br>
- Clears server-side session data<br>
- Client should also clear stored tokens locally
<br><br>
<b>Note:</b> This endpoint requires the access token, not the refresh token.


### Example Usage

<!-- UsageSnippet language="python" operationID="logout" method="post" path="/userAccount/logout/manual" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.user_account.logout()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LogoutResponse](../../models/logoutresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |