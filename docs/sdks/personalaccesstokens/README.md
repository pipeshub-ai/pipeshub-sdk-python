# PersonalAccessTokens

## Overview

Self-service, long-lived, scoped, revocable credentials that act as their
creator — unlike an OAuth app's `client_credentials` flow, which acts as
the app.

**Who can create one**
- **Any authenticated org member** — unlike OAuth apps, this is
  deliberately not admin-gated.

**How it's issued**
- Minted through the same OAuth access-token machinery as `/oauth2/token`,
  against one lazily-created, per-org synthetic OAuth app
  (`clientId: pat-system:<orgId>`) that every PAT in that org shares.
  That app is hidden from `/oauth-clients/*` — it never appears in your
  own OAuth app list and can't be managed through those routes.
- The raw token is prefixed `phpat_` ahead of the underlying JWT (see the
  `bearerAuth` security scheme) so it's recognizable to secret scanners.
  It's shown exactly once, at creation.

**Expiry and scopes**
- `expiryDays`: `30` (default), `90`, `365`, or `never`.
- Scopes default to the org's full configured `MCP_SCOPES` set if none
  are requested; `GET /personal-access-tokens/scopes` lists what's
  available.

**Admin visibility**
- Regular members only ever see and revoke their own tokens.
- Org admins can list and revoke *any* member's token via
  `/personal-access-tokens/admin*` — for incident response (a departed
  employee, a compromised laptop) — without needing the OAuth app CRUD
  access described above.


### Available Operations

