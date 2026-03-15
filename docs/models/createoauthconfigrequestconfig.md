# CreateOAuthConfigRequestConfig

OAuth application credentials


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | OAuth client ID from your OAuth application                         | 123456789-abc.apps.googleusercontent.com                            |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | OAuth client secret (stored encrypted, never returned in responses) | GOCSPX-xxxxxxxxxxxxx                                                |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Azure tenant ID (required only for Microsoft connectors)            | 12345678-1234-1234-1234-123456789abc                                |