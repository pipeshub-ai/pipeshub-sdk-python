# UpdateOAuthConfigResponse

OAuth configuration updated


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `success`                                                                                                   | *Optional[bool]*                                                                                            | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `oauth_config`                                                                                              | [Optional[models.OAuthConfig]](../models/oauthconfig.md)                                                    | :heavy_minus_sign:                                                                                          | OAuth configuration for a connector type. Created by admins to enable<br/>OAuth authentication for connectors.<br/> |