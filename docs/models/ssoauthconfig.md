# SSOAuthConfig

SAML SSO authentication configuration


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `certificate`                                           | *str*                                                   | :heavy_check_mark:                                      | X.509 certificate for signature validation (PEM format) |
| `entry_point`                                           | *str*                                                   | :heavy_check_mark:                                      | Identity provider SSO URL                               |
| `email_key`                                             | *str*                                                   | :heavy_check_mark:                                      | SAML attribute name for user email                      |
| `enable_jit`                                            | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Enable Just-In-Time user provisioning                   |