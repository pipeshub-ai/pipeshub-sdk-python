# DocumentBuffers

## Overview

### Available Operations

* [get](#get) - Get document buffer

## get

Retrieve the raw binary content of a document as a buffer. Used for in-memory document processing.<br><br>
<b>Overview:</b><br>
Returns the complete file content as a binary buffer. This is useful for server-side document processing, content analysis, or format conversion.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Document parsing and text extraction</li>
<li>Format conversion pipelines</li>
<li>Content analysis and indexing</li>
<li>Thumbnail generation</li>
</ul>
<b>Version Support:</b><br>
Specify <code>version</code> to get a specific historical version's content.<br><br>
<b>Memory Considerations:</b><br>
Large files will consume significant memory. For files &gt;100MB, consider using streaming download instead.<br><br>
<b>Response Format:</b><br>
Returns Node.js Buffer object serialized as JSON with type and data array.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDocumentBuffer" method="get" path="/document/{documentId}/buffer" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_buffers.get(document_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID (24-character MongoDB ObjectId)                         | 507f1f77bcf86cd799439011                                            |
| `version`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Version number to retrieve (0-indexed)                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |