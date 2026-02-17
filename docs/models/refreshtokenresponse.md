# RefreshTokenResponse

Response with new access token


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `user`                                               | [Optional[models.UserBasic]](../models/userbasic.md) | :heavy_minus_sign:                                   | Basic user information                               |
| `access_token`                                       | *Optional[str]*                                      | :heavy_minus_sign:                                   | New JWT access token (1 hour expiry)                 |