# OpenIDConnect

## Overview

OpenID Connect 1.0 endpoints for identity federation and discovery.

**Discovery:**
- `/.well-known/openid-configuration` - Authorization server metadata
- `/.well-known/jwks.json` - Public keys for token verification

**UserInfo:**
- `/oauth2/userinfo` - Get authenticated user's profile information

**Supported Claims:**
- `user_id` - User identifier
- `email`, `email_verified` - Email information
- `name`, `given_name`, `family_name` - Name information


### Available Operations

* [oauth_user_info](#oauth_user_info) - Get authenticated user information
* [openid_configuration](#openid_configuration) - OpenID Connect Discovery
* [jwks](#jwks) - JSON Web Key Set

## oauth_user_info

OpenID Connect UserInfo Endpoint.
<br><br>
Returns claims about the authenticated user. Requires a valid access token
with the `openid` scope.
<br><br>
<b>Available Claims:</b><br>
- `user_id` - User identifier<br>
- `name`, `given_name`, `family_name` - Name claims (with `profile` scope)<br>
- `email`, `email_verified` - Email claims (with `email` scope)
<br><br>
<b>Authentication:</b><br>
Pass the access token as a Bearer token: `Authorization: Bearer {access_token}`


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthUserInfo" method="get" path="/oauth2/userinfo" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.open_id_connect.oauth_user_info()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthUserInfoResponse](../../models/oauthuserinforesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## openid_configuration

OpenID Connect Discovery Endpoint (RFC 8414).
<br><br>
Returns metadata about the OAuth/OIDC authorization server including
endpoint URLs, supported features, and capabilities.
<br><br>
<b>Use Cases:</b><br>
- Automatic client configuration<br>
- Discovering supported features<br>
- Getting endpoint URLs without hardcoding
<br><br>
<b>Note:</b> This endpoint does not require authentication.


### Example Usage

<!-- UsageSnippet language="python" operationID="openidConfiguration" method="get" path="/.well-known/openid-configuration" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.open_id_connect.openid_configuration()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.OpenIDConfiguration](../../models/openidconfiguration.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## jwks

JSON Web Key Set Endpoint (RFC 7517).
<br><br>
Returns the public keys used to verify JWT signatures for ID tokens
and access tokens.
<br><br>
<b>Use Cases:</b><br>
- Verifying ID token signatures<br>
- Verifying access token signatures (if JWT-based)
<br><br>
<b>Note:</b><br>
- For HS256 (symmetric) signing, this returns empty keys<br>
- For RS256 (asymmetric) signing, returns public RSA keys<br>
- Keys should be cached with appropriate TTL


### Example Usage

<!-- UsageSnippet language="python" operationID="jwks" method="get" path="/.well-known/jwks.json" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.open_id_connect.jwks()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.Jwks](../../models/jwks.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |