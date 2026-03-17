# SSOAuthConfig

SAML SSO authentication configuration


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `certificate`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | X.509 certificate for signature validation (PEM format) |
| `entry_point`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | Identity provider SSO URL                               |
| `email_key`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | SAML attribute name for user email                      |
| `enable_jit`                                            | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Enable Just-In-Time user provisioning                   |