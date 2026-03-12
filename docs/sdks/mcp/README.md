# Mcp

## Overview

Model Context Protocol (MCP) endpoints for AI tool integration.

PipesHub exposes a Streamable HTTP MCP server that allows MCP-compatible clients
(such as Claude Desktop, Cursor, or custom agents) to interact with PipesHub tools
including search, conversations, knowledge base management, and connector operations.

**Transport:** Streamable HTTP (JSON-RPC over HTTP)
**Base Path:** `/mcp` (not under `/api/v1`)

**Authentication:**
All MCP requests require a valid Bearer token or OAuth 2.0 access token.

**Stateless Mode:**
The server operates in stateless mode — each request creates an independent MCP session.


### Available Operations

* [handle_mcp_request](#handle_mcp_request) - Handle MCP JSON-RPC request
* [handle_mcp_streaming_request](#handle_mcp_streaming_request) - MCP SSE streaming endpoint

## handle_mcp_request

Main MCP endpoint that handles all JSON-RPC requests including:
- `initialize` — Negotiate capabilities and protocol version
- `tools/list` — List available tools
- `tools/call` — Execute a tool (search, conversations, KB management, etc.)

The server operates in stateless mode with Streamable HTTP transport.
Each request creates an independent MCP server session.


### Example Usage

<!-- UsageSnippet language="python" operationID="handleMCPRequest" method="post" path="/mcp" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.mcp.handle_mcp_request(jsonrpc="2.0", method="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `jsonrpc`                                                           | [models.JsonrpcRequest](../../models/jsonrpcrequest.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `method`                                                            | *str*                                                               | :heavy_check_mark:                                                  | MCP method (e.g. initialize, tools/list, tools/call)                |
| `id`                                                                | [Optional[models.IDRequest]](../../models/idrequest.md)             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `params`                                                            | [Optional[models.Params]](../../models/params.md)                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.HandleMCPRequestResponse](../../models/handlemcprequestresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## handle_mcp_streaming_request

Used by MCP clients for SSE (Server-Sent Events) streaming.
In stateless mode, the transport returns 405 Method Not Allowed
since each request is handled independently via POST.


### Example Usage

<!-- UsageSnippet language="python" operationID="handleMCPStreamingRequest" method="get" path="/mcp" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.mcp.handle_mcp_streaming_request()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |