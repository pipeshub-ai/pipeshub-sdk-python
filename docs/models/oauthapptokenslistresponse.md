# OAuthAppTokensListResponse

Response body for `GET /oauth-clients/{appId}/tokens` (`listAppTokens`).



## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `tokens`                                                           | List[[models.OAuthTokenListItem](../models/oauthtokenlistitem.md)] | :heavy_check_mark:                                                 | Active access and refresh tokens for the app                       |