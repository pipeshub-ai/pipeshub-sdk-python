# ConversationSharedBy

Present on conversations the caller received via share. Identifies the
conversation initiator (the only user who can share a chat).



## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `user_id`                                          | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Display name, falling back to email or the user id |