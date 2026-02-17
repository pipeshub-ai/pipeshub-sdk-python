# Upload

## Overview

File upload operations

### Available Operations

* [to_knowledge_base](#to_knowledge_base) - Upload files to knowledge base
* [records_to_folder](#records_to_folder) - Upload files to folder

## to_knowledge_base

Upload one or more files directly to a knowledge base.<br><br>
<b>Overview:</b><br>
Batch upload multiple files in a single request. Each file becomes a new record in the KB with automatic content indexing.<br><br>
<b>Upload Limits:</b><br>
<ul>
<li><b>Max files per request:</b> 1000</li>
<li><b>Default max file size:</b> 30MB (configurable via platform settings)</li>
<li>Use <code>GET /knowledgeBase/limits</code> to check current limits</li>
</ul>
<b>Supported File Types:</b><br>
Documents (PDF, DOCX, TXT), Images (PNG, JPG), Videos (MP4), and more.<br><br>
<b>File Metadata:</b><br>
Use <code>files_metadata</code> to provide additional info like file paths and last modified timestamps.<br><br>
<b>Versioning:</b><br>
Set <code>isVersioned: true</code> to enable version tracking for uploaded files.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadRecordsToKB" method="post" path="/knowledgeBase/{kbId}/upload" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.upload.to_knowledge_base(kb_id="<id>", files=[
        {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    ], files_metadata="[{\"file_path\":\"/docs/report.pdf\",\"last_modified\":\"2024-01-15T10:30:00Z\"}]", is_versioned=True, record_type="FILE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `kb_id`                                                                     | *str*                                                                       | :heavy_check_mark:                                                          | Knowledge base ID                                                           |                                                                             |
| `files`                                                                     | List[[models.UploadRecordsToKBFile](../../models/uploadrecordstokbfile.md)] | :heavy_check_mark:                                                          | Files to upload (max 1000)                                                  |                                                                             |
| `files_metadata`                                                            | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | JSON array with file_path and last_modified for each file                   | [{"file_path":"/docs/report.pdf","last_modified":"2024-01-15T10:30:00Z"}]   |
| `is_versioned`                                                              | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Enable version tracking                                                     |                                                                             |
| `record_type`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Type of records to create                                                   |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.UploadResult](../../models/uploadresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## records_to_folder

Upload files directly to a specific folder within a knowledge base.<br><br>
<b>Same as KB upload</b> but files are placed in the specified folder instead of KB root.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadRecordsToFolder" method="post" path="/knowledgeBase/{kbId}/folder/{folderId}/upload" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.upload.records_to_folder(kb_id="<id>", folder_id="<id>", files=[
        {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    ], is_versioned=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `kb_id`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `folder_id`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | Target folder ID                                                                    |
| `files`                                                                             | List[[models.UploadRecordsToFolderFile](../../models/uploadrecordstofolderfile.md)] | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `files_metadata`                                                                    | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | JSON array with file metadata                                                       |
| `is_versioned`                                                                      | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UploadResult](../../models/uploadresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |