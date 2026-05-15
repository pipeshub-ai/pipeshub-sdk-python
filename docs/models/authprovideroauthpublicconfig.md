# AuthProviderOAuthPublicConfig

Public generic OAuth provider settings returned to clients


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_name`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Custom OAuth provider display name                                  |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | OAuth client ID                                                     |
| `token_endpoint`                                                    | *str*                                                               | :heavy_check_mark:                                                  | OAuth token endpoint URL                                            |
| `authorization_url`                                                 | *str*                                                               | :heavy_check_mark:                                                  | OAuth authorization URL                                             |
| `client_secret`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Client secret (omitted when stripped for public responses)          |
| `user_info_endpoint`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UserInfo endpoint URL                                               |
| `scope`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Default OAuth scopes                                                |
| `enable_jit`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether just-in-time user provisioning is enabled for this provider |