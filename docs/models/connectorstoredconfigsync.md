# ConnectorStoredConfigSync

Sync strategy plus connector-specific sync settings


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `selected_strategy`                                  | *Optional[str]*                                      | :heavy_minus_sign:                                   | `MANUAL`, `SCHEDULED` or `WEBHOOK`                   |
| `scheduled_config`                                   | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | Schedule used when `selectedStrategy` is `SCHEDULED` |
| `custom_values`                                      | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | Values of the connector's own sync fields            |
| `__pydantic_extra__`                                 | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | N/A                                                  |