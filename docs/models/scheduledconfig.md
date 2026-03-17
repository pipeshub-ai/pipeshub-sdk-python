# ScheduledConfig

Configuration for scheduled sync strategy


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `interval_minutes`                      | *Optional[int]*                         | :heavy_minus_sign:                      | Sync interval in minutes                | 60                                      |
| `cron_expression`                       | *Optional[str]*                         | :heavy_minus_sign:                      | Cron expression for advanced scheduling | 0 */6 * * *                             |
| `timezone`                              | *Optional[str]*                         | :heavy_minus_sign:                      | Timezone for scheduled sync             | America/New_York                        |