* [list_personal_access_tokens](#list_personal_access_tokens) - List your own personal access tokens
* [create_personal_access_token](#create_personal_access_token) - Create a personal access token
* [list_personal_access_token_scopes](#list_personal_access_token_scopes) - List scopes available for a new personal access token
* [revoke_personal_access_token](#revoke_personal_access_token) - Revoke one of your own personal access tokens
* [admin_list_personal_access_tokens](#admin_list_personal_access_tokens) - Admin: list every active personal access token in the org
* [admin_revoke_personal_access_token](#admin_revoke_personal_access_token) - Admin: revoke any user's personal access token by id

## list_personal_access_tokens

Lists the caller's own active (non-revoked, unexpired) personal
access tokens, newest first, capped at 100 rows server-side. Never
returns another user's tokens — see `GET /personal-access-tokens/admin`
for the org-admin, cross-user view.

Shares the same per-user rate limiter as `/oauth-clients/*`
(default 1000 req/min, `MAX_OAUTH_CLIENT_REQUESTS_PER_MINUTE`).


### Example Usage

<!-- UsageSnippet language="python" operationID="listPersonalAccessTokens" method="get" path="/personal-access-tokens" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.list_personal_access_tokens()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListPatResponse](../../models/listpatresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## create_personal_access_token

Mints a new personal access token for the caller. Deliberately not
admin-gated — any authenticated org member may create their own,
unlike OAuth app registration.

The token is minted against a lazily-created, per-org synthetic
OAuth app (`clientId: pat-system:<orgId>`) shared by every PAT in
that org — the same signing, hashing, and revocation machinery as
`/oauth2/token`, reused rather than duplicated.

`scopes` is validated against the org's configured `MCP_SCOPES`
env var, not the full role-aware OAuth-app scope catalog — a
non-admin can request any scope in that set.

The response's `accessToken` is shown **once**; only its SHA-256
hash is stored. It's prefixed `phpat_` (see the `bearerAuth`
security scheme).


### Example Usage

<!-- UsageSnippet language="python" operationID="createPersonalAccessToken" method="post" path="/personal-access-tokens" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.create_personal_access_token(name="Claude Desktop", scopes=[
        "kb:read",
        "semantic:write",
    ], expiry_days=30)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                          | Label to help you recognize the token later                                                                                                                                                                                                                                 | Claude Desktop                                                                                                                                                                                                                                                              |
| `scopes`                                                                                                                                                                                                                                                                    | List[*str*]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Scopes to grant, validated against the org's configured `MCP_SCOPES`<br/>(not the full role-aware OAuth-app scope set). Defaults to every<br/>scope in `MCP_SCOPES` if omitted.<br/>                                                                                        | [<br/>"kb:read",<br/>"semantic:write"<br/>]                                                                                                                                                                                                                                 |
| `expiry_days`                                                                                                                                                                                                                                                               | [Optional[models.ExpiryDays]](../../models/expirydays.md)                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Token lifetime. Defaults to `30` if omitted — a token minted<br/>without an explicit choice shouldn't default to the longest<br/>lifetime. `"never"` is stored as a ~100-year expiry (the<br/>underlying schema field is required and TTL-indexed, so there's<br/>no literal null option).<br/> | 30                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |

### Response

**[models.CreatePatResponse](../../models/createpatresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401                                   | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## list_personal_access_token_scopes

Returns the org's configured `MCP_SCOPES` as a flat array of scope
definitions, for populating the create-token scope picker. Unlike
`GET /oauth-clients/scopes`, this is **not** grouped by category and
**not** role-aware — every org member sees the same set, since PAT
scope selection isn't gated by admin status.


### Example Usage

<!-- UsageSnippet language="python" operationID="listPersonalAccessTokenScopes" method="get" path="/personal-access-tokens/scopes" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.list_personal_access_token_scopes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatScopesListResponse](../../models/patscopeslistresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401                                        | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## revoke_personal_access_token

Revokes a token by id, scoped to `{tokenId, clientId, callerUserId}`
— a caller can never revoke another user's token through this route,
even though everyone in the org shares the same underlying
`pat-system:<orgId>` client. Revocation takes effect immediately: the
token's next verification attempt fails, including one already in
flight.


### Example Usage

<!-- UsageSnippet language="python" operationID="revokePersonalAccessToken" method="delete" path="/personal-access-tokens/{tokenId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.revoke_personal_access_token(token_id="<id>", reason="rotated")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Personal access token ID                                            |                                                                     |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | rotated                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RevokePatResponse](../../models/revokepatresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 401, 404                                   | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## admin_list_personal_access_tokens

Lists every active personal access token across every member of the
org, paginated, with each token's owner attached (including owners
who've since been deleted from the org — see `ownerDeleted` on
`AdminPatListItem`). For incident response: a departed employee or a
compromised laptop, where only the token's own creator could
otherwise see or revoke it.

Requires org-admin privileges (`userAdminCheck`) — note this returns
**`400`**, not `403`, for a non-admin caller (shared middleware
behavior across the codebase, not specific to this route).


### Example Usage

<!-- UsageSnippet language="python" operationID="adminListPersonalAccessTokens" method="get" path="/personal-access-tokens/admin" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.admin_list_personal_access_tokens(page=1, limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number (defaults to `1` when omitted or empty)                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Items per page (defaults to `100` when omitted or empty; max 100)   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AdminPatListResponse](../../models/adminpatlistresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401                                   | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |

## admin_revoke_personal_access_token

Revokes a token by id, scoped to the org's PAT client but **not** to
a specific owning user — the admin counterpart to
`DELETE /personal-access-tokens/{tokenId}`. Requires org-admin
privileges (`userAdminCheck`); returns `400` (not `403`) for a
non-admin caller, same as `GET /personal-access-tokens/admin`.


### Example Usage

<!-- UsageSnippet language="python" operationID="adminRevokePersonalAccessToken" method="delete" path="/personal-access-tokens/admin/{tokenId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.personal_access_tokens.admin_revoke_personal_access_token(token_id="<id>", reason="rotated")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Personal access token ID                                            |                                                                     |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | rotated                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RevokePatResponse](../../models/revokepatresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.ApplicationJSONErrorResponse        | 400, 401, 404                              | application/json                           |
| errors.OAuthClientManagementRateLimitError | 429                                        | application/json                           |
| errors.PipeshubDefaultError                | 4XX, 5XX                                   | \*/\*                                      |