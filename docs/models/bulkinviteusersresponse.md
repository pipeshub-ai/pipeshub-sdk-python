# BulkInviteUsersResponse

Bulk invitation processed


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `success`                                    | *Optional[bool]*                             | :heavy_minus_sign:                           | N/A                                          | true                                         |
| `message`                                    | *Optional[str]*                              | :heavy_minus_sign:                           | N/A                                          | Bulk invitation completed                    |
| `invited`                                    | *Optional[int]*                              | :heavy_minus_sign:                           | Number of successful invitations sent        | 8                                            |
| `skipped`                                    | *Optional[int]*                              | :heavy_minus_sign:                           | Number of existing users skipped             | 1                                            |
| `failed`                                     | *Optional[int]*                              | :heavy_minus_sign:                           | Number of failed invitations                 | 1                                            |
| `failures`                                   | List[[models.Failure](../models/failure.md)] | :heavy_minus_sign:                           | Details of failed invitations                |                                              |