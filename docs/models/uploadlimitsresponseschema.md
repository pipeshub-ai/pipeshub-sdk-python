# UploadLimitsResponseSchema

Upload constraints returned by GET /knowledgeBase/limits.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `max_files_per_request`                                                      | *int*                                                                        | :heavy_check_mark:                                                           | Maximum number of files per upload request                                   | 1000                                                                         |
| `max_file_size_bytes`                                                        | *int*                                                                        | :heavy_check_mark:                                                           | Maximum file size in bytes (default 30MB when platform settings unavailable) | 31457280                                                                     |