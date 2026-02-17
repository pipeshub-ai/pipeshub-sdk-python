# OneDriveConfig

OneDrive/Microsoft 365 connector configuration


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `client_id`                            | *str*                                  | :heavy_check_mark:                     | Microsoft application client ID        |
| `client_secret`                        | *str*                                  | :heavy_check_mark:                     | Microsoft application client secret    |
| `tenant_id`                            | *str*                                  | :heavy_check_mark:                     | Microsoft/Azure tenant ID              |
| `has_admin_consent`                    | *Optional[bool]*                       | :heavy_minus_sign:                     | Whether admin consent has been granted |