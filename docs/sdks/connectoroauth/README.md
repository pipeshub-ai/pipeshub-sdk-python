# ConnectorOAuth

## Overview

OAuth 2.0 authorization flow for connectors requiring user consent

### Available Operations

* [get_o_auth_authorization_url](#get_o_auth_authorization_url) - Get OAuth authorization URL
* [handle_o_auth_callback](#handle_o_auth_callback) - OAuth callback handler

## get_o_auth_authorization_url

Start the OAuth sign-in for a connector instance.<br><br>
<b>Flow:</b><br>
<ol>
<li>Call this endpoint to get <code>authorizationUrl</code> and <code>state</code></li>
<li>A person opens the URL and gives consent at the provider</li>
<li>The provider redirects to <code>{baseUrl}/{redirectUri}</code> with <code>code</code> and <code>state</code></li>
<li>Pass both to <code>GET /connectors/oauth/callback</code> with a bearer token</li>
</ol>
The redirect URI is fixed when the connector is created (its <code>baseUrl</code>) and must be
registered with the provider.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthAuthorizationUrl" method="get" path="/connectors/{connectorId}/oauth/authorize" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_o_auth.get_o_auth_authorization_url(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `connector_id`                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                 | Connector instance ID                                                                                                                                                                                                                                              |
| `desktop`                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                 | `true` when the sign-in starts in the desktop app: the `state` sent to the provider is<br/>marked so the web callback page hands `code` and `state` to the app over a `pipeshub://`<br/>link instead of finishing the sign-in in the browser. Any other value is ignored.<br/> |
| `retries`                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                |

### Response

**[models.GetOAuthAuthorizationURLResponse](../../models/getoauthauthorizationurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## handle_o_auth_callback

Finish the OAuth sign-in: exchange the provider's <code>code</code> for tokens and store
them. Call it with the <code>code</code> and <code>state</code> the provider sent to the redirect URI,
as the connector's creator or an admin.<br><br>
<b>Result:</b><br>
Always JSON. <code>success</code> is true when the connector is signed in; otherwise
<code>error</code> and <code>errorMessage</code> say why. Provider tokens are never returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="handleOAuthCallback" method="get" path="/connectors/oauth/callback" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_o_auth.handle_o_auth_callback(code="<value>", state="Arizona")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `code`                                                                                                                              | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Authorization code from provider. A missing, empty or blank value is<br/>refused with `400`, even when the provider only sent `error`.<br/> |
| `state`                                                                                                                             | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | State parameter (contains connector ID). A missing, empty or blank value is refused with `400`.                                     |
| `error`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Error code if authorization failed                                                                                                  |
| `base_url`                                                                                                                          | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Origin prefixed to the returned `redirectUrl`                                                                                       |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.HandleOAuthCallbackResponse](../../models/handleoauthcallbackresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |