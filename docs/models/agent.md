# Agent

A custom AI agent with specialized capabilities, tools, and knowledge scope.
Agents can be configured for specific use cases like customer support,
code review, or domain-specific Q&A.



## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *Optional[str]*                                  | :heavy_minus_sign:                               | Full document ID (collection/key)                |                                                  |
| `key`                                            | *Optional[str]*                                  | :heavy_minus_sign:                               | Unique document key                              |                                                  |
| `rev`                                            | *Optional[str]*                                  | :heavy_minus_sign:                               | Document revision (ArangoDB)                     |                                                  |
| `name`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | Display name of the agent                        | Product Support Agent                            |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | What this agent is designed to do                |                                                  |
| `system_prompt`                                  | *Optional[str]*                                  | :heavy_minus_sign:                               | System instructions that define agent behavior   |                                                  |
| `start_message`                                  | *Optional[str]*                                  | :heavy_minus_sign:                               | Initial greeting shown when conversation starts  |                                                  |
| `instructions`                                   | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Additional agent execution instructions          |                                                  |
| `models`                                         | List[[models.Model](../models/model.md)]         | :heavy_minus_sign:                               | Model configuration entries                      |                                                  |
| `tags`                                           | List[*str*]                                      | :heavy_minus_sign:                               | Tags for categorization                          |                                                  |
| `is_active`                                      | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether the agent is active                      |                                                  |
| `is_deleted`                                     | *Optional[bool]*                                 | :heavy_minus_sign:                               | Soft delete flag                                 |                                                  |
| `share_with_org`                                 | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether agent is shared with the organization    |                                                  |
| `toolsets`                                       | List[[models.Toolset](../models/toolset.md)]     | :heavy_minus_sign:                               | Toolsets attached to the agent                   |                                                  |
| `knowledge`                                      | List[[models.Knowledge](../models/knowledge.md)] | :heavy_minus_sign:                               | Knowledge sources connected to the agent         |                                                  |
| `created_by`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | User key who created the agent                   |                                                  |
| `updated_by`                                     | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | User key who last updated the agent              |                                                  |
| `created_at_timestamp`                           | *Optional[int]*                                  | :heavy_minus_sign:                               | Creation timestamp in milliseconds               |                                                  |
| `updated_at_timestamp`                           | *Optional[int]*                                  | :heavy_minus_sign:                               | Last update timestamp in milliseconds            |                                                  |
| `can_view`                                       | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether current user can view this agent         |                                                  |
| `can_share`                                      | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether current user can share this agent        |                                                  |
| `can_edit`                                       | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether current user can edit this agent         |                                                  |
| `can_delete`                                     | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether current user can delete this agent       |                                                  |
| `user_role`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Current user's role on this agent                | OWNER                                            |
| `access_type`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | How the user has access to this agent            | INDIVIDUAL                                       |