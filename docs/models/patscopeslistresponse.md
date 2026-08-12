# PatScopesListResponse

Response body for `GET /personal-access-tokens/scopes` (`listScopes`).
Unlike `GET /oauth-clients/scopes`, this is a **flat array**, not
grouped by category, and reflects the org's configured `MCP_SCOPES`
rather than the full role-aware OAuth-app scope catalog.



## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `scopes`                                                   | List[[models.OAuthScopeInfo](../models/oauthscopeinfo.md)] | :heavy_check_mark:                                         | N/A                                                        |