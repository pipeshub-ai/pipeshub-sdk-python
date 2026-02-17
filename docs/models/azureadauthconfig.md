# AzureAdAuthConfig

Azure Active Directory authentication configuration


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `client_id`                                        | *str*                                              | :heavy_check_mark:                                 | Azure AD application client ID                     | 12345678-1234-1234-1234-123456789abc               |
| `tenant_id`                                        | *Optional[str]*                                    | :heavy_minus_sign:                                 | Azure AD tenant ID (use 'common' for multi-tenant) | common                                             |