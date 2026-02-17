# OpenidConnect

## Overview

### Available Operations

* [get_user_info](#get_user_info) - Get authenticated user information

## get_user_info

OpenID Connect UserInfo Endpoint.
<br><br>
Returns claims about the authenticated user. Requires a valid access token
with the `openid` scope.
<br><br>
<b>Available Claims:</b><br>
- `sub` - Subject identifier (user ID)<br>
- `name`, `given_name`, `family_name` - Name claims (with `profile` scope)<br>
- `email`, `email_verified` - Email claims (with `email` scope)
<br><br>
<b>Authentication:</b><br>
Pass the access token as a Bearer token: `Authorization: Bearer {access_token}`


### Example Usage

<!-- UsageSnippet language="python" operationID="oauthUserInfo" method="get" path="/oauth/userinfo" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.openid_connect.get_user_info()

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