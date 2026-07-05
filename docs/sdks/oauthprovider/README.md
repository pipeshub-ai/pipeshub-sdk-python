# OAuthProvider

## Overview

PipesHub OAuth 2.0 Authorization Server implementing RFC 6749, RFC 7636 (PKCE), and OpenID Connect.

**Supported Grant Types:**
- `authorization_code` - Standard OAuth flow with PKCE support
- `client_credentials` - Machine-to-machine authentication
- `refresh_token` - Token refresh for long-lived access

**Security Features:**
- PKCE (Proof Key for Code Exchange) for public clients
- State parameter for CSRF protection
- Configurable token lifetimes
- Token revocation and introspection

**OpenID Connect:**
- ID tokens with standard claims
- UserInfo endpoint for profile data
- Discovery endpoint for automatic configuration

**Machine tokens (`client_credentials`) — gateway and downstream identity:**
Access tokens may encode **`userId === client_id`**. The **Node.js API gateway** resolves the effective user to the OAuth **app creator**: first using the JWT **`createdBy`** claim when present, otherwise by loading the OAuth app by **`client_id`** from the registry. After verification it sets the authenticated session to that creator.

**Python services:** Validate `Authorization: Bearer` as today and use the JWT payload’s **`userId`** as-is for scopes and user-scoped logic (which may still equal **`client_id`** for machine tokens).

**Operational note:** Prefer tokens whose JWT already carries the creator as **`userId`**; use **`POST /oauth-clients/{appId}/revoke-all-tokens`** and obtain new tokens from **`POST /oauth2/token`** when rotating integrations.


### Available Operations

* [oauth_token](#oauth_token) - Exchange authorization code for tokens
* [oauth_revoke](#oauth_revoke) - Revoke an access or refresh token
* [oauth_introspect](#oauth_introspect) - Introspect a token

## oauth_token

OAuth 2.0 Token Endpoint (RFC 6749 Section 4.1.3).

Exchanges an authorization code, client credentials, or refresh token for access tokens.

**Grant Types:**
- `authorization_code`: Exchange auth code for tokens (user-based)
- `client_credentials`: Get tokens for machine-to-machine auth
- `refresh_token`: Get new access token using refresh token

For **`client_credentials`**, access tokens represent the **OAuth app creator** (the user who registered the client). The JWT may encode **`userId === client_id`**; the **Node API gateway** resolves the creator (**`createdBy`** claim or OAuth app lookup) — see **OAuth Provider** tag.

**Client Authentication:**
Can be provided via:
- HTTP Basic auth: `Authorization: Basic base64(client_id:client_secret)`
- Request body: `client_id` and `client_secret` parameters

**PKCE Verification:**
If authorization used PKCE, the `code_verifier` must be provided and will be
verified against the stored code challenge.


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthToken" method="post" path="/oauth2/token" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ErrorResponse                       | 400                                        | application/json                           |
| errors.OAuthErrorResponse                  | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## oauth_revoke

OAuth 2.0 Token Revocation Endpoint (RFC 7009).

Revokes an access token or refresh token, preventing further use.
Revoking a refresh token also invalidates associated access tokens.

**Use Cases:**
- User logs out of third-party app
- User revokes app access from account settings
- Security incident response

**Note:** Returns 200 OK even if token was already revoked or invalid
(per RFC 7009, to prevent token enumeration).


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthRevoke" method="post" path="/oauth2/revoke" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    pipeshub.o_auth_provider.oauth_revoke(token="<value>", client_id="<id>")

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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.OAuthErrorResponse                  | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## oauth_introspect

OAuth 2.0 Token Introspection Endpoint (RFC 7662).

Check if a token is active and retrieve its metadata.

**Use Cases:**
- Resource servers validating tokens
- Debugging token issues
- Checking token scopes before processing requests

**Response:**
- Active token: Returns `active: true` with token metadata
- Invalid/expired/revoked token: Returns only `active: false`


### Example Usage: active

<!-- UsageSnippet language="python" operationID="oauthIntrospect" method="post" path="/oauth2/introspect" example="active" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_introspect(token="<value>", client_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: inactive

<!-- UsageSnippet language="python" operationID="oauthIntrospect" method="post" path="/oauth2/introspect" example="inactive" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_introspect(token="<value>", client_id="<id>")

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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.OAuthErrorResponse                  | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |