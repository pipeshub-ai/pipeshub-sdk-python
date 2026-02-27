# DocumentManagement

## Overview

Document CRUD and retrieval operations

### Available Operations

* [download_document](#download_document) - Download document

## download_document

Get a time-limited signed URL to download the document, or receive the file directly for local storage.<br><br>
<b>Overview:</b><br>
This endpoint generates secure download access to documents. For cloud storage (S3/Azure), it returns a presigned URL. For local storage, it streams the file directly.<br><br>
<b>Download Behavior by Storage:</b><br>
<ul>
<li><b>S3/Azure:</b> Returns presigned URL valid for specified duration</li>
<li><b>Local:</b> Streams file directly with appropriate headers</li>
</ul>
<b>Version Download:</b><br>
Specify the <code>version</code> parameter to download a specific historical version. Only available for versioned documents.<br><br>
<b>URL Expiration:</b><br>
<ul>
<li>Default: 3600 seconds (1 hour)</li>
<li>Configurable via <code>expirationTimeInSeconds</code></li>
<li>Maximum depends on storage provider limits</li>
</ul>
<b>Security:</b><br>
Signed URLs are single-use and time-limited. They can be safely shared for temporary access.


### Example Usage

<!-- UsageSnippet language="python" operationID="downloadDocument" method="get" path="/document/{documentId}/download" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as p_client:

    res = p_client.document_management.download_document(document_id="507f1f77bcf86cd799439011", version=2, expiration_time_in_seconds=7200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `document_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | Document ID (24-character MongoDB ObjectId)                               | 507f1f77bcf86cd799439011                                                  |
| `version`                                                                 | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Version number to download (0-indexed). Must be less than total versions. | 2                                                                         |
| `expiration_time_in_seconds`                                              | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Signed URL validity duration in seconds                                   | 7200                                                                      |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.DownloadDocumentResponse](../../models/downloaddocumentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |