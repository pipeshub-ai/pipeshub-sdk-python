# GoogleWorkspaceOAuthConfig

Google Workspace OAuth configuration for connectors


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `client_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Google OAuth client ID                                                |
| `client_secret`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | Google OAuth client secret                                            |
| `enable_real_time_updates`                                            | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Enable Google Pub/Sub for real-time updates                           |
| `topic_name`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Google Pub/Sub topic name (required if enableRealTimeUpdates is true) |