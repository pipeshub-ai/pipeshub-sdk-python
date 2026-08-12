# ListPatResponse

Response body for `GET /personal-access-tokens` (`listTokens`) — the
caller's own active tokens, capped at 100 most-recent server-side.
Unlike the admin list, this is a flat array with no pagination
envelope and no owner fields (it's implicitly scoped to the caller).



## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `tokens`                                             | List[[models.PatListItem](../models/patlistitem.md)] | :heavy_check_mark:                                   | N/A                                                  |