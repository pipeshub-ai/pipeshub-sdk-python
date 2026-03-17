# SSOAuthConfig

SAML SSO authentication configuration


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `entry_point`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | Identity provider SSO URL                               | https://idp.example.com/sso/saml                        |
| `certificate`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | X.509 certificate for signature validation (PEM format) |                                                         |
| `email_key`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | SAML attribute name for user email                      | email                                                   |