# ReindexFailedRecordsRequest

Request payload


## Fields

| Field                    | Type                     | Required                 | Description              | Example                  |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `app`                    | *str*                    | :heavy_check_mark:       | Connector type name      | GOOGLE_DRIVE             |
| `connector_id`           | *str*                    | :heavy_check_mark:       | Connector instance ID    | 507f1f77bcf86cd799439011 |
| `status_filters`         | List[*str*]              | :heavy_minus_sign:       | Optional status filters  |                          |