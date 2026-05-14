# AuthProviderAzureAdPublicConfig

Public Azure AD OAuth settings returned to clients


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `tenant_id`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Azure AD tenant ID                                             |
| `client_id`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Azure AD client ID                                             |
| `enable_jit`                                                   | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether just-in-time user provisioning is enabled for Azure AD |