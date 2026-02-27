# ListConnectorInstancesRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `scope`                                              | [models.ConnectorScope](../models/connectorscope.md) | :heavy_check_mark:                                   | Filter by scope (team or personal)                   | team                                                 |
| `page`                                               | *Optional[int]*                                      | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `limit`                                              | *Optional[int]*                                      | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `search`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | Search by instance name                              |                                                      |