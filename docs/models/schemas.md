# Schemas

Auth schemas keyed by auth type (e.g., OAUTH, BASIC_AUTH)


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `oauth`                                                                            | [Optional[models.SchemasOAUTH]](../models/schemasoauth.md)                         | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `basic_auth`                                                                       | [Optional[models.BasicAuth]](../models/basicauth.md)                               | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `api_token`                                                                        | [Optional[models.APIToken]](../models/apitoken.md)                                 | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `oauth_admin_consent`                                                              | [Optional[models.SchemasOAUTHADMINCONSENT]](../models/schemasoauthadminconsent.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `username_password`                                                                | [Optional[models.UsernamePassword]](../models/usernamepassword.md)                 | :heavy_minus_sign:                                                                 | N/A                                                                                |