# ConnectorFiltersConfig

Filter configuration to control what data is synced (sync filters and indexing filters)


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `sync`                                                                                 | [Optional[models.ConnectorFiltersConfigSync]](../models/connectorfiltersconfigsync.md) | :heavy_minus_sign:                                                                     | Sync filter selections                                                                 |
| `indexing`                                                                             | [Optional[models.Indexing]](../models/indexing.md)                                     | :heavy_minus_sign:                                                                     | Indexing filter selections                                                             |