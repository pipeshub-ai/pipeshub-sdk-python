# ConnectorConfigConfig

Configuration sections


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `auth`                                                                         | [Optional[models.Auth]](../models/auth.md)                                     | :heavy_minus_sign:                                                             | Authentication configuration (sensitive data redacted)                         |
| `sync`                                                                         | [Optional[models.ConnectorConfigSync]](../models/connectorconfigsync.md)       | :heavy_minus_sign:                                                             | Sync configuration (schedule, options)                                         |
| `filters`                                                                      | [Optional[models.ConnectorConfigFilters]](../models/connectorconfigfilters.md) | :heavy_minus_sign:                                                             | Filter selections for data scope                                               |