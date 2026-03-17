# GenericOAuthConfig

Generic OAuth 2.0 provider configuration


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `provider_name`                       | *Optional[str]*                       | :heavy_minus_sign:                    | Display name for the OAuth provider   |
| `client_id`                           | *Optional[str]*                       | :heavy_minus_sign:                    | OAuth client ID                       |
| `client_secret`                       | *Optional[str]*                       | :heavy_minus_sign:                    | OAuth client secret                   |
| `authorization_url`                   | *Optional[str]*                       | :heavy_minus_sign:                    | Authorization endpoint URL            |
| `token_endpoint`                      | *Optional[str]*                       | :heavy_minus_sign:                    | Token endpoint URL                    |
| `user_info_endpoint`                  | *Optional[str]*                       | :heavy_minus_sign:                    | User info endpoint URL                |
| `scope`                               | *Optional[str]*                       | :heavy_minus_sign:                    | OAuth scopes to request               |
| `redirect_uri`                        | *Optional[str]*                       | :heavy_minus_sign:                    | OAuth redirect URI                    |
| `enable_jit`                          | *Optional[bool]*                      | :heavy_minus_sign:                    | Enable Just-In-Time user provisioning |