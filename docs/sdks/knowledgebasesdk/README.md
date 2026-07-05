# KnowledgeBase

## Overview

Knowledge base management operations

### Available Operations

* [create_knowledge_base](#create_knowledge_base) - Create a new knowledge base
* [list_knowledge_bases](#list_knowledge_bases) - List all knowledge bases
* [get_knowledge_base](#get_knowledge_base) - Get knowledge base by ID
* [update_knowledge_base](#update_knowledge_base) - Update knowledge base
* [delete_knowledge_base](#delete_knowledge_base) - Delete knowledge base
* [get_record_by_id](#get_record_by_id) - Get record by ID
* [update_record](#update_record) - Update record
* [delete_record](#delete_record) - Delete record
* [stream_record_buffer](#stream_record_buffer) - Stream record content
* [create_folder](#create_folder) - Create folder
* [update_folder](#update_folder) - Update folder
* [delete_folder](#delete_folder) - Delete folder
* [upload_records](#upload_records) - Upload files to knowledge base or folder
* [get_upload_limits](#get_upload_limits) - Get knowledge base upload limits
* [reindex_record](#reindex_record) - Reindex single record
* [reindex_record_group](#reindex_record_group) - Reindex record group
* [move_record](#move_record) - Move record to another location
* [~~get_knowledge_hub_root_nodes~~](#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes :warning: **Deprecated**
* [~~get_knowledge_hub_child_nodes~~](#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes :warning: **Deprecated**

## create_knowledge_base

Create a new knowledge base for organizing and managing documents within your organization.

**Overview:**

A knowledge base is a container for organizing related documents, files, and content. It provides a central location for teams to collaborate on shared information.

**Features:**

- Hierarchical folder structure support
- Role-based access control (OWNER, WRITER, READER)
- Full-text search across all records
- Integration with external connectors (Google Drive, OneDrive, etc.)
- Automatic content indexing for AI-powered search

**Naming Rules:**

- Name must be 1-255 characters
- Special characters and HTML tags are sanitized
- Names don't need to be unique within organization

**Creator Permissions:**

The user creating the KB automatically becomes the OWNER with full administrative rights.


### Example Usage

<!-- UsageSnippet language="python" operationID="createKnowledgeBase" method="post" path="/knowledgeBase" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.create_knowledge_base(kb_name="Product Documentation")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_name`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Name of the knowledge base                                          | Product Documentation                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.KnowledgeBaseCreateResponse](../../models/knowledgebasecreateresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_knowledge_bases

Retrieve a paginated list of all knowledge bases accessible to the authenticated user.

**Overview:**

Returns knowledge bases where the user has at least READER permission. Results include the user's role for each KB.

**Filtering:**

- **search:** Full-text search on KB names (max 1000 chars)
- **permissions:** Filter by user's role (comma-separated: OWNER, WRITER, READER)

**Sorting Options:**

- `name` — Alphabetical by KB name
- `createdAtTimestamp` — By creation date
- `updatedAtTimestamp` — By last modification
- `userRole` — By permission level

**Performance:**

Uses efficient pagination with limit/offset. For large result sets, use smaller page sizes.

**Query parameters:**

Only `page`, `limit`, `search`, `permissions`, `sortBy`, and `sortOrder` are allowed; unknown query keys are rejected.


### Example Usage

<!-- UsageSnippet language="python" operationID="listKnowledgeBases" method="get" path="/knowledgeBase" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.list_knowledge_bases(page=1, limit=20, permissions="OWNER,ORGANIZER,WRITER", sort_by="name", sort_order="asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                            | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Page number (1-indexed). Omitted values default to 1.                                                                                                             |                                                                                                                                                                   |
| `limit`                                                                                                                                                           | *Optional[int]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Results per page (max 100). Omitted values default to 20.                                                                                                         |                                                                                                                                                                   |
| `search`                                                                                                                                                          | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Search KB names (max 1000 chars). Rejected if it contains HTML/script tags,<br/>event handlers, `javascript:`, or format specifiers (validated in Zod + controller).<br/> |                                                                                                                                                                   |
| `permissions`                                                                                                                                                     | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Comma-separated permission roles to filter by. Each token must be one of:<br/>OWNER, WRITER, READER.<br/>                                                         | OWNER,WRITER                                                                                                                                                      |
| `sort_by`                                                                                                                                                         | [Optional[models.ListKnowledgeBasesSortBy]](../../models/listknowledgebasessortby.md)                                                                             | :heavy_minus_sign:                                                                                                                                                | Field to sort by.                                                                                                                                                 |                                                                                                                                                                   |
| `sort_order`                                                                                                                                                      | [Optional[models.ListKnowledgeBasesSortOrder]](../../models/listknowledgebasessortorder.md)                                                                       | :heavy_minus_sign:                                                                                                                                                | Sort direction.                                                                                                                                                   |                                                                                                                                                                   |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.GetAllKnowledgeBaseResponseSchema](../../models/getallknowledgebaseresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_knowledge_base

Retrieve detailed information about a specific knowledge base.

**Overview:**

Returns complete KB metadata including name, timestamps, root-level folders, and the requesting user's role.

**Access Control:**

User must have at least READER permission to view KB details.


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeBase" method="get" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.get_knowledge_base(kb_id="kb_550e8400-e29b-41d4-a716")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID (non-empty string)                                | 8a095180-2989-4018-b448-70eb75fba1c7                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetKnowledgeBaseByID](../../models/getknowledgebasebyid.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 403, 404               | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_knowledge_base

Update a knowledge base's name.

**Required permission:**

User must have one of `OWNER` or `WRITER` on the knowledge base.

**Validation:**

- `kbId` path parameter must be a valid UUID (`updateKBSchema`)
- When provided, `kbName` must be 1–255 characters
- XSS and format-specifier checks are applied to `kbName` in the gateway controller


### Example Usage

<!-- UsageSnippet language="python" operationID="updateKnowledgeBase" method="put" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_knowledge_base(kb_id="<id>", kb_name="Updated Documentation Hub")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID (UUID)                                            | 8a095180-2989-4018-b448-70eb75fba1c7                                |
| `kb_name`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New name for the knowledge base                                     | Updated Documentation Hub                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateKnowledgeBaseByID](../../models/updateknowledgebasebyid.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_knowledge_base

Permanently delete a knowledge base and all its contents.

**Required permission:**

User must have `OWNER` role on the knowledge base.

**What gets deleted:**

- All folders within the KB
- All records and their indexed content
- All permission grants
- Associated storage files

**Warning:** This action is irreversible. Consider exporting data before deletion.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteKnowledgeBase" method="delete" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.delete_knowledge_base(kb_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID (non-empty string)                                | 8a095180-2989-4018-b448-70eb75fba1c7                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteKnowledgeBaseByID](../../models/deleteknowledgebasebyid.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 403, 404               | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_record_by_id

Retrieve detailed information about a specific record.

**Overview:**

Returns complete record metadata including name, type, indexing status, storage information, and version history.

**File conversion:**

Use the optional `convertTo` parameter to request file format conversion (e.g., PDF to text). Supported conversions include PPT to PDF and PPTX to PDF.


### Example Usage

<!-- UsageSnippet language="python" operationID="getRecordById" method="get" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.get_record_by_id(record_id="<id>", convert_to="txt")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                           | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | Record ID                                                                                                             |                                                                                                                       |
| `convert_to`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | Optional format to convert the file to (e.g., PDF to text). Supported conversions include PPT to PDF and PPTX to PDF. | txt                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.GetRecordByIDResponseSchema](../../models/getrecordbyidresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_record

Update a record's name and/or file content.

**Overview:**

Allows updating the display name and optionally replacing the file content. Triggers re-indexing when content changes.

**Required permission:**

WRITER or higher

**Updating file content:**

Include a new file in the request to replace the existing content. The file extension must match the original.

**Side effects:**

- Updates `updatedAtTimestamp`
- Increments version if file content changed
- Triggers re-indexing for content changes


### Example Usage

<!-- UsageSnippet language="python" operationID="updateRecord" method="put" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_record(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `record_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Record ID                                                             |
| `record_name`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | New name for the record                                               |
| `file`                                                                | [Optional[models.UpdateRecordFile]](../../models/updaterecordfile.md) | :heavy_minus_sign:                                                    | Replacement file content                                              |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UpdateRecordResponse](../../models/updaterecordresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_record

Permanently delete a record from the knowledge base.

**Required permission:**

WRITER or higher

**What gets deleted:**

- Record metadata
- Associated storage file
- Indexed content and embeddings

**Warning:** This action is irreversible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteRecord" method="delete" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.delete_record(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteRecordResponseSchema](../../models/deleterecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream_record_buffer

Stream the binary content of a record's file.

**Overview:**

Returns the raw file content with appropriate `Content-Type` and `Content-Disposition` headers for download or inline viewing.

**Use cases:**

- File downloads
- Inline document preview
- Content extraction pipelines

**Format conversion:**

Use the `convertTo` parameter to convert between formats (e.g. DOCX to PDF).


### Example Usage

<!-- UsageSnippet language="python" operationID="streamRecordBuffer" method="get" path="/knowledgeBase/stream/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.stream_record_buffer(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID                                                           |
| `convert_to`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Target format for conversion                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 400, 401                         | application/json                 |
| errors.ErrorResponse             | 403                              | application/json                 |
| errors.StreamRecordErrorResponse | 403                              | application/json                 |
| errors.StreamRecordErrorResponse | 404, 409                         | application/json                 |
| errors.StreamRecordErrorResponse | 500                              | application/json                 |
| errors.PipeshubDefaultError      | 4XX, 5XX                         | \*/\*                            |

## create_folder

Create a folder in a knowledge base. Omit `folderId` to create at the KB root;
pass `folderId` as a query parameter to create a nested subfolder inside an
existing parent folder.

**Required permission:** WRITER or higher

**Folder features:**

- Organize records hierarchically
- Support nested subfolders (unlimited depth)
- Inherit parent KB permissions

**Naming rules:**

- 1–255 characters
- XSS protection applied
- Spaces and special characters allowed
- Duplicate names rejected within the same parent (`409`)

**Response:** Returns `id` and `name` for the created folder.


### Example Usage

<!-- UsageSnippet language="python" operationID="createFolder" method="post" path="/knowledgeBase/{kbId}/folder" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.create_folder(kb_id="<id>", folder_name="Project Documents")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   |                                                                     |
| `folder_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name of the folder                                                  | Project Documents                                                   |
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Parent folder ID. Omit to create at the knowledge base root.        |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FolderCreateResponseSchema](../../models/foldercreateresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_folder

Rename a folder.

**Required permission:** WRITER or higher


### Example Usage

<!-- UsageSnippet language="python" operationID="updateFolder" method="put" path="/knowledgeBase/{kbId}/folder/{folderId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_folder(kb_id="<id>", folder_id="<id>", folder_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FolderUpdateResponseSchema](../../models/folderupdateresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_folder

Delete a folder and all its contents.

**Required permission:** WRITER or higher

**Cascade delete:**

All subfolders and records within will be permanently deleted.

**Warning:** This action is irreversible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteFolder" method="delete" path="/knowledgeBase/{kbId}/folder/{folderId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.delete_folder(kb_id="<id>", folder_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FolderDeleteResponseSchema](../../models/folderdeleteresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upload_records

Upload one or more files to a knowledge base root or to a specific folder.

**Overview**

Batch upload multiple files in a single request. Each file becomes a new record with automatic content indexing.
Omit the `folderId` query parameter to upload to the KB root; include it to upload into that folder.

**Upload Limits**

- **Max files per request:** 1000
- **Default max file size:** 30MB (configurable via platform settings)
- Use `GET /knowledgeBase/limits` to check current limits

**Supported File Types**

Documents (PDF, DOCX, DOC, XLS, XLSX, PPT, PPTX, TXT, CSV, MD), Images (PNG, JPG, JPEG, SVG, WebP), Web (HTML, HTM), and Google Workspace formats.

**File Metadata**

Use `files_metadata` to provide additional info like file paths and last modified timestamps.

**Versioning**

Set `isVersioned: true` to enable version tracking for uploaded files.

**Streaming response**

This endpoint responds with `Content-Type: text/event-stream`.
The upload and its per-file progress are a single request: the body streams
a `file:succeeded` or `file:failed` event per file
(including files rejected up front for size/type), followed by a final
`done` summary, then closes. See the
`UploadStreamSSEEvent` schema for the event/payload contract.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadRecords" method="post" path="/knowledgeBase/{kbId}/upload" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.upload_records(kb_id="<id>", files=[], files_metadata="[{\"file_path\":\"/docs/report.pdf\",\"last_modified\":\"2024-01-15T10:30:00Z\"}]", is_versioned=True, record_type="FILE")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `kb_id`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | Knowledge base ID                                                         |                                                                           |
| `files`                                                                   | List[[models.UploadRecordsFile](../../models/uploadrecordsfile.md)]       | :heavy_check_mark:                                                        | Files to upload (max 1000)                                                |                                                                           |
| `folder_id`                                                               | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Target folder ID. Omit to upload to the KB root.                          |                                                                           |
| `files_metadata`                                                          | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | JSON array with file_path and last_modified for each file                 | [{"file_path":"/docs/report.pdf","last_modified":"2024-01-15T10:30:00Z"}] |
| `is_versioned`                                                            | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Enable version tracking                                                   |                                                                           |
| `record_type`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Type of records to create                                                 |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[Union[eventstreaming.EventStream[models.UploadStreamSSEEvent], eventstreaming.EventStreamAsync[models.UploadStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 413, 429 | application/json             |
| errors.PipeshubDefaultError  | 4XX, 5XX                     | \*/\*                        |

## get_upload_limits

Retrieve current upload constraints for the organization.

**Use case:** Call this before uploads to validate file sizes on the client
side and display appropriate limits to users.


### Example Usage

<!-- UsageSnippet language="python" operationID="getUploadLimits" method="get" path="/knowledgeBase/limits" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.get_upload_limits()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadLimitsResponseSchema](../../models/uploadlimitsresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_record

Trigger reindexing for a specific record.

**Overview:**

Reprocesses the record's content to update search indexes and AI embeddings. Useful after content changes or to fix indexing failures.

**Depth parameter:**

Controls processing depth for complex documents (`-1` for full depth, `0`–`100` for limited).

**Status filters:**

Optional `statusFilters` array limits reindex to records in matching indexing states
(e.g. `FAILED`, `AUTO_INDEX_OFF`).


### Example Usage

<!-- UsageSnippet language="python" operationID="reindexRecord" method="post" path="/knowledgeBase/reindex/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.reindex_record(record_id="<id>", depth=0, force=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `record_id`                                                                                                                                      | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | N/A                                                                                                                                              |
| `depth`                                                                                                                                          | *Optional[int]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Child traversal depth (`0` = record only; higher values include<br/>descendants; `100` is used by clients for folder-like reindex).<br/>         |
| `force`                                                                                                                                          | *Optional[bool]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                               | Force reindex even when the connector considers the record unchanged.                                                                            |
| `status_filters`                                                                                                                                 | List[[models.IndexingStatusFilter](../../models/indexingstatusfilter.md)]                                                                        | :heavy_minus_sign:                                                                                                                               | When set, only records whose indexing status matches one of these<br/>values are reindexed (applies to the record and its descendants per `depth`).<br/> |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Response

**[models.ReIndexRecordResponseSchema](../../models/reindexrecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_record_group

Trigger reindexing for all records in a folder or knowledge base.

**Overview:**

Batch reindex operation for entire containers. The `recordGroupId` can be a folder ID or KB ID.

**Status filters:**

Optional `statusFilters` limit which child records are queued (e.g. failed-only or manual-indexing).


### Example Usage

<!-- UsageSnippet language="python" operationID="reindexRecordGroup" method="post" path="/knowledgeBase/reindex/record-group/{recordGroupId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.reindex_record_group(record_group_id="<id>", depth=0, force=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `record_group_id`                                                         | *str*                                                                     | :heavy_check_mark:                                                        | Folder ID or KB ID                                                        |
| `depth`                                                                   | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Depth of records under the record group to include.                       |
| `force`                                                                   | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Force reindex for all matched records in the group.                       |
| `status_filters`                                                          | List[[models.IndexingStatusFilter](../../models/indexingstatusfilter.md)] | :heavy_minus_sign:                                                        | When set, only records matching these indexing statuses are reindexed.<br/> |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ReIndexRecordGroupResponseSchema](../../models/reindexrecordgroupresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## move_record

Move a file or folder record to a different location within the same knowledge base.

Set `newParentId` to a folder ID to move the record into that folder, or `null` to move it to the knowledge base root.

**Required Permission:** OWNER or WRITER


### Example Usage: moveToFolder

<!-- UsageSnippet language="python" operationID="moveRecord" method="put" path="/knowledgeBase/{kbId}/record/{recordId}/move" example="moveToFolder" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.move_record(kb_id="702f8ff0-0a01-4354-b592-eea268f40f25", record_id="<id>", new_parent_id="folder-abc123")

    # Handle response
    print(res)

```
### Example Usage: moveToRoot

<!-- UsageSnippet language="python" operationID="moveRecord" method="put" path="/knowledgeBase/{kbId}/record/{recordId}/move" example="moveToRoot" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.move_record(kb_id="8bdbd4fc-ec2e-4e15-8a88-ae59a5b4bad2", record_id="<id>", new_parent_id=None)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `kb_id`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | Knowledge base UUID                                                     |
| `record_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | Record identifier (file or folder)                                      |
| `new_parent_id`                                                         | *Nullable[str]*                                                         | :heavy_check_mark:                                                      | Target folder ID, or null to move the record to the knowledge base root |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.KnowledgeBaseMoveRecordResponse](../../models/knowledgebasemoverecordresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_knowledge_hub_root_nodes~~

Returns root-level nodes (connector apps and Collection apps) or, when
filters or search are applied, a flat list of matching nodes across the
entire knowledge hub tree.

**Overview**

The Knowledge Hub provides a unified view across all knowledge sources:
- **Collection** — locally uploaded knowledge bases (`origin: COLLECTION`)
- **Connector app** — external connector instances such as Google Drive,
  Slack, Confluence, Jira (`origin: CONNECTOR`)

Use this endpoint to build file-browser UIs and sidebar navigation trees.

**Browsing vs. searching**

When no filters or search query are provided, only top-level app nodes
are returned. Adding `nodeTypes`, `q`, or other filter params triggers a
search across the full tree, returning matching nodes regardless of depth.

For children of a specific node, use
`GET /knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}`.

**Pagination and sorting**

Results are always paginated. Default sort is `updatedAt` descending.
The `pagination` object in the response contains `hasNext` / `hasPrev`
flags suitable for infinite-scroll or page-based navigation.

**Expanding the response**

Use the `include` parameter to request additional sections:
- `availableFilters` — adds `filters.available` with all filter options
- `counts` — adds a `counts` summary broken down by node type
- `breadcrumbs` — adds the breadcrumb trail (empty at root level)
- `permissions` — adds the caller's permission flags

**Access control**

Requires a valid bearer token. For OAuth tokens the `kb:read` scope
must be present; regular JWT bearer tokens pass through without scope
enforcement.


> :warning: **DEPRECATED**: Use the Knowledge Base API instead. This grouping will be removed in a future release.

### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubRootNodes" method="get" path="/knowledgeBase/knowledge-hub/nodes" example="root_apps" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.get_knowledge_hub_root_nodes(only_containers=False, page=1, limit=50, sort_by="updatedAt", sort_order="desc", q="quarterly report", node_types="app,recordGroup", record_types="FILE,CONFLUENCE_PAGE", origins="CONNECTOR", connector_ids="f3a4b5b6-5b6c-4e85-9097-3202cfe696fc", indexing_status="COMPLETED,FAILED", created_at="gte:1700000000000,lte:1710000000000", updated_at="gte:1700000000000,lte:1710000000000", size="gte:0,lte:10485760", include="availableFilters,counts")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `only_containers`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | When `true`, only nodes that have children are returned (useful for<br/>building sidebar / tree navigation). Leaf nodes are excluded.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Page number (1-indexed). Combined with `limit` to paginate results.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Maximum number of items to return per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sort_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.GetKnowledgeHubRootNodesSortBy]](../../models/getknowledgehubrootnodessortby.md)                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Field to sort results by. Omitted → default `updatedAt`.<br/>Unknown value → silently falls back to `name`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sort_order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.GetKnowledgeHubRootNodesSortOrder]](../../models/getknowledgehubrootnodessortorder.md)                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Sort direction. Omitted → default `desc`.<br/>Unknown value → silently falls back to `asc`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `q`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Full-text search query. Must be between 2 and 500 characters<br/>(inclusive). When provided, the endpoint searches across the entire<br/>node tree regardless of the current browse level.<br/>                                                                                                                                                                                                                                                                                                                                           | quarterly report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `node_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of node types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `folder`, `app`, `recordGroup`, `record`<br/>                                                                                                                                                                                                                                                                                                                                                           | app,recordGroup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `record_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of record types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `FILE`, `DRIVE`, `WEBPAGE`, `DATABASE`, `DATASOURCE`,<br/>`MESSAGE`, `MAIL`, `GROUP_MAIL`, `TICKET`, `COMMENT`,<br/>`INLINE_COMMENT`, `CONFLUENCE_PAGE`, `CONFLUENCE_BLOGPOST`,<br/>`SHAREPOINT_PAGE`, `SHAREPOINT_LIST`, `SHAREPOINT_LIST_ITEM`,<br/>`SHAREPOINT_DOCUMENT_LIBRARY`, `LINK`, `PROJECT`, `PULL_REQUEST`,<br/>`MEETING`, `PRODUCT`, `DEAL`, `CASE`, `TASK`, `ARTIFACT`,<br/>`CODE_FILE`, `SQL_TABLE`, `SQL_VIEW`, `OTHERS`<br/> | FILE,CONFLUENCE_PAGE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `origins`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of origin types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `COLLECTION`, `CONNECTOR`<br/>                                                                                                                                                                                                                                                                                                                                                                        | CONNECTOR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `connector_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of connector instance IDs (UUIDs) to filter by.<br/>Maximum 100 items. No enum validation — any string is accepted, but<br/>non-existent IDs simply yield zero results.<br/>                                                                                                                                                                                                                                                                                                                                         | f3a4b5b6-5b6c-4e85-9097-3202cfe696fc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `indexing_status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of indexing statuses to include. Invalid values<br/>are silently ignored. Maximum 100 items.<br/><br/>Valid values: `NOT_STARTED`, `PAUSED`, `IN_PROGRESS`, `COMPLETED`,<br/>`FAILED`, `FILE_TYPE_NOT_SUPPORTED`, `AUTO_INDEX_OFF`, `EMPTY`,<br/>`ENABLE_MULTIMODAL_MODELS`, `QUEUED`<br/>                                                                                                                                                                                                                           | COMPLETED,FAILED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Created-date range filter. Format: `gte:<epochMs>,lte:<epochMs>`.<br/>Both bounds are optional (you may send just `gte:...` or just<br/>`lte:...`). Timestamps must be in the range 0 to 9999999999999 and<br/>`gte` must be less than or equal to `lte` when both are present.<br/>                                                                                                                                                                                                                                                      | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Updated-date range filter. Same format and constraints as `createdAt`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                               | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | File-size range filter in bytes. Format: `gte:<bytes>,lte:<bytes>`.<br/>Both bounds are optional. Values must be non-negative and at most<br/>1099511627776 (1 TB). `gte` must be less than or equal to `lte`<br/>when both are present.<br/>                                                                                                                                                                                                                                                                                             | gte:0,lte:10485760                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `include`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of additional response sections to include.<br/>Invalid values are silently ignored. Maximum 100 items.<br/><br/>Valid values: `breadcrumbs`, `counts`, `availableFilters`, `permissions`<br/>                                                                                                                                                                                                                                                                                                                       | availableFilters,counts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.KnowledgeHubNodesResponse](../../models/knowledgehubnodesresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.GetKnowledgeHubRootNodesBadRequestError     | 400                                                | application/json                                   |
| errors.GetKnowledgeHubRootNodesUnauthorizedError   | 401                                                | application/json                                   |
| errors.GetKnowledgeHubRootNodesForbiddenError      | 403                                                | application/json                                   |
| errors.GetKnowledgeHubRootNodesInternalServerError | 500                                                | application/json                                   |
| errors.PipeshubDefaultError                        | 4XX, 5XX                                           | \*/\*                                              |

## ~~get_knowledge_hub_child_nodes~~

Returns the children of a specific node in the knowledge hub tree.
Use this endpoint to drill down into Collections, connector app
hierarchies, folders, and record groups.

**Navigation hierarchy**

The typical drill-down path is:
1. Root apps (`GET /knowledgeBase/knowledge-hub/nodes`)
2. Record groups / folders within an app (`parentType=app`)
3. Records within a record group (`parentType=recordGroup`)
4. Sub-records or attachments within a record (`parentType=record`)

**Parent identification**

- `parentType` must be one of: `app`, `recordGroup`, `folder`, `record`
- `parentId` is either a standard UUID or the Collection app sentinel
  `knowledgeBase_<orgId>` (e.g. `knowledgeBase_org123`)

**Filtering and searching**

All query-param filters from the root endpoint are available here and
operate within the scope of the parent node's subtree. When `q` is
provided, the search spans all descendants of the parent node.

**Response extras**

When `include=breadcrumbs` is set, the response contains a
`breadcrumbs` array tracing the path from the root to the current
node. The `currentNode` and `parentNode` objects are always populated
for non-root requests.

**Access control**

Requires a valid bearer token. For OAuth tokens the `kb:read` scope
must be present; regular JWT bearer tokens pass through without scope
enforcement.


> :warning: **DEPRECATED**: Use the Knowledge Base API instead. This grouping will be removed in a future release.

### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubChildNodes" method="get" path="/knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}" example="collection_record_groups" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.get_knowledge_hub_child_nodes(parent_type="app", parent_id="<id>", only_containers=False, page=1, limit=50, sort_by="updatedAt", sort_order="desc", q="quarterly report", node_types="recordGroup", record_types="FILE,CONFLUENCE_PAGE", origins="CONNECTOR", connector_ids="f3a4b5b6-5b6c-4e85-9097-3202cfe696fc", indexing_status="COMPLETED,FAILED", created_at="gte:1700000000000,lte:1710000000000", updated_at="gte:1700000000000,lte:1710000000000", size="gte:0,lte:10485760", include="breadcrumbs,availableFilters")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `parent_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [models.ParentType](../../models/parenttype.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type of the parent node whose children to retrieve.<br/><br/>Must be one of: `app`, `recordGroup`, `folder`, `record`.<br/>Any other value returns a 400 error.<br/>                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `parent_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Identifier of the parent node. Accepts two formats:<br/>- A standard UUID (e.g. `f3a4b5b6-5b6c-4e85-9097-3202cfe696fc`)<br/>- The Collection app sentinel `knowledgeBase_<orgId>`<br/>  (e.g. `knowledgeBase_org123`)<br/><br/>Any value that does not match either format returns a 400 error.<br/>                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `only_containers`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | When `true`, only nodes that have children are returned (useful for<br/>building sidebar / tree navigation). Leaf nodes are excluded.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Page number (1-indexed). Combined with `limit` to paginate results.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Maximum number of items to return per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sort_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.GetKnowledgeHubChildNodesSortBy]](../../models/getknowledgehubchildnodessortby.md)                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Field to sort results by. Omitted → default `updatedAt`.<br/>Unknown value → silently falls back to `name`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sort_order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.GetKnowledgeHubChildNodesSortOrder]](../../models/getknowledgehubchildnodessortorder.md)                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Sort direction. Omitted → default `desc`.<br/>Unknown value → silently falls back to `asc`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `q`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Full-text search query. Must be between 2 and 500 characters<br/>(inclusive). When provided, the endpoint searches across all<br/>descendants of the parent node.<br/>                                                                                                                                                                                                                                                                                                                                                                    | quarterly report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `node_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of node types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `folder`, `app`, `recordGroup`, `record`<br/>                                                                                                                                                                                                                                                                                                                                                           | recordGroup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `record_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of record types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `FILE`, `DRIVE`, `WEBPAGE`, `DATABASE`, `DATASOURCE`,<br/>`MESSAGE`, `MAIL`, `GROUP_MAIL`, `TICKET`, `COMMENT`,<br/>`INLINE_COMMENT`, `CONFLUENCE_PAGE`, `CONFLUENCE_BLOGPOST`,<br/>`SHAREPOINT_PAGE`, `SHAREPOINT_LIST`, `SHAREPOINT_LIST_ITEM`,<br/>`SHAREPOINT_DOCUMENT_LIBRARY`, `LINK`, `PROJECT`, `PULL_REQUEST`,<br/>`MEETING`, `PRODUCT`, `DEAL`, `CASE`, `TASK`, `ARTIFACT`,<br/>`CODE_FILE`, `SQL_TABLE`, `SQL_VIEW`, `OTHERS`<br/> | FILE,CONFLUENCE_PAGE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `origins`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of origin types to include. Invalid values are<br/>silently ignored. Maximum 100 items.<br/><br/>Valid values: `COLLECTION`, `CONNECTOR`<br/>                                                                                                                                                                                                                                                                                                                                                                        | CONNECTOR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `connector_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of connector instance IDs (UUIDs) to filter by.<br/>Maximum 100 items. No enum validation — any string is accepted, but<br/>non-existent IDs simply yield zero results.<br/>                                                                                                                                                                                                                                                                                                                                         | f3a4b5b6-5b6c-4e85-9097-3202cfe696fc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `indexing_status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of indexing statuses to include. Invalid values<br/>are silently ignored. Maximum 100 items.<br/><br/>Valid values: `NOT_STARTED`, `PAUSED`, `IN_PROGRESS`, `COMPLETED`,<br/>`FAILED`, `FILE_TYPE_NOT_SUPPORTED`, `AUTO_INDEX_OFF`, `EMPTY`,<br/>`ENABLE_MULTIMODAL_MODELS`, `QUEUED`<br/>                                                                                                                                                                                                                           | COMPLETED,FAILED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Created-date range filter. Format: `gte:<epochMs>,lte:<epochMs>`.<br/>Both bounds are optional (you may send just `gte:...` or just<br/>`lte:...`). Timestamps must be in the range 0 to 9999999999999 and<br/>`gte` must be less than or equal to `lte` when both are present.<br/>                                                                                                                                                                                                                                                      | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Updated-date range filter. Same format and constraints as `createdAt`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                               | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | File-size range filter in bytes. Format: `gte:<bytes>,lte:<bytes>`.<br/>Both bounds are optional. Values must be non-negative and at most<br/>1099511627776 (1 TB). `gte` must be less than or equal to `lte`<br/>when both are present.<br/>                                                                                                                                                                                                                                                                                             | gte:0,lte:10485760                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `include`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Comma-separated list of additional response sections to include.<br/>Invalid values are silently ignored. Maximum 100 items.<br/><br/>Valid values: `breadcrumbs`, `counts`, `availableFilters`, `permissions`<br/>                                                                                                                                                                                                                                                                                                                       | breadcrumbs,availableFilters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.KnowledgeHubNodesResponse](../../models/knowledgehubnodesresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.GetKnowledgeHubChildNodesBadRequestError     | 400                                                 | application/json                                    |
| errors.GetKnowledgeHubChildNodesUnauthorizedError   | 401                                                 | application/json                                    |
| errors.GetKnowledgeHubChildNodesForbiddenError      | 403                                                 | application/json                                    |
| errors.GetKnowledgeHubChildNodesNotFoundError       | 404                                                 | application/json                                    |
| errors.GetKnowledgeHubChildNodesInternalServerError | 500                                                 | application/json                                    |
| errors.PipeshubDefaultError                         | 4XX, 5XX                                            | \*/\*                                               |