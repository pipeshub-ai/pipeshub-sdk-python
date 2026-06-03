# OAuthApps

## Overview

Manage OAuth 2.0 client applications registered with PipesHub.

OAuth apps allow third-party applications to access PipesHub APIs on behalf of users
or organizations. Each app receives a client ID and secret for authentication.

**Who can see which apps**
- **Everyone (including org admins)** sees and manages only OAuth apps **they created** (`createdBy`). Other members' apps are hidden (not listed; individual operations return not found).

**Who authorizes vs. client credentials**
- **Authorization code:** Any authenticated user in the workspace may complete consent for a valid `client_id`; issued tokens represent **that user**.
- **Client credentials:** Access tokens represent the **OAuth app creator** (who registered the client), not the caller.

**Scopes**
- `GET /oauth-clients/scopes` returns scopes grouped by category for the **signed-in user's role**.
- **Org admins** may register apps that request additional **admin-only** scopes; non-admins cannot select those scopes when creating or updating an app.

**App Types:**
- **Confidential clients**: Server-side apps that can securely store secrets
- **Public clients**: Browser/mobile apps that cannot securely store secrets (use PKCE)

**App Lifecycle:**
- Create apps with name, redirect URIs, allowed scopes, and optional URLs (homepage, privacy, terms)
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

Returns a paginated list of OAuth apps registered by the signed-in user. Access is creator-scoped — even org admins only see apps they created themselves, so this endpoint is safe to use for per-user developer dashboards without leaking org-wide app metadata.

Each entry carries the full app configuration except the client secret, which is only ever returned at creation time and immediately after a regeneration.

