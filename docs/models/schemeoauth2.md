# SchemeOauth2

OAuth 2.0 authentication with fine-grained scopes.
Supports authorization_code (with PKCE) and client_credentials flows.
OAuth tokens are Bearer JWTs — use the same Authorization header as regular tokens.
For **client_credentials**, machine JWTs may use `userId === client_id`; the Node gateway resolves the application's token identity — the service account it is pointed at, or its creator for an application registered before that was required — see **OAuth Provider** tag.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `client_id`        | *str*              | :heavy_check_mark: | N/A                |
| `client_secret`    | *str*              | :heavy_check_mark: | N/A                |
| `token_url`        | *str*              | :heavy_check_mark: | N/A                |