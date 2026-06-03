# ChatAttachmentUploadResponse

Success envelope returned by `POST /conversations/attachments/upload`
and `POST /agents/{agentKey}/conversations/attachments/upload`.



## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                        | *Nullable[str]*                                                                                          | :heavy_check_mark:                                                                                       | Existing conversation id echoed from the request when the upload is tied to a thread; otherwise `null`.<br/> |
| `attachments`                                                                                            | List[[models.ChatAttachmentUploadRef](../models/chatattachmentuploadref.md)]                             | :heavy_check_mark:                                                                                       | N/A                                                                                                      |