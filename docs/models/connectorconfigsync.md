# ConnectorConfigSync

Sync configuration


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `selected_strategy`                                                                            | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Selected sync strategy                                                                         |
| `scheduled_config`                                                                             | [Optional[models.ConnectorConfigScheduledConfig]](../models/connectorconfigscheduledconfig.md) | :heavy_minus_sign:                                                                             | Scheduled sync configuration                                                                   |
| `webhook_config`                                                                               | [Optional[models.ConnectorConfigWebhookConfig]](../models/connectorconfigwebhookconfig.md)     | :heavy_minus_sign:                                                                             | Webhook configuration                                                                          |