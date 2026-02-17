# OpenIDConnect

## Overview

### Available Operations

* [get_configuration](#get_configuration) - OpenID Connect Discovery
* [jwks](#jwks) - JSON Web Key Set

## get_configuration

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.open_id_connect.get_configuration()

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.open_id_connect.jwks()

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