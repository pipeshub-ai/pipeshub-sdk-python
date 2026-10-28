# ConnectorStoredConfig

A connector instance's saved settings. Secret auth fields come back masked; saving the mask back keeps the stored value. Provider OAuth tokens are never returned.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `auth`                                                                                     | [Optional[models.ConnectorStoredConfigAuth]](../models/connectorstoredconfigauth.md)       | :heavy_minus_sign:                                                                         | Auth fields for the instance's auth type, keyed by field name                              |
| `sync`                                                                                     | [Optional[models.ConnectorStoredConfigSync]](../models/connectorstoredconfigsync.md)       | :heavy_minus_sign:                                                                         | Sync strategy plus connector-specific sync settings                                        |
| `filters`                                                                                  | [Optional[models.ConnectorStoredConfigFilters]](../models/connectorstoredconfigfilters.md) | :heavy_minus_sign:                                                                         | Saved filter selections                                                                    |