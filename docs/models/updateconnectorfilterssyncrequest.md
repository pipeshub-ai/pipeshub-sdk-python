# UpdateConnectorFiltersSyncRequest

Request to update filters and sync config (connector must be authenticated and inactive)


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `sync`                                                                                  | [Optional[models.ConnectorSyncConfig]](../models/connectorsyncconfig.md)                | :heavy_minus_sign:                                                                      | Synchronization configuration for a connector instance                                  |
| `filters`                                                                               | [Optional[models.ConnectorFiltersConfig]](../models/connectorfiltersconfig.md)          | :heavy_minus_sign:                                                                      | Filter configuration to control what data is synced (sync filters and indexing filters) |
| `base_url`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |