# ConnectorIndexingStatusCounts

Number of records in each indexing status.


## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `not_started`              | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `paused`                   | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `in_progress`              | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `completed`                | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `failed`                   | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `file_type_not_supported`  | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `auto_index_off`           | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `empty`                    | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `enable_multimodal_models` | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `queued`                   | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `skipped`                  | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `password_protected`       | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `__pydantic_extra__`       | Dict[str, *int*]           | :heavy_minus_sign:         | N/A                        |