# OAuthExchangeResponse

OAuth token response


## Fields

| Field                   | Type                    | Required                | Description             | Example                 |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `access_token`          | *Optional[str]*         | :heavy_minus_sign:      | OAuth access token      |                         |
| `id_token`              | *Optional[str]*         | :heavy_minus_sign:      | OAuth ID token (JWT)    |                         |
| `token_type`            | *Optional[str]*         | :heavy_minus_sign:      | N/A                     | Bearer                  |
| `expires_in`            | *Optional[int]*         | :heavy_minus_sign:      | Token expiry in seconds |                         |