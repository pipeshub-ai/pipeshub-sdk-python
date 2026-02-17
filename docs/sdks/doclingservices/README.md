# DoclingServices

## Overview

### Available Operations

* [create_blocks](#create_blocks) - [Docling Service] Create blocks from parse result (Phase 2)

## create_blocks

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Phase 2 of two-phase PDF processing - create blocks from parse result.<br><br>

<b>Service:</b> Docling Service<br>
<b>Port:</b> 8081<br>
<b>Base URL:</b> <code>http://localhost:8081</code><br><br>

<b>Authentication:</b> Internal only - called by Indexing Service<br><br>

<b>Note:</b> This endpoint creates content blocks from a previously parsed
PDF document. It may involve LLM calls for table processing.


### Example Usage

<!-- UsageSnippet language="python" operationID="doclingCreateBlocks" method="post" path="/docling/create-blocks" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.docling_services.create_blocks(parse_result="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `parse_result`                                                      | *str*                                                               | :heavy_check_mark:                                                  | JSON-encoded DoclingDocument from /parse-pdf                        |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Optional - process specific page only                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.DoclingCreateBlocksResponse](../../models/doclingcreateblocksresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |