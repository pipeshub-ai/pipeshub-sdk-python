# ForgotPasswordRequest

Request to send password reset email


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `email`                                       | *str*                                         | :heavy_check_mark:                            | Email address to send reset link to           |
| `cf_turnstile_response`                       | *Optional[str]*                               | :heavy_minus_sign:                            | Cloudflare Turnstile CAPTCHA token (optional) |