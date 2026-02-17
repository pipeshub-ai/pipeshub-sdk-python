# AuthenticateRequest

Request to authenticate using specified method.
**Credential format varies by method:**
- `password`: `{ password: "string" }`
- `otp`: `{ otp: "123456" }` (6-digit code)
- `google`: `"google-id-token-string"`
- `microsoft`: `{ accessToken: "...", idToken: "..." }`
- `azureAd`: `{ accessToken: "...", idToken: "..." }`
- `oauth`: `{ accessToken: "...", idToken: "..." }`
- `samlSso`: handled via redirect flow



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `method`                                                             | [models.Method](../models/method.md)                                 | :heavy_check_mark:                                                   | Authentication method to use                                         |
| `credentials`                                                        | [models.Credentials](../models/credentials.md)                       | :heavy_check_mark:                                                   | Credentials based on the authentication method                       |
| `email`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional email for verification (used with some OAuth methods)       |
| `cf_turnstile_response`                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Cloudflare Turnstile CAPTCHA token (optional, if CAPTCHA is enabled) |