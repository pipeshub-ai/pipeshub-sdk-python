# DocumentManagement

## Overview

### Available Operations

* [get_by_id](#get_by_id) - Get document by ID
* [delete_by_id](#delete_by_id) - Delete document
* [download](#download) - Download document

## get_by_id

Retrieve complete document metadata by its unique identifier.<br><br>
<b>Overview:</b><br>
Returns all document information including metadata, version history, storage location, and access permissions. Use this to display document details or prepare for download/edit operations.<br><br>
<b>Response Includes:</b><br>
<ul>
<li>Document metadata (name, path, size, type)</li>
<li>Storage information (vendor, URLs)</li>
<li>Version history (if versioned)</li>
<li>Permission settings</li>
<li>Custom metadata</li>
<li>Timestamps (created, updated)</li>
</ul>
<b>Authorization:</b><br>
Document must belong to the requesting user's organization.<br><br>
<b>Note:</b> Soft-deleted documents (isDeleted: true) are not returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDocumentById" method="get" path="/document/{documentId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_management.get_by_id(document_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID (24-character MongoDB ObjectId)                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDocumentByIDResponse](../../models/getdocumentbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_by_id

Soft delete a document from the system. The document is marked as deleted but not permanently removed.<br><br>
<b>Overview:</b><br>
This endpoint performs a soft delete, marking the document as deleted while preserving its data for potential recovery or audit purposes.<br><br>
<b>What Happens on Delete:</b><br>
<ul>
<li><code>isDeleted</code> flag set to true</li>
<li><code>deletedByUserId</code> recorded</li>
<li>Document excluded from normal queries</li>
<li>File remains in storage (soft delete)</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Document must belong to user's organization</li>
<li>User must have appropriate permissions</li>
</ul>
<b>Recovery:</b><br>
Soft-deleted documents can be restored by administrators if needed.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDocumentById" method="delete" path="/document/{documentId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_management.delete_by_id(document_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID (24-character MongoDB ObjectId)                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteDocumentByIDResponse](../../models/deletedocumentbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## download

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_management.download(document_id="507f1f77bcf86cd799439011", version=2, expiration_time_in_seconds=7200)

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