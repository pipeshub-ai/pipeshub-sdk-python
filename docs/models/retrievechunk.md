# RetrieveChunk


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Stable for the same indexed block, for deduplication and caching.  |
| `text`                                                             | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `score`                                                            | *OptionalNullable[float]*                                          | :heavy_minus_sign:                                                 | N/A                                                                |
| `record`                                                           | [models.RetrieveChunkRecord](../models/retrievechunkrecord.md)     | :heavy_check_mark:                                                 | N/A                                                                |
| `citation`                                                         | [models.RetrieveChunkCitation](../models/retrievechunkcitation.md) | :heavy_check_mark:                                                 | N/A                                                                |