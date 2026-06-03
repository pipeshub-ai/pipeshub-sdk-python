# ChatAttachmentUploadRef

Concrete attachment metadata returned by `POST /conversations/attachments/upload`
(or the equivalent agent route).



## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `record_id`                                                   | *str*                                                         | :heavy_check_mark:                                            | Server-assigned attachment record id.                         |
| `record_name`                                                 | *str*                                                         | :heavy_check_mark:                                            | Original filename stored for the attachment.                  |
| `mime_type`                                                   | *str*                                                         | :heavy_check_mark:                                            | MIME type of the uploaded file.                               |
| `extension`                                                   | *str*                                                         | :heavy_check_mark:                                            | File extension derived by the backend.                        |
| `virtual_record_id`                                           | *str*                                                         | :heavy_check_mark:                                            | Synthetic record id used by the graph layer.                  |
| `ocr_mode`                                                    | *Optional[str]*                                               | :heavy_minus_sign:                                            | Optional backend-reported processing mode for the attachment. |