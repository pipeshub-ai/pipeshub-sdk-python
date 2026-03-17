# GenericOAuthConfig

Generic OAuth 2.0 provider configuration


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `provider_name`                           | *str*                                     | :heavy_check_mark:                        | Display name for the OAuth provider       | Custom OAuth Provider                     |
| `client_id`                               | *str*                                     | :heavy_check_mark:                        | OAuth client ID                           |                                           |
| `client_secret`                           | *str*                                     | :heavy_check_mark:                        | OAuth client secret                       |                                           |
| `authorization_url`                       | *str*                                     | :heavy_check_mark:                        | Authorization endpoint URL                | https://provider.example.com/authorize    |
| `token_endpoint`                          | *str*                                     | :heavy_check_mark:                        | Token endpoint URL                        | https://provider.example.com/token        |
| `user_info_endpoint`                      | *str*                                     | :heavy_check_mark:                        | User info endpoint URL                    | https://provider.example.com/userinfo     |
| `scope`                                   | *str*                                     | :heavy_check_mark:                        | OAuth scopes to request                   | openid email profile                      |
| `redirect_uri`                            | *str*                                     | :heavy_check_mark:                        | OAuth redirect URI                        | http://localhost:3001/auth/oauth/callback |
| `enable_jit`                              | *Optional[bool]*                          | :heavy_minus_sign:                        | Enable Just-In-Time user provisioning     |                                           |