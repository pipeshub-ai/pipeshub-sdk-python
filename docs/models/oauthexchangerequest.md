# OAuthExchangeRequest

Request to exchange OAuth authorization code for tokens


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `code`                                     | *str*                                      | :heavy_check_mark:                         | OAuth authorization code                   |
| `email`                                    | *str*                                      | :heavy_check_mark:                         | User email                                 |
| `provider`                                 | *str*                                      | :heavy_check_mark:                         | OAuth provider name                        |
| `redirect_uri`                             | *str*                                      | :heavy_check_mark:                         | Redirect URI used in authorization request |