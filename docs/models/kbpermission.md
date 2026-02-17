# KBPermission


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `user_id`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | User ID                                                            |
| `team_id`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Team ID                                                            |
| `role`                                                             | [Optional[models.KBPermissionRole]](../models/kbpermissionrole.md) | :heavy_minus_sign:                                                 | Permission role                                                    |
| `kb_id`                                                            | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Knowledge base ID                                                  |
| `granted_by`                                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | User ID who granted the permission                                 |
| `granted_at`                                                       | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Timestamp when permission was granted                              |