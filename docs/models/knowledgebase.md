# KnowledgeBase


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *Optional[str]*                                            | :heavy_minus_sign:                                         | Unique knowledge base identifier                           |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | Name of the knowledge base                                 |
| `connector_id`                                             | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | Associated connector ID (null for manual KBs)              |
| `created_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | Creation timestamp in milliseconds                         |
| `updated_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | Last update timestamp in milliseconds                      |
| `created_by`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | User ID of the creator                                     |
| `user_role`                                                | [Optional[models.UserRoleEnum]](../models/userroleenum.md) | :heavy_minus_sign:                                         | User's role in this knowledge base                         |
| `folders`                                                  | List[[models.Folder](../models/folder.md)]                 | :heavy_minus_sign:                                         | Folders in this knowledge base                             |