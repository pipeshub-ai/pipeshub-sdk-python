# OAuthClientManagementRateLimitError

JSON body when OAuth client management routes exceed the per-minute rate limit (same limiter as other `/oauth-clients/*` routes).


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `error`                                                                                                  | [models.OAuthClientManagementRateLimitErrorError](../models/oauthclientmanagementratelimiterrorerror.md) | :heavy_check_mark:                                                                                       | N/A                                                                                                      |