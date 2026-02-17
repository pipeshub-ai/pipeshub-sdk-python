# DocumentBuffer

## Overview

### Available Operations

* [update](#update) - Update document buffer

## update

Replace the document's file content with a new file. Updates the current version without creating version history.<br><br>
<b>Overview:</b><br>
This endpoint replaces the document's content in storage. Use this for quick updates that don't need version tracking.<br><br>
<b>When to Use:</b><br>
<ul>
<li>Updating draft documents</li>
<li>Replacing temporary files</li>
<li>Quick fixes without version history</li>
</ul>
<b>For Version Tracking:</b><br>
Use <code>/uploadNextVersion</code> instead if you need to maintain version history.<br><br>
<b>File Constraints:</b><br>
<ul>
<li>Maximum size: 100MB</li>
<li>File extension must match original document</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Increments <code>mutationCount</code></li>
<li>Updates <code>sizeInBytes</code></li>
<li>Updates <code>updatedAt</code> timestamp</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateDocumentBuffer" method="put" path="/document/{documentId}/buffer" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_buffer.update(document_id="507f1f77bcf86cd799439011", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `document_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | Document ID (24-character MongoDB ObjectId)                                 | 507f1f77bcf86cd799439011                                                    |
| `file`                                                                      | [models.UpdateDocumentBufferFile](../../models/updatedocumentbufferfile.md) | :heavy_check_mark:                                                          | New file content (max 100MB)                                                |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.UpdateDocumentBufferResponse](../../models/updatedocumentbufferresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |