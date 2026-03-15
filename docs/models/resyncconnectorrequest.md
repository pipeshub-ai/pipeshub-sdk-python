# ResyncConnectorRequest

Request body for Resync connector


## Fields

| Field                          | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `connector_name`               | *str*                          | :heavy_check_mark:             | Connector type name            | GOOGLE_DRIVE                   |
| `connector_id`                 | *str*                          | :heavy_check_mark:             | Connector instance ID          | conn-abc123                    |
| `full_sync`                    | *Optional[bool]*               | :heavy_minus_sign:             | Whether to perform a full sync |                                |