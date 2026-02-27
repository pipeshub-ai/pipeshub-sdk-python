# ConnectorOAuth

## Overview

OAuth 2.0 authorization flow for connectors requiring user consent

### Available Operations

* [get_o_auth_authorization_url](#get_o_auth_authorization_url) - Get OAuth authorization URL
* [handle_o_auth_callback](#handle_o_auth_callback) - OAuth callback handler

## get_o_auth_authorization_url

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
from pipeshub import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as p_client:

    res = p_client.connector_o_auth.get_o_auth_authorization_url(connector_id="<id>")

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

## handle_o_auth_callback

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


with Pipeshub() as p_client:

    res = p_client.connector_o_auth.handle_o_auth_callback()

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