# OAuthTokenListItem

Information about an issued token


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Token ID                                                             |
| `token_type`                                                         | [Optional[models.TokenType]](../models/tokentype.md)                 | :heavy_minus_sign:                                                   | Type of token                                                        |
| `user_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | User ID (if user-based token)                                        |
| `scopes`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Granted scopes                                                       |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Token creation time                                                  |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Token expiration time                                                |
| `is_revoked`                                                         | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether token has been revoked                                       |