Use the `status` query parameter to filter by lifecycle state (`active`, `suspended`, `revoked`) and `search` for a case-insensitive substring match against `name` or `description`.


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

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `page`                                                                               | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | Page number (matches `listAppsQuerySchema`: defaults to `1` when omitted or empty).<br/> |
| `limit`                                                                              | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | Items per page (defaults to `20` when omitted or empty; max 100).<br/>               |
| `status`                                                                             | [Optional[models.ListOAuthAppsStatus]](../../models/listoauthappsstatus.md)          | :heavy_minus_sign:                                                                   | Filter by status                                                                     |
| `search`                                                                             | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Search by app name or description (case-insensitive)                                 |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[models.OAuthAppListResponse](../../models/oauthapplistresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403                                   | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## create_o_auth_app

Register a new OAuth app for the organization. Any authenticated org member may create apps; the creator is recorded as the app's owner and is the only user who can subsequently read, update, suspend, activate, regenerate the secret of, or delete it.

The `clientSecret` is returned in this response **only** — it is stored hashed server-side and cannot be retrieved later. Persist it before exiting the create flow; if it is ever lost, rotate via `POST /oauth-clients/{appId}/regenerate-secret`.

`allowedScopes` is validated against the caller's role-aware scope set (see `GET /oauth-clients/scopes`). Org admins may include admin-only scopes; non-admins requesting a restricted scope receive `400`.

All `/oauth-clients/*` routes share a per-user rate limiter (default 1000 req/min, configurable via the `MAX_OAUTH_CLIENT_REQUESTS_PER_MINUTE` env var).


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

    res = pipeshub.o_auth_apps.create_o_auth_app(name="My Integration App", allowed_scopes=[
        "openid",
        "profile",
        "read:records",
    ], description="Integrates PipesHub with our internal tools", redirect_uris=[
        "https://myapp.com/callback",
        "http://localhost:3000/callback",
    ], allowed_grant_types=[
        "authorization_code",
        "refresh_token",
    ], is_confidential=True, access_token_lifetime=3600, refresh_token_lifetime=604800)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                            | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | App name (displayed to users during authorization)                                                                                                                | My Integration App                                                                                                                                                |
| `allowed_scopes`                                                                                                                                                  | List[*str*]                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                | Scopes the app can request (non-empty)                                                                                                                            | [<br/>"openid",<br/>"profile",<br/>"read:records"<br/>]                                                                                                           |
| `description`                                                                                                                                                     | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | App description                                                                                                                                                   | Integrates PipesHub with our internal tools                                                                                                                       |
| `redirect_uris`                                                                                                                                                   | List[*str*]                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                | Allowed redirect URIs (max 10). Required when an effective grant list includes `authorization_code`<br/>(including the default when `allowedGrantTypes` is omitted).<br/> | [<br/>"https://myapp.com/callback",<br/>"http://localhost:3000/callback"<br/>]                                                                                    |
| `allowed_grant_types`                                                                                                                                             | List[[models.CreateOAuthAppRequestAllowedGrantType](../../models/createoauthapprequestallowedgranttype.md)]                                                       | :heavy_minus_sign:                                                                                                                                                | Allowed grant types. Defaults to `["authorization_code", "refresh_token"]` if omitted (applied by the service, not Zod).<br/>                                     | [<br/>"authorization_code",<br/>"refresh_token"<br/>]                                                                                                             |
| `homepage_url`                                                                                                                                                    | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | App homepage URL (shown during authorization)                                                                                                                     |                                                                                                                                                                   |
| `privacy_policy_url`                                                                                                                                              | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Privacy policy URL                                                                                                                                                |                                                                                                                                                                   |
| `terms_of_service_url`                                                                                                                                            | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Terms of service URL                                                                                                                                              |                                                                                                                                                                   |
| `is_confidential`                                                                                                                                                 | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Whether the app can securely store secrets.<br/>- `true`: Server-side app (secret required for token requests)<br/>- `false`: Browser/mobile app (must use PKCE)<br/> |                                                                                                                                                                   |
| `access_token_lifetime`                                                                                                                                           | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Access token lifetime in seconds (300–86400)                                                                                                                      | 3600                                                                                                                                                              |
| `refresh_token_lifetime`                                                                                                                                          | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Refresh token lifetime in seconds (3600–31536000)                                                                                                                 | 2592000                                                                                                                                                           |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.CreateOAuthAppResponse](../../models/createoauthappresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401, 403                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## list_o_auth_scopes

Returns the OAuth scopes the signed-in user is permitted to register on new or updated apps, grouped by category. Use this to populate scope-picker UIs and to validate `allowedScopes` client-side before submitting to `createOAuthApp` / `updateOAuthApp`.

The result is role-aware. Org admins (members of an admin user group) receive every registered scope; everyone else is filtered to exclude admin-only scopes: `org:write`, `org:admin`, `user:invite`, `user:delete`, `usergroup:write`, `team:write`, `config:write`, `crawl:write`, `crawl:delete`.

Each key in the `scopes` map matches the `category` field on the `OAuthScopeInfo` entries it contains. A category may appear with an empty array when every scope it contains is restricted for the caller — treat empty buckets as "no permitted scopes in this group", not as a missing category.

Shares the per-user rate limiter applied to every `/oauth-clients/*` route (default 1000 req/min, `MAX_OAUTH_CLIENT_REQUESTS_PER_MINUTE`).


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

**[models.OAuthScopesGroupedResponse](../../models/oauthscopesgroupedresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## get_o_auth_app

Returns the full configuration of an OAuth app you registered. The `clientSecret` is never echoed back here; if you need a new one, call `POST /oauth-clients/{appId}/regenerate-secret`.

Access is creator-scoped: even org admins receive `404` for apps owned by other users. This avoids leaking app metadata across org members and keeps the read surface symmetric with `listOAuthApps`.


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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## update_o_auth_app

Update an OAuth app's configuration. All body fields are optional — supply only what should change. URL fields (`homepageUrl`, `privacyPolicyUrl`, `termsOfServiceUrl`) accept `null` to clear them.

Creator-only: even org admins cannot edit apps owned by other users.

When modifying `allowedScopes`, the new set must remain a subset of the caller's role-aware scope list (same rule as `GET /oauth-clients/scopes`). When adding `authorization_code` to `allowedGrantTypes`, `redirectUris` becomes required and must contain at least one URI; otherwise the request is rejected with `400` by the Zod refine on `updateAppSchema`.

This endpoint never rotates the client secret — use `POST /oauth-clients/{appId}/regenerate-secret` for that.


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

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_id`                                                                                                                                                                         | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | OAuth app ID                                                                                                                                                                     |
| `name`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | App name                                                                                                                                                                         |
| `description`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | App description                                                                                                                                                                  |
| `redirect_uris`                                                                                                                                                                  | List[*str*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                               | Allowed redirect URIs (up to 10). Required when `authorization_code` grant type is enabled.<br/>Preserved in the database even if `authorization_code` is removed from grant types.<br/> |
| `allowed_grant_types`                                                                                                                                                            | List[[models.UpdateOAuthAppRequestAllowedGrantType](../../models/updateoauthapprequestallowedgranttype.md)]                                                                      | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `allowed_scopes`                                                                                                                                                                 | List[*str*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `homepage_url`                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `privacy_policy_url`                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `terms_of_service_url`                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `access_token_lifetime`                                                                                                                                                          | *Optional[int]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `refresh_token_lifetime`                                                                                                                                                         | *Optional[int]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.UpdateOAuthAppResponse](../../models/updateoauthappresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401, 403, 404                         | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## delete_o_auth_app

Soft-deletes an OAuth app. The app is flagged `isDeleted=true` on the `OAuthApp` document, removed from list/get responses for every caller, and all of its access and refresh tokens are revoked in the same operation. There is no restore endpoint — deletion is final.

Creator-only: even org admins cannot delete apps owned by other users.


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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## regenerate_o_auth_app_secret

Generates a fresh client secret for an OAuth app. The previous secret is invalidated immediately — any client still presenting it will fail token exchange at `POST /oauth2/token` until updated.

The new secret is returned in this response **only** and cannot be retrieved later. Pair this call with credential propagation to every integration that uses the app. If the rotation was triggered by a suspected leak, also call `POST /oauth-clients/{appId}/revoke-all-tokens` to invalidate already-issued access and refresh tokens instead of waiting for their natural expiry.

Creator-only: even org admins cannot rotate secrets for other users' apps.


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

**[models.RegenerateOAuthAppSecretResponse](../../models/regenerateoauthappsecretresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## suspend_o_auth_app

Moves an OAuth app to `status: "suspended"`, blocking new token issuance at `POST /oauth2/token` and the authorization-code consent flow. Tokens that have already been issued remain valid until their natural expiry — call `POST /oauth-clients/{appId}/revoke-all-tokens` immediately afterwards if you need an immediate lockout.

Use this for temporary suspensions where you intend to reactivate later. For permanent removal, use `DELETE /oauth-clients/{appId}`. Suspending an app that is already suspended returns `400`.

Creator-only.


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

**[models.SuspendOAuthAppResponse](../../models/suspendoauthappresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401, 403, 404                         | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## activate_o_auth_app

Moves a suspended OAuth app back to `status: "active"`, restoring its ability to authenticate and obtain new tokens via `POST /oauth2/token`.

A revoked app cannot be reactivated (returns `400`); the only path back is to register a new app. Activating an app that is already active also returns `400`.

Creator-only.


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

**[models.ActivateOAuthAppResponse](../../models/activateoauthappresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401, 403, 404                         | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## list_o_auth_app_tokens

Lists active access and refresh tokens currently issued to an OAuth app, sorted newest first. Useful for auditing app usage and picking specific tokens to investigate before a targeted revocation.

Each entry includes the token type (`access` or `refresh`), the user the token was issued for (omitted for client-credentials access tokens), the granted scopes, the issuance and expiry timestamps, and the revocation flag. Each type is capped at 100 most-recent rows server-side (`listTokensForApp` in `oauth_token.service.ts`); revoked and expired tokens are excluded.

Creator-only.


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

**[models.OAuthAppTokensListResponse](../../models/oauthapptokenslistresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## revoke_all_o_auth_app_tokens

Revokes every access and refresh token currently issued to an OAuth app, in a single operation. Use this for emergency credential rotation, suspected secret leaks, or as a follow-up to `POST /oauth-clients/{appId}/regenerate-secret` when you want existing sessions invalidated immediately rather than letting them expire naturally.

The response `count` is the total number of tokens revoked across both types. Clients of this app must then obtain new tokens via the standard OAuth flow.

Creator-only.


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

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 403, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |