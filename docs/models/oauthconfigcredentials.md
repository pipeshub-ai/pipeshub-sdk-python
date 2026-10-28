# OAuthConfigCredentials

The credentials stored for an OAuth configuration, exactly as the admin submitted them and
not masked. The keys are the `name` of each entry in the connector type's `authFields`
(see `GET /oauth/registry/{connectorType}`), so they differ from one connector type to the next.
Create and update do not check the values, so any JSON value that was sent (a number,
`null`, a nested object, an array of any items) is stored and returned here as it was sent,
even for `clientId` and `clientSecret`.



## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                       | [OptionalNullable[models.OAuthConfigCredentialValue]](../models/oauthconfigcredentialvalue.md)    | :heavy_minus_sign:                                                                                | OAuth client ID; a string unless something else was sent                                          |
| `client_secret`                                                                                   | [OptionalNullable[models.OAuthConfigCredentialValue]](../models/oauthconfigcredentialvalue.md)    | :heavy_minus_sign:                                                                                | OAuth client secret, in clear text; a string unless something else was sent                       |
| `tenant_id`                                                                                       | [OptionalNullable[models.OAuthConfigCredentialValue]](../models/oauthconfigcredentialvalue.md)    | :heavy_minus_sign:                                                                                | Directory (tenant) ID, for Microsoft connector types; a string unless something else was sent     |
| `__pydantic_extra__`                                                                              | Dict[str, [Nullable[models.OAuthConfigCredentialValue]](../models/oauthconfigcredentialvalue.md)] | :heavy_minus_sign:                                                                                | N/A                                                                                               |