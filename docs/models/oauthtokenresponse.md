# OAuthTokenResponse

OAuth 2.0 Token Response (RFC 6749 Section 5.1).
Contains the access token and optional refresh/ID tokens.



## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `access_token`                                              | *Optional[str]*                                             | :heavy_minus_sign:                                          | The access token for API requests                           |                                                             |
| `token_type`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Token type (always "Bearer")                                | Bearer                                                      |
| `expires_in`                                                | *Optional[int]*                                             | :heavy_minus_sign:                                          | Access token lifetime in seconds                            | 3600                                                        |
| `refresh_token`                                             | *Optional[str]*                                             | :heavy_minus_sign:                                          | Refresh token for obtaining new access tokens               |                                                             |
| `scope`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | Granted scopes (may differ from requested)                  |                                                             |
| `id_token`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | OpenID Connect ID token (JWT) if openid scope was requested |                                                             |