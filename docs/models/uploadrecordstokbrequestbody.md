# UploadRecordsToKBRequestBody

Request payload


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `files`                                                                   | List[[models.UploadRecordsToKBFile](../models/uploadrecordstokbfile.md)]  | :heavy_check_mark:                                                        | Files to upload (max 1000)                                                |                                                                           |
| `files_metadata`                                                          | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | JSON array with file_path and last_modified for each file                 | [{"file_path":"/docs/report.pdf","last_modified":"2024-01-15T10:30:00Z"}] |
| `is_versioned`                                                            | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Enable version tracking                                                   |                                                                           |
| `record_type`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Type of records to create                                                 |                                                                           |