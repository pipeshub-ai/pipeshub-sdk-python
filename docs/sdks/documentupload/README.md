# DocumentUpload

## Overview

### Available Operations

* [upload](#upload) - Upload a new document
* [create_placeholder](#create_placeholder) - Create document placeholder
* [get_direct_url](#get_direct_url) - Get direct upload URL

## upload

Upload a new document to PipesHub storage. Supports multiple storage backends including S3, Azure Blob, and local storage.<br><br>
<b>Overview:</b><br>
This endpoint handles document uploads with automatic processing, metadata extraction, and optional versioning. It's the primary endpoint for adding new files to PipesHub.<br><br>
<b>Upload Flow:</b><br>
<ol>
<li>Client sends file with metadata via multipart/form-data</li>
<li>Document metadata saved to database</li>
<li>Returns document object with storage URLs</li>
</ol>
<b>File Size Limits:</b><br>
<ul>
<li><b>Maximum:</b> 1GB (1,073,741,824 bytes)</li>
<li><b>Large file threshold:</b> 10MB (triggers direct upload flow)</li>
</ul>
<b>Supported File Types:</b><br>
<ul>
<li><b>Documents:</b> PDF, DOCX, DOC, XLSX, XLS, PPTX, PPT, TXT, MD, CSV</li>
<li><b>Images:</b> PNG, JPG, JPEG, GIF, WebP, SVG, BMP, TIFF</li>
<li><b>Videos:</b> MP4, AVI, MOV, MKV, WebM</li>
<li><b>Audio:</b> MP3, WAV, FLAC, AAC</li>
<li><b>Archives:</b> ZIP, RAR, 7Z, TAR, GZ</li>
</ul>
<b>Version Control:</b><br>
Set <code>isVersionedFile: "true"</code> to enable version tracking. Versioned documents maintain full history of all changes.<br><br>
<b>Response Headers:</b><br>
<ul>
<li><code>x-document-id</code>: Unique document identifier</li>
<li><code>x-document-name</code>: Document name as stored</li>
</ul>
<b>Storage Backends:</b><br>
Automatically routes to configured storage: Amazon S3, Azure Blob Storage, or Local filesystem.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadDocument" method="post" path="/document/upload" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_upload.upload(document_name="Q4 Financial Report.pdf", is_versioned_file="true", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, document_path="/reports/finance/2024", alternate_document_name="2024-Q4-Finance", permissions="owner", custom_metadata="{\"department\":\"finance\",\"quarter\":\"Q4\"}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `document_name`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | Display name for the document                                                           | Q4 Financial Report.pdf                                                                 |
| `is_versioned_file`                                                                     | [models.IsVersionedFile](../../models/isversionedfile.md)                               | :heavy_check_mark:                                                                      | Enable version control for this document                                                | true                                                                                    |
| `file`                                                                                  | [models.UploadDocumentFile](../../models/uploaddocumentfile.md)                         | :heavy_check_mark:                                                                      | The file to upload (max 1GB)                                                            |                                                                                         |
| `document_path`                                                                         | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Virtual folder path for organization                                                    | /reports/finance/2024                                                                   |
| `alternate_document_name`                                                               | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Alternative name for search/display                                                     | 2024-Q4-Finance                                                                         |
| `permissions`                                                                           | [Optional[models.UploadDocumentPermissions]](../../models/uploaddocumentpermissions.md) | :heavy_minus_sign:                                                                      | Default permission level for shared access                                              |                                                                                         |
| `custom_metadata`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | JSON string of custom key-value metadata                                                | {"department":"finance","quarter":"Q4"}                                                 |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.UploadDocumentResponse](../../models/uploaddocumentresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_placeholder

Create a document metadata record without uploading file content. Used in conjunction with direct upload for large files.<br><br>
<b>Overview:</b><br>
This endpoint creates a document entry in the database without actual file content. The file is then uploaded directly to storage using the <code>/directUpload</code> endpoint.<br><br>
<b>Direct Upload Flow:</b><br>
<ol>
<li>Call this endpoint to create document placeholder</li>
<li>Receive document ID in response</li>
<li>Call <code>/document/{documentId}/directUpload</code> to get presigned URL</li>
<li>Upload file directly to presigned URL</li>
<li>Document becomes accessible once upload completes</li>
</ol>
<b>Use Cases:</b><br>
<ul>
<li>Large file uploads (bypassing server)</li>
<li>Client-side upload progress tracking</li>
<li>Resumable uploads</li>
<li>Reduced server memory usage</li>
</ul>
<b>Note:</b> Extension must be provided without the dot (e.g., "pdf" not ".pdf").


### Example Usage

<!-- UsageSnippet language="python" operationID="createDocumentPlaceholder" method="post" path="/document/placeholder" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_upload.create_placeholder(document_name="Large Video File.mp4", document_path="/videos/training", extension="mp4", permissions="owner", is_versioned_file=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `document_name`                                                                                               | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Display name for the document                                                                                 | Large Video File.mp4                                                                                          |
| `document_path`                                                                                               | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Virtual folder path                                                                                           | /videos/training                                                                                              |
| `extension`                                                                                                   | *str*                                                                                                         | :heavy_check_mark:                                                                                            | File extension WITHOUT dot                                                                                    | mp4                                                                                                           |
| `alternate_document_name`                                                                                     | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | Alternative name for search/display                                                                           |                                                                                                               |
| `permissions`                                                                                                 | [Optional[models.CreateDocumentPlaceholderPermissions]](../../models/createdocumentplaceholderpermissions.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `meta_data`                                                                                                   | [Optional[models.CreateDocumentPlaceholderMetaData]](../../models/createdocumentplaceholdermetadata.md)       | :heavy_minus_sign:                                                                                            | Custom metadata key-value pairs                                                                               |                                                                                                               |
| `is_versioned_file`                                                                                           | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Enable version control                                                                                        |                                                                                                               |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.Document](../../models/document.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_direct_url

Generate a presigned URL for direct client-to-storage upload, bypassing the server for large files.<br><br>
<b>Overview:</b><br>
This endpoint provides a presigned URL that allows clients to upload directly to storage (S3/Azure) without routing through the server. Essential for large file uploads.<br><br>
<b>Direct Upload Flow:</b><br>
<ol>
<li>Create document placeholder with <code>/placeholder</code></li>
<li>Call this endpoint with document ID</li>
<li>Receive presigned URL and document ID</li>
<li>Client uploads file directly to presigned URL (PUT request)</li>
<li>Document becomes available once upload completes</li>
</ol>
<b>Benefits:</b><br>
<ul>
<li>No server memory consumption for large files</li>
<li>Direct transfer to storage (faster)</li>
<li>Client-side progress tracking</li>
<li>Reduced server bandwidth</li>
</ul>
<b>URL Validity:</b><br>
Presigned URLs typically expire after 1 hour. Upload must complete before expiration.<br><br>
<b>Note:</b> Only available for S3 and Azure Blob storage. Local storage does not support direct upload.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDirectUploadUrl" method="post" path="/document/{documentId}/directUpload" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.document_upload.get_direct_url(document_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID from placeholder creation                               | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDirectUploadURLResponse](../../models/getdirectuploadurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |