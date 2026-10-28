# DeleteConnectorInstanceResponse

Deletion accepted. The connector is marked `DELETING` and removed in
the background, so a `GET` shortly afterwards answers `404`.



## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `success`                                                                          | *bool*                                                                             | :heavy_check_mark:                                                                 | N/A                                                                                |                                                                                    |
| `message`                                                                          | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                | Connector deletion initiated                                                       |
| `connector_id`                                                                     | *str*                                                                              | :heavy_check_mark:                                                                 | ID of the connector being deleted                                                  |                                                                                    |
| `status`                                                                           | [models.DeleteConnectorInstanceStatus](../models/deleteconnectorinstancestatus.md) | :heavy_check_mark:                                                                 | N/A                                                                                |                                                                                    |