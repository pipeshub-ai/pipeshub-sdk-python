# ChatAttachmentRef

Reference to an attachment produced by `POST /conversations/attachments/upload`
(or the equivalent agent route). Include in create/stream/message bodies
so the turn is sent with uploaded files.



## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `record_id`                                             | *str*                                                   | :heavy_check_mark:                                      | Attachment record id returned from the upload endpoint. |
| `record_name`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | Original display name of the file when known.           |
| `mime_type`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | MIME type of the uploaded file.                         |
| `extension`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | File extension (e.g. `pdf`).                            |
| `virtual_record_id`                                     | *Optional[str]*                                         | :heavy_minus_sign:                                      | Optional synthetic record id used by the graph layer.   |