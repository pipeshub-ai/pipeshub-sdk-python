# GetOAuthAuthorizationURLResponse

Provider consent URL


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `success`                                          | *bool*                                             | :heavy_check_mark:                                 | N/A                                                |
| `authorization_url`                                | *str*                                              | :heavy_check_mark:                                 | Open in a browser to give consent                  |
| `state`                                            | *str*                                              | :heavy_check_mark:                                 | Pass back with the provider's code to the callback |