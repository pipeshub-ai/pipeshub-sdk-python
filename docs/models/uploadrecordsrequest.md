# UploadRecordsRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `kb_id`                                                                  | *str*                                                                    | :heavy_check_mark:                                                       | Knowledge base ID                                                        |
| `folder_id`                                                              | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Target folder ID. Omit to upload to the KB root.                         |
| `body`                                                                   | [models.UploadRecordsRequestBody](../models/uploadrecordsrequestbody.md) | :heavy_check_mark:                                                       | Request payload                                                          |