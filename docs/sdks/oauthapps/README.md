# OAuthApps

## Overview

Manage OAuth 2.0 client applications registered with PipesHub.

OAuth apps allow third-party applications to access PipesHub APIs on behalf of users
or organizations. Each app receives a client ID and secret for authentication.

**App Types:**
- **Confidential clients**: Server-side apps that can securely store secrets
- **Public clients**: Browser/mobile apps that cannot securely store secrets (use PKCE)

**App Lifecycle:**
- Create apps with name, redirect URIs, and allowed scopes
- Regenerate secrets if compromised
- Suspend/activate apps to control access
- Revoke all tokens for emergency access removal


### Available Operations

* [list_o_auth_apps](#list_o_auth_apps) - List OAuth apps
* [create_o_auth_app](#create_o_auth_app) - Create OAuth app
* [list_o_auth_scopes](#list_o_auth_scopes) - List available scopes
* [get_o_auth_app](#get_o_auth_app) - Get OAuth app details
* [update_o_auth_app](#update_o_auth_app) - Update OAuth app
* [delete_o_auth_app](#delete_o_auth_app) - Delete OAuth app
* [regenerate_o_auth_app_secret](#regenerate_o_auth_app_secret) - Regenerate client secret
* [suspend_o_auth_app](#suspend_o_auth_app) - Suspend OAuth app
* [activate_o_auth_app](#activate_o_auth_app) - Activate suspended OAuth app
* [list_o_auth_app_tokens](#list_o_auth_app_tokens) - List app tokens
* [revoke_all_o_auth_app_tokens](#revoke_all_o_auth_app_tokens) - Revoke all app tokens

## list_o_auth_apps

List all OAuth apps registered for the organization.
<br><br>
Returns a paginated list of apps with their configuration (excluding secrets).
<br><br>
<b>Filters:</b><br>
- `status` - Filter by app status (active, suspended, revoked)<br>
- `search` - Search by app name


### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthApps" method="get" path="/oauth-clients" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.list_o_auth_apps(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `page`                                                                      | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Page number                                                                 |
| `limit`                                                                     | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Items per page                                                              |
| `status`                                                                    | [Optional[models.ListOAuthAppsStatus]](../../models/listoauthappsstatus.md) | :heavy_minus_sign:                                                          | Filter by status                                                            |
| `search`                                                                    | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Search by app name                                                          |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OAuthAppListResponse](../../models/oauthapplistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_o_auth_app

Create a new OAuth app for the organization.
<br><br>
<b>Important:</b> The client secret is only returned once during creation.
Store it securely - it cannot be retrieved later. If lost, you'll need to
regenerate it.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="createOAuthApp" method="post" path="/oauth-clients" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.create_o_auth_app(name="My Integration App", redirect_uris=[
        "https://myapp.com/callback",
        "http://localhost:3000/callback",
    ], allowed_scopes=[
        "openid",
        "profile",
        "read:records",
    ], description="Integrates PipesHub with our internal tools", allowed_grant_types=[
        "authorization_code",
        "refresh_token",
    ], is_confidential=True, access_token_lifetime=3600, refresh_token_lifetime=604800)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                    | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | App name (displayed to users during authorization)                                                                                                        | My Integration App                                                                                                                                        |
| `redirect_uris`                                                                                                                                           | List[*str*]                                                                                                                                               | :heavy_check_mark:                                                                                                                                        | Allowed redirect URIs (1-10 URIs)                                                                                                                         | [<br/>"https://myapp.com/callback",<br/>"http://localhost:3000/callback"<br/>]                                                                            |
| `allowed_scopes`                                                                                                                                          | List[*str*]                                                                                                                                               | :heavy_check_mark:                                                                                                                                        | Scopes the app can request                                                                                                                                | [<br/>"openid",<br/>"profile",<br/>"read:records"<br/>]                                                                                                   |
| `description`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | App description                                                                                                                                           | Integrates PipesHub with our internal tools                                                                                                               |
| `allowed_grant_types`                                                                                                                                     | List[[models.CreateOAuthAppRequestAllowedGrantType](../../models/createoauthapprequestallowedgranttype.md)]                                               | :heavy_minus_sign:                                                                                                                                        | Allowed grant types. Defaults to all if not specified.<br/>                                                                                               | [<br/>"authorization_code",<br/>"refresh_token"<br/>]                                                                                                     |
| `homepage_url`                                                                                                                                            | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | App homepage URL (shown during authorization)                                                                                                             |                                                                                                                                                           |
| `privacy_policy_url`                                                                                                                                      | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Privacy policy URL                                                                                                                                        |                                                                                                                                                           |
| `terms_of_service_url`                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Terms of service URL                                                                                                                                      |                                                                                                                                                           |
| `is_confidential`                                                                                                                                         | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | Whether the app can securely store secrets.<br/>- `true`: Server-side app (secret required for token requests)<br/>- `false`: Browser/mobile app (must use PKCE)<br/> |                                                                                                                                                           |
| `access_token_lifetime`                                                                                                                                   | *Optional[int]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Access token lifetime in seconds (300-86400)                                                                                                              | 3600                                                                                                                                                      |
| `refresh_token_lifetime`                                                                                                                                  | *Optional[int]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Refresh token lifetime in seconds (3600-31536000)                                                                                                         | 604800                                                                                                                                                    |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.OAuthAppWithSecret](../../models/oauthappwithsecret.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_o_auth_scopes

List all available OAuth scopes that can be requested by apps.
<br><br>
Returns scope names, descriptions, and categories for display
in app configuration UI.


### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthScopes" method="get" path="/oauth-clients/scopes" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.list_o_auth_scopes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOAuthScopesResponse](../../models/listoauthscopesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_o_auth_app

Get details of a specific OAuth app.
<br><br>
Returns app configuration without the client secret.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthApp" method="get" path="/oauth-clients/{appId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.get_o_auth_app(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID (MongoDB ObjectId)                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthAppResponse](../../models/oauthappresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_o_auth_app

Update an OAuth app's configuration.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.
<br><br>
<b>Note:</b> To regenerate the client secret, use the
`/oauth-clients/{appId}/regenerate-secret` endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateOAuthApp" method="put" path="/oauth-clients/{appId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.update_o_auth_app(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `app_id`                                                                                                    | *str*                                                                                                       | :heavy_check_mark:                                                                                          | OAuth app ID                                                                                                |
| `name`                                                                                                      | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | App name                                                                                                    |
| `description`                                                                                               | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | App description                                                                                             |
| `redirect_uris`                                                                                             | List[*str*]                                                                                                 | :heavy_minus_sign:                                                                                          | Allowed redirect URIs                                                                                       |
| `allowed_grant_types`                                                                                       | List[[models.UpdateOAuthAppRequestAllowedGrantType](../../models/updateoauthapprequestallowedgranttype.md)] | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `allowed_scopes`                                                                                            | List[*str*]                                                                                                 | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `homepage_url`                                                                                              | *OptionalNullable[str]*                                                                                     | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `privacy_policy_url`                                                                                        | *OptionalNullable[str]*                                                                                     | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `terms_of_service_url`                                                                                      | *OptionalNullable[str]*                                                                                     | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `access_token_lifetime`                                                                                     | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `refresh_token_lifetime`                                                                                    | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.OAuthAppResponse](../../models/oauthappresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_o_auth_app

Delete (soft delete) an OAuth app.
<br><br>
This marks the app as deleted and revokes all its tokens.
The app cannot be restored after deletion.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOAuthApp" method="delete" path="/oauth-clients/{appId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.delete_o_auth_app(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOAuthAppResponse](../../models/deleteoauthappresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## regenerate_o_auth_app_secret

Regenerate the client secret for an OAuth app.
<br><br>
The old secret is immediately invalidated. Any clients using the old
secret will fail to authenticate until updated with the new secret.
<br><br>
<b>Important:</b> The new secret is only returned once. Store it securely.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="regenerateOAuthAppSecret" method="post" path="/oauth-clients/{appId}/regenerate-secret" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.regenerate_o_auth_app_secret(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthAppWithSecret](../../models/oauthappwithsecret.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## suspend_o_auth_app

Suspend an OAuth app, preventing it from authenticating or issuing tokens.
<br><br>
Existing tokens remain valid until they expire, but no new tokens can
be obtained. Use this for temporary access suspension.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="suspendOAuthApp" method="post" path="/oauth-clients/{appId}/suspend" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.suspend_o_auth_app(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthAppResponse](../../models/oauthappresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## activate_o_auth_app

Reactivate a suspended OAuth app, allowing it to authenticate and issue tokens again.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="activateOAuthApp" method="post" path="/oauth-clients/{appId}/activate" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.activate_o_auth_app(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthAppResponse](../../models/oauthappresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_o_auth_app_tokens

List all active tokens issued to an OAuth app.
<br><br>
Useful for monitoring app usage and identifying tokens to revoke.
<br><br>
<b>Admin Only:</b> Requires admin privileges.


### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthAppTokens" method="get" path="/oauth-clients/{appId}/tokens" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.list_o_auth_app_tokens(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.OAuthTokenListItem]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## revoke_all_o_auth_app_tokens

Revoke all tokens (access and refresh) issued to an OAuth app.
<br><br>
Use this for emergency access removal or when rotating credentials.
<br><br>
<b>Admin Only:</b> Requires admin privileges.
<br><br>
<b>Rate Limited:</b> 10 requests per minute.


### Example Usage

<!-- UsageSnippet language="python" operationID="revokeAllOAuthAppTokens" method="post" path="/oauth-clients/{appId}/revoke-all-tokens" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_apps.revoke_all_o_auth_app_tokens(app_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | OAuth app ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RevokeAllOAuthAppTokensResponse](../../models/revokealloauthapptokensresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |