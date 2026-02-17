# SSOAuthConfig

SAML SSO authentication configuration


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `entry_point`                                           | *str*                                                   | :heavy_check_mark:                                      | Identity provider SSO URL                               | https://idp.example.com/sso/saml                        |
| `certificate`                                           | *str*                                                   | :heavy_check_mark:                                      | X.509 certificate for signature validation (PEM format) |                                                         |
| `email_key`                                             | *str*                                                   | :heavy_check_mark:                                      | SAML attribute name for user email                      | email                                                   |