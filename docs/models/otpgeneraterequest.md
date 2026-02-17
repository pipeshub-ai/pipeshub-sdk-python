# OtpGenerateRequest

Request to generate and send OTP


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `email`                                       | *str*                                         | :heavy_check_mark:                            | Email address to send OTP to                  |
| `cf_turnstile_response`                       | *Optional[str]*                               | :heavy_minus_sign:                            | Cloudflare Turnstile CAPTCHA token (optional) |