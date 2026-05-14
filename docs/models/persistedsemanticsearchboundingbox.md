# PersistedSemanticSearchBoundingBox

Bounding box subdocument embedded in persisted citation metadata.
`boundingBoxSchema` does not set `_id: false`, so Mongoose auto-injects an `_id`.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `x`                | *float*            | :heavy_check_mark: | N/A                |
| `y`                | *float*            | :heavy_check_mark: | N/A                |