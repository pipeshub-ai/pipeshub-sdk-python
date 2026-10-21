# GetConnectorRegistryResponse

Connector registry retrieved


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `success`                                                                    | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `connectors`                                                                 | List[[models.ConnectorRegistryEntry](../models/connectorregistryentry.md)]   | :heavy_check_mark:                                                           | N/A                                                                          |
| `pagination`                                                                 | [models.ConnectorPagination](../models/connectorpagination.md)               | :heavy_check_mark:                                                           | N/A                                                                          |
| `registry_counts_by_scope`                                                   | [Optional[models.RegistryCountsByScope]](../models/registrycountsbyscope.md) | :heavy_minus_sign:                                                           | How many connector types each scope offers                                   |