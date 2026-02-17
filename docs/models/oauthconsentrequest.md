# OAuthConsentRequest

Request to submit user consent for OAuth authorization


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `client_id`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | The OAuth app's client ID                                                |
| `redirect_uri`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | Redirect URI (must match authorization request)                          |
| `scope`                                                                  | *str*                                                                    | :heavy_check_mark:                                                       | Requested scopes                                                         |
| `state`                                                                  | *str*                                                                    | :heavy_check_mark:                                                       | State parameter from authorization request                               |
| `consent`                                                                | [models.Consent](../models/consent.md)                                   | :heavy_check_mark:                                                       | User's consent decision                                                  |
| `code_challenge`                                                         | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | PKCE code challenge (if used in authorization request)                   |
| `code_challenge_method`                                                  | [Optional[models.CodeChallengeMethod]](../models/codechallengemethod.md) | :heavy_minus_sign:                                                       | PKCE challenge method                                                    |