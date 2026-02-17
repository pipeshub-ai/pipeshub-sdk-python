# KnowledgeBase


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `key`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Unique knowledge base identifier                           |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | Name of the knowledge base                                 |
| `org_id`                                                   | *str*                                                      | :heavy_check_mark:                                         | Organization ID                                            |
| `created_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | Creation timestamp                                         |
| `updated_at_timestamp`                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | Last update timestamp                                      |
| `user_role`                                                | [Optional[models.UserRoleEnum]](../models/userroleenum.md) | :heavy_minus_sign:                                         | User's role in this knowledge base                         |
| `is_deleted`                                               | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the knowledge base is deleted                      |