# DeleteAgentConversationChatAttachmentRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `agent_key`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | Agent key path parameter. Must be non-empty.                                   |
| `record_id`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | Attachment record id (from the upload response). Must be non-blank after trim. |