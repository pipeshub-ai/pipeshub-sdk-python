# GetUploadLimitsResponse

Upload limits retrieved


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `max_files_per_request`                    | *Optional[int]*                            | :heavy_minus_sign:                         | Maximum number of files per upload request | 1000                                       |
| `max_file_size_bytes`                      | *Optional[int]*                            | :heavy_minus_sign:                         | Maximum file size in bytes (default 30MB)  | 31457280                                   |