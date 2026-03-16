# MicrosoftAuthConfig

Microsoft authentication configuration


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `client_id`                              | *Optional[str]*                          | :heavy_minus_sign:                       | Microsoft application client ID          | 12345678-1234-1234-1234-123456789abc     |
| `tenant_id`                              | *Optional[str]*                          | :heavy_minus_sign:                       | Microsoft tenant ID                      |                                          |
| `authority`                              | *Optional[str]*                          | :heavy_minus_sign:                       | Microsoft authority URL                  | https://login.microsoftonline.com/common |
| `enable_jit`                             | *Optional[bool]*                         | :heavy_minus_sign:                       | Enable Just-In-Time user provisioning    |                                          |