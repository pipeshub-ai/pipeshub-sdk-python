# SchemeOauth2

OAuth 2.0 authentication with fine-grained scopes.
Supports authorization_code (with PKCE) and client_credentials flows.
OAuth tokens are Bearer JWTs — use the same Authorization header as regular tokens.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `client_id`        | *str*              | :heavy_check_mark: | N/A                |
| `client_secret`    | *str*              | :heavy_check_mark: | N/A                |
| `token_url`        | *str*              | :heavy_check_mark: | N/A                |