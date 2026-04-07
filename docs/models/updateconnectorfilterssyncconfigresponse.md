# UpdateConnectorFiltersSyncConfigResponse

Configuration updated


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `success`                                                                        | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |
| `config`                                                                         | [Optional[models.ConnectorConfig]](../models/connectorconfig.md)                 | :heavy_minus_sign:                                                               | Configuration for a connector instance including auth, sync, and filter settings |
| `message`                                                                        | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Success message                                                                  |
| `sync_filters_changed`                                                           | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Indicates whether sync filters changed, requiring a full resync                  |