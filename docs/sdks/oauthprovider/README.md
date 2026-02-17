# OauthProvider

## Overview

### Available Operations

* [authorize](#authorize) - Initiate OAuth authorization flow
* [submit_consent](#submit_consent) - Submit authorization consent
* [exchange_token](#exchange_token) - Exchange authorization code for tokens
* [revoke](#revoke) - Revoke an access or refresh token
* [introspect](#introspect) - Introspect a token

## authorize

OAuth 2.0 Authorization Endpoint (RFC 6749 Section 4.1.1).
<br><br>
Initiates the authorization code flow. Users are redirected here by OAuth clients
to authorize access to their account.
<br><br>
<b>Flow:</b><br>
1. Client redirects user to this endpoint with required parameters<br>
2. If not logged in, user is redirected to PipesHub login<br>
3. User sees consent page with requested scopes<br>
4. User grants or denies consent<br>
5. User is redirected back to client with authorization code
<br><br>
<b>PKCE Support (RFC 7636):</b><br>
- Required for public clients (SPA, mobile apps)<br>
- Recommended for confidential clients<br>
- Use S256 method (SHA256 hash of code_verifier)
<br><br>
<b>Security:</b><br>
- Always use HTTPS in production<br>
- State parameter provides CSRF protection<br>
- Redirect URI must match registered URIs exactly


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthAuthorize" method="get" path="/oauth/authorize" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.oauth_provider.authorize(response_type="code", client_id="<id>", redirect_uri="https://coordinated-dime.biz/", scope="openid profile email read:records", state="Delaware")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `response_type`                                                                                         | [models.ResponseType](../../models/responsetype.md)                                                     | :heavy_check_mark:                                                                                      | Must be "code" for authorization code grant                                                             |                                                                                                         |
| `client_id`                                                                                             | *str*                                                                                                   | :heavy_check_mark:                                                                                      | OAuth app client ID                                                                                     |                                                                                                         |
| `redirect_uri`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Callback URI (must match registered URI)                                                                |                                                                                                         |
| `scope`                                                                                                 | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Space-separated list of requested scopes                                                                | openid profile email read:records                                                                       |
| `state`                                                                                                 | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Random string for CSRF protection                                                                       |                                                                                                         |
| `code_challenge`                                                                                        | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | PKCE code challenge (base64url-encoded)                                                                 |                                                                                                         |
| `code_challenge_method`                                                                                 | [Optional[models.OauthAuthorizeCodeChallengeMethod]](../../models/oauthauthorizecodechallengemethod.md) | :heavy_minus_sign:                                                                                      | PKCE method (S256 recommended)                                                                          |                                                                                                         |
| `nonce`                                                                                                 | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Nonce for ID token binding                                                                              |                                                                                                         |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.OauthAuthorizeResponse](../../models/oauthauthorizeresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.OAuthErrorResponse   | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## submit_consent

Submit user's consent decision for OAuth authorization.
<br><br>
Called after user reviews the consent page and makes a decision.
This endpoint generates an authorization code if consent is granted.
<br><br>
<b>Responses:</b><br>
- Consent granted: Redirects to client with authorization code<br>
- Consent denied: Redirects to client with `access_denied` error


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthAuthorizeConsent" method="post" path="/oauth/authorize" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_provider.submit_consent(client_id="<id>", redirect_uri="https://excellent-license.com", scope="<value>", state="South Dakota", consent="denied")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `client_id`                                                                 | *str*                                                                       | :heavy_check_mark:                                                          | The OAuth app's client ID                                                   |
| `redirect_uri`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | Redirect URI (must match authorization request)                             |
| `scope`                                                                     | *str*                                                                       | :heavy_check_mark:                                                          | Requested scopes                                                            |
| `state`                                                                     | *str*                                                                       | :heavy_check_mark:                                                          | State parameter from authorization request                                  |
| `consent`                                                                   | [models.Consent](../../models/consent.md)                                   | :heavy_check_mark:                                                          | User's consent decision                                                     |
| `code_challenge`                                                            | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | PKCE code challenge (if used in authorization request)                      |
| `code_challenge_method`                                                     | [Optional[models.CodeChallengeMethod]](../../models/codechallengemethod.md) | :heavy_minus_sign:                                                          | PKCE challenge method                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OauthAuthorizeConsentResponse](../../models/oauthauthorizeconsentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.OAuthErrorResponse   | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## exchange_token

OAuth 2.0 Token Endpoint (RFC 6749 Section 4.1.3).
<br><br>
Exchanges an authorization code, client credentials, or refresh token for access tokens.
<br><br>
<b>Grant Types:</b><br>
- `authorization_code`: Exchange auth code for tokens (user-based)<br>
- `client_credentials`: Get tokens for machine-to-machine auth<br>
- `refresh_token`: Get new access token using refresh token
<br><br>
<b>Client Authentication:</b><br>
Can be provided via:<br>
- HTTP Basic auth: `Authorization: Basic base64(client_id:client_secret)`<br>
- Request body: `client_id` and `client_secret` parameters
<br><br>
<b>PKCE Verification:</b><br>
If authorization used PKCE, the `code_verifier` must be provided and will be
verified against the stored code challenge.


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthToken" method="post" path="/oauth/token" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.oauth_provider.exchange_token(grant_type="client_credentials")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `grant_type`                                                                                                                                                                         | [models.GrantType](../../models/granttype.md)                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                   | OAuth grant type:<br/>- `authorization_code`: Exchange auth code for tokens<br/>- `client_credentials`: Machine-to-machine auth<br/>- `refresh_token`: Get new access token using refresh token<br/> |
| `code`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Authorization code (required for authorization_code grant)                                                                                                                           |
| `redirect_uri`                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Redirect URI (required for authorization_code grant)                                                                                                                                 |
| `client_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Client ID (can also be sent via Basic auth header)                                                                                                                                   |
| `client_secret`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Client secret (can also be sent via Basic auth header)                                                                                                                               |
| `refresh_token`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Refresh token (required for refresh_token grant)                                                                                                                                     |
| `scope`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Requested scopes (optional, defaults to original grant scopes)                                                                                                                       |
| `code_verifier`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | PKCE code verifier (RFC 7636). Required if code_challenge was used.<br/>Must be 43-128 characters from [A-Za-z0-9-._~]<br/>                                                          |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[models.OAuthTokenResponse](../../models/oauthtokenresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.OAuthErrorResponse   | 400, 401                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## revoke

OAuth 2.0 Token Revocation Endpoint (RFC 7009).
<br><br>
Revokes an access token or refresh token, preventing further use.
Revoking a refresh token also invalidates associated access tokens.
<br><br>
<b>Use Cases:</b><br>
- User logs out of third-party app<br>
- User revokes app access from account settings<br>
- Security incident response
<br><br>
<b>Note:</b> Returns 200 OK even if token was already revoked or invalid
(per RFC 7009, to prevent token enumeration).


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthRevoke" method="post" path="/oauth/revoke" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.oauth_provider.revoke(token="<value>", client_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `token`                                                                                             | *str*                                                                                               | :heavy_check_mark:                                                                                  | The token to revoke                                                                                 |
| `client_id`                                                                                         | *str*                                                                                               | :heavy_check_mark:                                                                                  | Client ID                                                                                           |
| `token_type_hint`                                                                                   | [Optional[models.OAuthRevokeRequestTokenTypeHint]](../../models/oauthrevokerequesttokentypehint.md) | :heavy_minus_sign:                                                                                  | Hint about token type (optional, improves performance)                                              |
| `client_secret`                                                                                     | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Client secret                                                                                       |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.OAuthErrorResponse   | 401                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## introspect

OAuth 2.0 Token Introspection Endpoint (RFC 7662).
<br><br>
Check if a token is active and retrieve its metadata.
<br><br>
<b>Use Cases:</b><br>
- Resource servers validating tokens<br>
- Debugging token issues<br>
- Checking token scopes before processing requests
<br><br>
<b>Response:</b><br>
- Active token: Returns `active: true` with token metadata<br>
- Invalid/expired/revoked token: Returns only `active: false`


### Example Usage: active

<!-- UsageSnippet language="python" operationID="oauthIntrospect" method="post" path="/oauth/introspect" example="active" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.oauth_provider.introspect(token="<value>", client_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: inactive

<!-- UsageSnippet language="python" operationID="oauthIntrospect" method="post" path="/oauth/introspect" example="inactive" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.oauth_provider.introspect(token="<value>", client_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `token`                                                                                                     | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The token to introspect                                                                                     |
| `client_id`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | Client ID                                                                                                   |
| `token_type_hint`                                                                                           | [Optional[models.OAuthIntrospectRequestTokenTypeHint]](../../models/oauthintrospectrequesttokentypehint.md) | :heavy_minus_sign:                                                                                          | Hint about token type                                                                                       |
| `client_secret`                                                                                             | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Client secret                                                                                               |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.OAuthIntrospectResponse](../../models/oauthintrospectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.OAuthErrorResponse   | 401                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |