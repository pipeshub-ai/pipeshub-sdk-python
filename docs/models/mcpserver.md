# McpServer

MCP server instance linked to an agent, as projected by the graph
store on `GET /agents/{agentKey}` and `GET /agents` — same shape as
`Toolset`. MCP server nodes carry no secrets, only the attach-time
snapshot of `instanceId`/`typeId`/`name`.



## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `key`                                                                       | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | MCP server instance node key in the backing graph store.                    |
| `name`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | MCP server attachment name (attach-time snapshot).                          |
| `display_name`                                                              | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Human-readable MCP server product label (for example `Jira MCP`).           |
| `type_id`                                                                   | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Catalog server type id, when this instance came from a registered template. |
| `instance_id`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Admin-created MCP server instance id.                                       |
| `tools`                                                                     | List[[models.McpServerTool](../models/mcpservertool.md)]                    | :heavy_minus_sign:                                                          | N/A                                                                         |