# FeatureFlag

Platform feature flag definition


## Fields

| Field                    | Type                     | Required                 | Description              | Example                  |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `key`                    | *Optional[str]*          | :heavy_minus_sign:       | Unique feature flag key  | ENABLE_BETA_CONNECTORS   |
| `label`                  | *Optional[str]*          | :heavy_minus_sign:       | Display label            | Enable Beta Connectors   |
| `description`            | *Optional[str]*          | :heavy_minus_sign:       | Feature flag description |                          |
| `default_enabled`        | *Optional[bool]*         | :heavy_minus_sign:       | Default enabled state    |                          |