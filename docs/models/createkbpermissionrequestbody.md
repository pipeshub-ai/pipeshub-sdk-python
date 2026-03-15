# CreateKBPermissionRequestBody

Request payload


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `user_ids`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | User IDs to grant permission                                         |
| `team_ids`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | Team IDs to grant permission                                         |
| `role`                                                               | [models.CreateKBPermissionRole](../models/createkbpermissionrole.md) | :heavy_check_mark:                                                   | Permission role to grant                                             |