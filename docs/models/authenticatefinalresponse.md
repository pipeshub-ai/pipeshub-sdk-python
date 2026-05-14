# AuthenticateFinalResponse

All authentication steps complete; JWT tokens returned


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `message`                         | *str*                             | :heavy_check_mark:                | Success message                   | Fully authenticated               |
| `access_token`                    | *str*                             | :heavy_check_mark:                | JWT access token (1 hour expiry)  |                                   |
| `refresh_token`                   | *str*                             | :heavy_check_mark:                | JWT refresh token (7 days expiry) |                                   |