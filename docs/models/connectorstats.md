# ConnectorStats

Statistics for a connector's records


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `connector_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `total_records`    | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `indexed_records`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `failed_records`   | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `pending_records`  | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `last_sync_time`   | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `status_breakdown` | Dict[str, *int*]   | :heavy_minus_sign: | N/A                |