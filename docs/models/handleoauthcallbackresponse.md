# HandleOAuthCallbackResponse

Result of exchanging the code. `success` is false when the provider refused it.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `success`                                  | *bool*                                     | :heavy_check_mark:                         | N/A                                        |
| `redirect_url`                             | *Optional[str]*                            | :heavy_minus_sign:                         | Where the web app would send the user next |
| `error`                                    | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `error_message`                            | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |