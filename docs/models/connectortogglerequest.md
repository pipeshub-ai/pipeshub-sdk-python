# ConnectorToggleRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | [models.ConnectorToggleRequestType](../models/connectortogglerequesttype.md) | :heavy_check_mark:                                                           | 'sync' flips data synchronization; 'agent' flips use by agents               |
| `full_sync`                                                                  | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | When turning sync on, start from scratch                                     |
| `device_id`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Local FS only                                                                |
| `device_name`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Local FS only                                                                |