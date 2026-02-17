# MoveRecordRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `kb_id`                                                            | *str*                                                              | :heavy_check_mark:                                                 | Knowledge base ID                                                  |
| `record_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | Record ID to move                                                  |
| `body`                                                             | [models.MoveRecordRequestBody](../models/moverecordrequestbody.md) | :heavy_check_mark:                                                 | Target parent folder for the record                                |