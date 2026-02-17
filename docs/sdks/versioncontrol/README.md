# VersionControl

## Overview

### Available Operations

* [upload_next_version](#upload_next_version) - Upload next version
* [rollback](#rollback) - Rollback to previous version
* [check_document_modified](#check_document_modified) - Check if document is modified

## upload_next_version

Upload a new version of a versioned document, maintaining full version history.<br><br>
<b>Overview:</b><br>
This endpoint creates a new version entry in the document's version history. The previous version remains accessible and the document can be rolled back if needed.<br><br>
<b>Version Control Flow:</b><br>
<ol>
<li>Upload new file content</li>
<li>System compares with previous version</li>
<li>If different, creates new version entry</li>
<li>Updates version history with metadata</li>
<li>Current document points to new version</li>
</ol>
<b>Version Entry Contains:</b><br>
<ul>
<li>Version number (auto-incremented)</li>
<li>Storage URL for this version</li>
<li>Size and extension</li>
<li>Optional note describing changes</li>
<li>User who created version</li>
<li>Timestamp</li>
</ul>
<b>Requirements:</b><br>
<ul>
<li>Document must have <code>isVersionedFile: true</code></li>
<li>File extension must match original document</li>
<li>Content must differ from previous version</li>
</ul>
<b>File Constraints:</b><br>
<ul>
<li>Maximum size: 100MB</li>
<li>Same extension as original required</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadNextVersion" method="post" path="/document/{documentId}/uploadNextVersion" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.version_control.upload_next_version(document_id="507f1f77bcf86cd799439011", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, current_version_note="Draft version with initial content", next_version_note="Final version with all revisions incorporated")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `document_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Document ID (24-character MongoDB ObjectId)                           | 507f1f77bcf86cd799439011                                              |
| `file`                                                                | [models.UploadNextVersionFile](../../models/uploadnextversionfile.md) | :heavy_check_mark:                                                    | New version file (max 100MB)                                          |                                                                       |
| `current_version_note`                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Note describing the current version being replaced                    | Draft version with initial content                                    |
| `next_version_note`                                                   | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Note describing the new version being uploaded                        | Final version with all revisions incorporated                         |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.UploadNextVersionResponse](../../models/uploadnextversionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## rollback

Restore a versioned document to a previous version. Creates a new version entry with the rolled-back content.<br><br>
<b>Overview:</b><br>
This endpoint allows reverting a document to any previous version while maintaining the complete version history. The rollback itself creates a new version entry.<br><br>
<b>Rollback Flow:</b><br>
<ol>
<li>Specify target version number to rollback to</li>
<li>System retrieves content from that version</li>
<li>Creates new version entry with restored content</li>
<li>Adds rollback note to version history</li>
<li>Document now shows restored content</li>
</ol>
<b>Version History Preserved:</b><br>
Rollback does NOT delete intermediate versions. Full history remains intact for audit purposes.<br><br>
<b>Requirements:</b><br>
<ul>
<li>Document must be versioned</li>
<li>Target version must exist (less than current version count)</li>
<li>Note explaining rollback reason is required</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Reverting accidental changes</li>
<li>Restoring to known-good state</li>
<li>Undoing problematic updates</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="rollBackToPreviousVersion" method="post" path="/document/{documentId}/rollBack" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.version_control.rollback(document_id="507f1f77bcf86cd799439011", version="2", note="Reverting to version 2 due to incorrect data in version 3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID (24-character MongoDB ObjectId)                         | 507f1f77bcf86cd799439011                                            |
| `version`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Version number to rollback to (0-indexed)                           | 2                                                                   |
| `note`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Reason for rollback (required for audit trail)                      | Reverting to version 2 due to incorrect data in version 3           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RollBackToPreviousVersionResponse](../../models/rollbacktopreviousversionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## check_document_modified

Check if the current document content differs from the last saved version. Useful for detecting unsaved changes.<br><br>
<b>Overview:</b><br>
Compares the current document buffer with the most recent version in history to detect modifications. Returns true if content has changed since last version.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Prompting user to save before closing</li>
<li>Auto-save decision making</li>
<li>Version creation validation</li>
<li>Change detection in workflows</li>
</ul>
<b>Comparison Method:</b><br>
Performs binary comparison of file buffers. Identical content returns false even if edited and reverted.<br><br>
<b>Requirements:</b><br>
Document must be versioned to have comparison baseline.


### Example Usage

<!-- UsageSnippet language="python" operationID="checkDocumentModified" method="get" path="/document/{documentId}/isModified" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.version_control.check_document_modified(document_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Document ID (24-character MongoDB ObjectId)                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CheckDocumentModifiedResponse](../../models/checkdocumentmodifiedresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |