# UpdateTeamUsersPermissionsRequestBody

Request payload


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `user_ids`                                                                                         | List[*str*]                                                                                        | :heavy_minus_sign:                                                                                 | User IDs (legacy format)                                                                           |
| `role`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Role to assign (legacy format)                                                                     |
| `user_roles`                                                                                       | List[[models.UpdateTeamUsersPermissionsUserRole](../models/updateteamuserspermissionsuserrole.md)] | :heavy_minus_sign:                                                                                 | User-role pairs (new format)                                                                       |