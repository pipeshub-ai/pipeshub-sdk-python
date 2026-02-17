# CreateConnectorRequestConfig

Initial configuration (can also be set after creation)


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `auth`                                                                                  | [Optional[models.ConnectorAuthConfig]](../models/connectorauthconfig.md)                | :heavy_minus_sign:                                                                      | Authentication configuration for a connector instance                                   |
| `sync`                                                                                  | [Optional[models.ConnectorSyncConfig]](../models/connectorsyncconfig.md)                | :heavy_minus_sign:                                                                      | Synchronization configuration for a connector instance                                  |
| `filters`                                                                               | [Optional[models.ConnectorFiltersConfig]](../models/connectorfiltersconfig.md)          | :heavy_minus_sign:                                                                      | Filter configuration to control what data is synced (sync filters and indexing filters) |