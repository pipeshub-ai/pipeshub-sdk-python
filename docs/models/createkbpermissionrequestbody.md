# CreateKBPermissionRequestBody

Request payload


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `user_ids`                                                                 | List[*str*]                                                                | :heavy_check_mark:                                                         | User IDs to grant permission (at least one of userIds or teamIds required) | [<br/>"507f1f77bcf86cd799439011"<br/>]                                     |
| `team_ids`                                                                 | List[*str*]                                                                | :heavy_minus_sign:                                                         | Team IDs to grant permission                                               |                                                                            |
| `role`                                                                     | [models.CreateKBPermissionRole](../models/createkbpermissionrole.md)       | :heavy_check_mark:                                                         | Permission role to grant                                                   | READER                                                                     |