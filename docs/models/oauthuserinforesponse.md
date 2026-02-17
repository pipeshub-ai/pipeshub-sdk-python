# OAuthUserInfoResponse

OpenID Connect UserInfo Response.
Contains claims about the authenticated user.



## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `sub`                                      | *str*                                      | :heavy_check_mark:                         | Subject identifier (user ID)               |
| `name`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Full name                                  |
| `given_name`                               | *Optional[str]*                            | :heavy_minus_sign:                         | First name                                 |
| `family_name`                              | *Optional[str]*                            | :heavy_minus_sign:                         | Last name                                  |
| `email`                                    | *Optional[str]*                            | :heavy_minus_sign:                         | Email address                              |
| `email_verified`                           | *Optional[bool]*                           | :heavy_minus_sign:                         | Whether email has been verified            |
| `picture`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | Profile picture URL                        |
| `updated_at`                               | *Optional[int]*                            | :heavy_minus_sign:                         | Last profile update timestamp (Unix epoch) |