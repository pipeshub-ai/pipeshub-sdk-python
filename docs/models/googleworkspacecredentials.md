# GoogleWorkspaceCredentials

Google Workspace service account or OAuth credentials


## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `user_type`                                                                                                  | [Optional[models.UserType]](../models/usertype.md)                                                           | :heavy_minus_sign:                                                                                           | Type of credentials: 'individual' for OAuth, 'business' for service account                                  |
| `credentials`                                                                                                | [Optional[models.GoogleWorkspaceCredentialsCredentials]](../models/googleworkspacecredentialscredentials.md) | :heavy_minus_sign:                                                                                           | Credential data (structure depends on userType)                                                              |