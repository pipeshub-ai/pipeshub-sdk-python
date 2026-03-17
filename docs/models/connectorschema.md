# ConnectorSchema

Schema definition for configuring a connector type


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `connector_type`                                           | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `auth_schema`                                              | [Optional[models.AuthSchema]](../models/authschema.md)     | :heavy_minus_sign:                                         | JSON Schema for authentication fields                      |
| `sync_schema`                                              | [Optional[models.SyncSchema]](../models/syncschema.md)     | :heavy_minus_sign:                                         | JSON Schema for sync configuration                         |
| `filter_schema`                                            | [Optional[models.FilterSchema]](../models/filterschema.md) | :heavy_minus_sign:                                         | JSON Schema for filter options                             |
| `required_fields`                                          | List[*str*]                                                | :heavy_minus_sign:                                         | Required field names                                       |