# RegenerateOAuthAppSecretResponse

Response body for `POST /oauth-clients/{appId}/regenerate-secret` (`regenerateSecret`).



## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `message`                                                          | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | Client secret regenerated successfully                             |
| `client_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | OAuth client ID (unchanged)                                        |                                                                    |
| `client_secret`                                                    | *str*                                                              | :heavy_check_mark:                                                 | New client secret (store securely; previous secret is invalidated) |                                                                    |