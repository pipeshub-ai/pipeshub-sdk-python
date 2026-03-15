# HandleMCPRequestRequest

JSON-RPC 2.0 request object


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `jsonrpc`                                            | [models.JsonrpcRequest](../models/jsonrpcrequest.md) | :heavy_check_mark:                                   | N/A                                                  |
| `id`                                                 | [Optional[models.IDRequest]](../models/idrequest.md) | :heavy_minus_sign:                                   | N/A                                                  |
| `method`                                             | *str*                                                | :heavy_check_mark:                                   | MCP method (e.g. initialize, tools/list, tools/call) |
| `params`                                             | [Optional[models.Params]](../models/params.md)       | :heavy_minus_sign:                                   | N/A                                                  |