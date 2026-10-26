# AuthProviders

Configuration for external authentication providers (returned when those methods are allowed)


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `google`                                                                                             | [Optional[models.AuthProviderGooglePublicConfig]](../models/authprovidergooglepublicconfig.md)       | :heavy_minus_sign:                                                                                   | Public Google OAuth settings returned to clients                                                     |
| `microsoft`                                                                                          | [Optional[models.AuthProviderMicrosoftPublicConfig]](../models/authprovidermicrosoftpublicconfig.md) | :heavy_minus_sign:                                                                                   | Public Microsoft OAuth settings returned to clients                                                  |