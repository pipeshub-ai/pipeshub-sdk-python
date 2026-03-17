# GenericOAuthConfig

Generic OAuth 2.0 provider configuration


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `provider_name`                       | *str*                                 | :heavy_check_mark:                    | Display name for the OAuth provider   |
| `client_id`                           | *str*                                 | :heavy_check_mark:                    | OAuth client ID                       |
| `client_secret`                       | *str*                                 | :heavy_check_mark:                    | OAuth client secret                   |
| `authorization_url`                   | *str*                                 | :heavy_check_mark:                    | Authorization endpoint URL            |
| `token_endpoint`                      | *str*                                 | :heavy_check_mark:                    | Token endpoint URL                    |
| `user_info_endpoint`                  | *str*                                 | :heavy_check_mark:                    | User info endpoint URL                |
| `scope`                               | *str*                                 | :heavy_check_mark:                    | OAuth scopes to request               |
| `redirect_uri`                        | *str*                                 | :heavy_check_mark:                    | OAuth redirect URI                    |
| `enable_jit`                          | *Optional[bool]*                      | :heavy_minus_sign:                    | Enable Just-In-Time user provisioning |