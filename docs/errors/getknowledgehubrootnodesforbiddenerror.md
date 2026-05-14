# GetKnowledgeHubRootNodesForbiddenError

Insufficient OAuth scope.

Only applies to OAuth tokens. The token did not carry the `kb:read`
scope required by this endpoint. Regular (non-OAuth) JWT bearer
tokens are not subject to scope enforcement and will not receive
this error.



## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `error`                                                                                                      | [models.GetKnowledgeHubRootNodesErrorHTTPForbidden](../models/getknowledgehubrootnodeserrorhttpforbidden.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |