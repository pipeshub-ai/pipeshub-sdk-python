# GenericOAuthConfig

Generic OAuth 2.0 provider configuration


## Fields

| Field                               | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `provider_name`                     | *Optional[str]*                     | :heavy_minus_sign:                  | Display name for the OAuth provider | Custom OAuth Provider               |
| `client_id`                         | *Optional[str]*                     | :heavy_minus_sign:                  | OAuth client ID                     |                                     |
| `client_secret`                     | *Optional[str]*                     | :heavy_minus_sign:                  | OAuth client secret                 |                                     |
| `authorization_url`                 | *Optional[str]*                     | :heavy_minus_sign:                  | Authorization endpoint URL          |                                     |
| `token_endpoint`                    | *Optional[str]*                     | :heavy_minus_sign:                  | Token endpoint URL                  |                                     |
| `user_info_endpoint`                | *Optional[str]*                     | :heavy_minus_sign:                  | User info endpoint URL              |                                     |
| `scope`                             | *Optional[str]*                     | :heavy_minus_sign:                  | OAuth scopes to request             | openid profile email                |
| `redirect_uri`                      | *Optional[str]*                     | :heavy_minus_sign:                  | OAuth redirect URI                  |                                     |