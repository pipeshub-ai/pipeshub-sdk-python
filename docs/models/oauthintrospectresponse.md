# OAuthIntrospectResponse

OAuth 2.0 Token Introspection Response (RFC 7662).
Contains token metadata if active, or just `active: false` if not.



## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `active`                                | *bool*                                  | :heavy_check_mark:                      | Whether the token is currently active   |
| `scope`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | Scopes granted to the token             |
| `client_id`                             | *Optional[str]*                         | :heavy_minus_sign:                      | Client ID the token was issued to       |
| `username`                              | *Optional[str]*                         | :heavy_minus_sign:                      | User identifier (if user-based token)   |
| `token_type`                            | *Optional[str]*                         | :heavy_minus_sign:                      | Token type                              |
| `exp`                                   | *Optional[int]*                         | :heavy_minus_sign:                      | Token expiration timestamp (Unix epoch) |
| `iat`                                   | *Optional[int]*                         | :heavy_minus_sign:                      | Token issuance timestamp (Unix epoch)   |
| `nbf`                                   | *Optional[int]*                         | :heavy_minus_sign:                      | Token not-before timestamp (Unix epoch) |
| `sub`                                   | *Optional[str]*                         | :heavy_minus_sign:                      | Subject (user ID)                       |
| `aud`                                   | *Optional[str]*                         | :heavy_minus_sign:                      | Audience (client ID)                    |
| `iss`                                   | *Optional[str]*                         | :heavy_minus_sign:                      | Issuer URL                              |
| `jti`                                   | *Optional[str]*                         | :heavy_minus_sign:                      | Unique token identifier                 |