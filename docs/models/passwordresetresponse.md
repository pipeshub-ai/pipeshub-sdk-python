# PasswordResetResponse

Response after successful password reset


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | password reset                                                      |
| `access_token`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New JWT access token (since password change invalidates old tokens) |                                                                     |