# OAuthIntrospectRequest

OAuth 2.0 Token Introspection Request (RFC 7662).
Check if a token is active and get its metadata.



## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `token`                                                                                                  | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The token to introspect                                                                                  |
| `token_type_hint`                                                                                        | [Optional[models.OAuthIntrospectRequestTokenTypeHint]](../models/oauthintrospectrequesttokentypehint.md) | :heavy_minus_sign:                                                                                       | Hint about token type                                                                                    |
| `client_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Client ID                                                                                                |
| `client_secret`                                                                                          | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | Client secret                                                                                            |