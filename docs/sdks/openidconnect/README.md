# OpenIDConnect

## Overview

OpenID Connect 1.0 endpoints for identity federation and discovery.

**Discovery:**
- `/.well-known/openid-configuration` - Authorization server metadata
- `/.well-known/oauth-authorization-server` - Authorization server metadata (RFC 8414)
- `/.well-known/oauth-protected-resource/mcp` - Protected resource metadata (RFC 9728)
- `/.well-known/jwks.json` - Public keys for token verification

**UserInfo:**
- `/oauth2/userinfo` - Get authenticated user's profile information

**Supported Claims:**
- `user_id` - User identifier
- `email`, `email_verified` - Email information
- `name`, `given_name`, `family_name` - Name information


### Available Operations

* [oauth_user_info](#oauth_user_info) - Get authenticated user information

## oauth_user_info

OpenID Connect UserInfo Endpoint.

Returns claims about the authenticated user. Requires a valid access token
with the `openid` scope.

**Available Claims:**
- `user_id` - User identifier
- `name`, `given_name`, `family_name` - Name claims (with `profile` scope)
- `email`, `email_verified` - Email claims (with `email` scope)

**Authentication:**
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