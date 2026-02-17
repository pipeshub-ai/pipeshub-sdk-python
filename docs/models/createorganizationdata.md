# CreateOrganizationData


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `organization`                                             | [Optional[models.Organization]](../models/organization.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `admin_user`                                               | [Optional[models.User]](../models/user.md)                 | :heavy_minus_sign:                                         | User account in an organization                            |
| `access_token`                                             | *Optional[str]*                                            | :heavy_minus_sign:                                         | JWT token for immediate login                              |