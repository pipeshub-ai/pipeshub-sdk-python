# MicrosoftAuthConfig

Microsoft authentication configuration


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `client_id`                                  | *str*                                        | :heavy_check_mark:                           | Microsoft application client ID              |                                              |
| `tenant_id`                                  | *Optional[str]*                              | :heavy_minus_sign:                           | Microsoft tenant ID                          |                                              |
| `authority`                                  | *Optional[str]*                              | :heavy_minus_sign:                           | Microsoft authority URL                      | https://login.microsoftonline.com/{tenantId} |
| `enable_jit`                                 | *Optional[bool]*                             | :heavy_minus_sign:                           | Enable Just-In-Time user provisioning        |                                              |