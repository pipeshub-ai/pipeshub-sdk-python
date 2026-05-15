# GetAvailableModelsByTypeForbiddenError

Insufficient OAuth scope.

Only applies to OAuth tokens. The token did not carry the `config:read`
scope required by this endpoint. Regular (non-OAuth) JWT bearer tokens
are not subject to scope enforcement and will not receive this error.



## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `error`                                                                                                      | [models.GetAvailableModelsByTypeErrorHTTPForbidden](../models/getavailablemodelsbytypeerrorhttpforbidden.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |