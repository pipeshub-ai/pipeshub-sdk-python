# OAuthRevokeRequest

OAuth 2.0 Token Revocation Request (RFC 7009).
Revokes an access or refresh token.



## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `token`                                                                                          | *str*                                                                                            | :heavy_check_mark:                                                                               | The token to revoke                                                                              |
| `token_type_hint`                                                                                | [Optional[models.OAuthRevokeRequestTokenTypeHint]](../models/oauthrevokerequesttokentypehint.md) | :heavy_minus_sign:                                                                               | Hint about token type (optional, improves performance)                                           |
| `client_id`                                                                                      | *str*                                                                                            | :heavy_check_mark:                                                                               | Client ID                                                                                        |
| `client_secret`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Client secret                                                                                    |