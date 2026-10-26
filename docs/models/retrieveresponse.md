# RetrieveResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `chunks`                                                                     | List[[models.RetrieveChunk](../models/retrievechunk.md)]                     | :heavy_check_mark:                                                           | N/A                                                                          |
| `incomplete`                                                                 | *bool*                                                                       | :heavy_check_mark:                                                           | True when part of the search could not run (for example a source timed out). |
| `message`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Why `chunks` is empty, when it is.                                           |