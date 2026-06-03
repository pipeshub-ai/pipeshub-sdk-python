# AgentListResponse

Paginated response returned by `GET /agents`.

The Node gateway forwards the Python backend response on success. If
the backend returns a non-200 response, the gateway still returns HTTP
200 with `success: true`, an empty `agents` array, and a zeroed
pagination block derived from the requested `page` / `limit`.



## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `success`                                                      | *bool*                                                         | :heavy_check_mark:                                             | N/A                                                            | true                                                           |
| `agents`                                                       | List[[models.AgentListItem](../models/agentlistitem.md)]       | :heavy_check_mark:                                             | N/A                                                            |                                                                |
| `pagination`                                                   | [models.AgentListPagination](../models/agentlistpagination.md) | :heavy_check_mark:                                             | Pagination block returned by `GET /agents`.                    |                                                                |