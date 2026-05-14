# AuthenticatedPasswordResetResponse

Response after authenticated user changes password (new access token issued)


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `data`                                     | *str*                                      | :heavy_check_mark:                         | N/A                                        | password reset                             |
| `access_token`                             | *str*                                      | :heavy_check_mark:                         | New JWT access token after password change |                                            |