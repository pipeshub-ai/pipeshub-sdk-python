# ListOAuthConfigsByTypeResponse

Saved OAuth apps


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `success`                                                                        | *bool*                                                                           | :heavy_check_mark:                                                               | N/A                                                                              |
| `oauth_configs`                                                                  | List[[models.OAuthConfigRecord](../models/oauthconfigrecord.md)]                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `pagination`                                                                     | [Optional[models.OAuthRegistryPagination]](../models/oauthregistrypagination.md) | :heavy_minus_sign:                                                               | Pagination block of `GET /oauth/registry` and `GET /oauth/{connectorType}`       |