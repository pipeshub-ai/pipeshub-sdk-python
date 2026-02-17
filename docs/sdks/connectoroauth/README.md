# ConnectorOAuth

## Overview

### Available Operations

* [exchange_code_for_token](#exchange_code_for_token) - Exchange authorization code for tokens (legacy)
* [get_authorization_url](#get_authorization_url) - Get OAuth authorization URL
* [handle_callback](#handle_callback) - OAuth callback handler

## exchange_code_for_token

Exchange a Google Workspace authorization code for access and refresh tokens.<br><br>
<b>Note:</b> This is a legacy endpoint specific to Google Workspace connectors.
For new integrations, use the standard OAuth flow via
<code>/connectors/{connectorId}/oauth/authorize</code> and the callback.<br><br>
<b>Flow:</b><br>
<ol>
<li>User completes Google Workspace OAuth consent in the browser</li>
<li>Browser receives authorization code</li>
<li>Frontend sends the code to this endpoint</li>
<li>Backend exchanges code for tokens and stores them</li>
</ol>
<b>Admin Only:</b> Requires admin privileges.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTokenFromCode" method="post" path="/connectors/getTokenFromCode" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_o_auth.exchange_code_for_token(code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Authorization code from Google OAuth consent flow                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTokenFromCodeResponse](../../models/gettokenfromcoderesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_authorization_url

Generate an OAuth authorization URL to start the OAuth flow.<br><br>
<b>Flow:</b><br>
<ol>
<li>Call this endpoint to get the authorization URL</li>
<li>Redirect user's browser to the URL</li>
<li>User authenticates with the provider</li>
<li>Provider redirects to callback with authorization code</li>
<li>Callback exchanges code for tokens automatically</li>
</ol>
<b>State Parameter:</b><br>
The response includes a <code>state</code> value that encodes the
connector ID. This is validated in the callback.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthAuthorizationUrl" method="get" path="/connectors/{connectorId}/oauth/authorize" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_o_auth.get_authorization_url(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Base URL for self-hosted instances                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthAuthorizationURLResponse](../../models/getoauthauthorizationurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## handle_callback

Handle the OAuth callback from the identity provider.<br><br>
<b>Note:</b><br>
This endpoint is called by the OAuth provider after user authentication.
The state parameter contains the encoded connector ID.<br><br>
<b>Success:</b><br>
On success, tokens are stored and the connector becomes authenticated.
User is redirected to the frontend success page.<br><br>
<b>Error:</b><br>
If the provider returns an error (e.g., user denied access),
user is redirected with error information.


### Example Usage

<!-- UsageSnippet language="python" operationID="handleOAuthCallback" method="get" path="/connectors/oauth/callback" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_o_auth.handle_callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Authorization code from provider                                    |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | State parameter (contains connector ID)                             |
| `error`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Error code if authorization failed                                  |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Base URL for redirect                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HandleOAuthCallbackResponse](../../models/handleoauthcallbackresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |