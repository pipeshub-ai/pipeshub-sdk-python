# CreateConnectorInstanceResponse

Connector instance created. It is not syncing yet.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `success`                                                | *bool*                                                   | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `connector`                                              | [models.ConnectorCreated](../models/connectorcreated.md) | :heavy_check_mark:                                       | Summary of a connector instance that was just created    |                                                          |
| `message`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | Connector instance created successfully.                 |