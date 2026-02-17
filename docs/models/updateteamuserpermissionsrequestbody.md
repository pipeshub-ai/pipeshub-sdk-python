# UpdateTeamUserPermissionsRequestBody

Request payload


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `user_id`                                                                          | *str*                                                                              | :heavy_check_mark:                                                                 | ID of the user whose role to update                                                | 507f1f77bcf86cd799439012                                                           |
| `role`                                                                             | [models.UpdateTeamUserPermissionsRole](../models/updateteamuserpermissionsrole.md) | :heavy_check_mark:                                                                 | New role to assign to the user                                                     | admin                                                                              |