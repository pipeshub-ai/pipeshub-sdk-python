# OAuthTokenListItem

Information about an issued token (one element returned by `listTokensForApp`
in `oauth_token.service.ts`). `userId` is omitted for client-credentials access
tokens; all other fields are always populated.



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Token ID                                                             |
| `token_type`                                                         | [models.TokenType](../models/tokentype.md)                           | :heavy_check_mark:                                                   | Type of token                                                        |
| `user_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | User ID (omitted for client-credentials access tokens)               |
| `scopes`                                                             | List[*str*]                                                          | :heavy_check_mark:                                                   | Granted scopes                                                       |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Token creation time                                                  |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Token expiration time                                                |
| `is_revoked`                                                         | *bool*                                                               | :heavy_check_mark:                                                   | Whether token has been revoked                                       |