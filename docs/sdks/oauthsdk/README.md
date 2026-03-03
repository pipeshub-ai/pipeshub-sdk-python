# OAuth

## Overview

OAuth 2.0 token exchange for third-party authentication providers

### Available Operations

* [exchange_o_auth_code](#exchange_o_auth_code) - Exchange OAuth authorization code for tokens

## exchange_o_auth_code

Exchange an OAuth authorization code for access and ID tokens.
Used after the OAuth authorization flow redirects back to the application.
<br><br>
<b>Supported Providers:</b><br>
- Generic OAuth 2.0 providers configured in org settings
<br><br>
<b>Flow:</b><br>
1. User is redirected to OAuth provider's authorization URL<br>
2. User authorizes and is redirected back with a code<br>
3. This endpoint exchanges the code for tokens<br>
4. Tokens can then be used with the <code>/userAccount/authenticate</code> endpoint


### Example Usage

<!-- UsageSnippet language="python" operationID="exchangeOAuthCode" method="post" path="/userAccount/oauth/exchange" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth.exchange_o_auth_code(code="<value>", email="Jason2@gmail.com", provider="<value>", redirect_uri="https://enlightened-developing.info")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | OAuth authorization code                                            |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | User email                                                          |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | OAuth provider name                                                 |
| `redirect_uri`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Redirect URI used in authorization request                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthExchangeResponse](../../models/oauthexchangeresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.AuthError            | 400                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |