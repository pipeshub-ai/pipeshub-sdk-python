# ListOAuthConfigsByTypeResponse

OAuth configurations retrieved


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `success`                                                                | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | N/A                                                                      |
| `oauth_configs`                                                          | List[[models.OAuthConfig](../models/oauthconfig.md)]                     | :heavy_minus_sign:                                                       | N/A                                                                      |
| `pagination`                                                             | [Optional[models.ConnectorPagination]](../models/connectorpagination.md) | :heavy_minus_sign:                                                       | Pagination information for connector lists                               |