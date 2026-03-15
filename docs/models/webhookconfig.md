# WebhookConfig

Configuration for webhook-based sync


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `webhook_url`                                       | *Optional[str]*                                     | :heavy_minus_sign:                                  | URL to receive webhook events (auto-generated)      |                                                     |
| `events`                                            | List[*str*]                                         | :heavy_minus_sign:                                  | Subscribed event types                              | [<br/>"file.created",<br/>"file.modified",<br/>"file.deleted"<br/>] |