# GetOAuthRegistryResponse

OAuth connector types retrieved


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `success`                                                                  | *bool*                                                                     | :heavy_check_mark:                                                         | N/A                                                                        |
| `connectors`                                                               | List[[models.OAuthRegistryEntry](../models/oauthregistryentry.md)]         | :heavy_check_mark:                                                         | N/A                                                                        |
| `pagination`                                                               | [models.OAuthRegistryPagination](../models/oauthregistrypagination.md)     | :heavy_check_mark:                                                         | Pagination block of `GET /oauth/registry` and `GET /oauth/{connectorType}` |