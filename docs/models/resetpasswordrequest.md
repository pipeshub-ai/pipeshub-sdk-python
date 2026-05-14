# ResetPasswordRequest

Request payload


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `current_password`                                                                     | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `new_password`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `cf_turnstile_response`                                                                | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Cloudflare Turnstile CAPTCHA token (required when Turnstile is configured server-side) |