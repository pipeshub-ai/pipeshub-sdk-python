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
* [update_record_multipart](#update_record_multipart) - Update record
* [update_record](#update_record) - Update record
* [update_record_form](#update_record_form) - Update record
* [delete_record](#delete_record) - Delete record
* [restore_record](#restore_record) - Restore a deleted record
* [restore_records](#restore_records) - Restore several deleted records
* [list_trash](#list_trash) - List a collection's recently deleted items
* [stream_record_buffer](#stream_record_buffer) - Stream record content
* [create_folder](#create_folder) - Create folder
* [create_subfolder](#create_subfolder) - Create subfolder
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

- Name must be 1-255 characters and hold at least one character that is not whitespace
- Whitespace around the name is removed before it is stored
- A name that contains an HTML tag, a `javascript:` URL or an inline event handler
  (`onclick=` and the like) is refused with `400`; nothing is stripped out of it
- Names don't need to be unique within organization

**Request body:**

Only `kbName` is read. Any other field is dropped before the handler runs, so a
knowledge base cannot be created hidden, or with another role or organization,
through this endpoint.

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

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           | Example                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `kb_name`                                                                                                                             | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | Name of the knowledge base. Leading and trailing whitespace is removed<br/>first, so a name made only of whitespace is refused as empty.<br/> | Product Documentation                                                                                                                 |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |                                                                                                                                       |

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

- **search:** Full-text search on KB names (max 1000 chars). A longer value is answered `500`, not `400`.
- **permissions:** Filter by user's role (comma-separated: OWNER, WRITER, READER)

**Sorting Options:**

- `name` — Alphabetical by KB name
- `createdAtTimestamp` — By creation date
- `updatedAtTimestamp` — By last modification
- `userRole` — By permission level

**Performance:**

Uses efficient pagination with limit/offset. For large result sets, use smaller page sizes.

**Query parameters:**

Only `page`, `limit`, `search`, `permissions`, `sortBy`, and `sortOrder` are allowed; any other
query key is rejected with `400` (`VALIDATION_ERROR`: "These fields aren't accepted here: <key>.").
A parameter sent more than once is rejected the same way. `page`, `limit`, `search`,
`permissions` and `sortBy` sent with an empty value are read as not sent; an empty
`sortOrder` is rejected.


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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Page number (1-indexed). Omitted or empty values default to 1. A page past the last<br/>one returns an empty list. The value is read with JavaScript `parseInt`, so text after<br/>leading digits is ignored (`1abc` is page 1); send a plain integer.<br/>                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Results per page (max 100). Omitted or empty values default to 20. Read with<br/>JavaScript `parseInt` like `page`.<br/>                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `search`                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Search KB names (max 1000 chars after trimming). Rejected with `400` if it contains<br/>HTML/script tags, event handlers or `javascript:` (`HTTP_BAD_REQUEST`), or a<br/>printf-style format specifier (`VALIDATION_ERROR`). The format-specifier check<br/>also catches ordinary text such as `50% discount` (`%`, a space, then a letter<br/>like `d`). A value longer than 1000 characters is answered `500`.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `permissions`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Comma-separated permission roles to filter by. Each token must be exactly one of<br/>OWNER, WRITER, READER: upper case, with no space around the commas. Empty tokens<br/>(`OWNER,,WRITER,`) are dropped, but a value with no role at all (`,`) is rejected.<br/>An empty value is read as not sent.<br/>                                                                                         | OWNER,WRITER                                                                                                                                                                                                                                                                                                                                                                                      |
| `sort_by`                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.ListKnowledgeBasesSortBy]](../../models/listknowledgebasessortby.md)                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Field to sort by. An empty value is read as the default.                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sort_order`                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[models.ListKnowledgeBasesSortOrder]](../../models/listknowledgebasessortorder.md)                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Sort direction.                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                   |

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

Returns complete KB metadata including name, timestamps, every folder (nested ones
included, without their parent), and the requesting user's role.

**Access Control:**

User must have at least READER permission to view KB details. A knowledge base the
caller holds no role on is answered `404` with the same message as an unknown id, so
its existence is not revealed.

**Request:** only the `kbId` path parameter is read; any query string or body is ignored.


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

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             | Example                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `kb_id`                                                                                                                 | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | Knowledge base ID (non-empty string). It is not checked to be a UUID: any other<br/>value is looked up and answered `404`.<br/> | 8a095180-2989-4018-b448-70eb75fba1c7                                                                                    |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |                                                                                                                         |

### Response

**[models.GetKnowledgeBaseByID](../../models/getknowledgebasebyid.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_knowledge_base

Update a knowledge base's name.

**Required permission:**

User must have one of `OWNER` or `WRITER` on the knowledge base.

**Validation:**

- `kbId` path parameter must be a valid UUID (`updateKBSchema`)
- `kbName` is trimmed first, then must be 1–255 characters
- A `kbName` holding an HTML tag, a `javascript:` URL or an inline event handler is
  refused with `400` before authentication; one holding a printf-style format
  specifier (`%s`, `%n`, `%x`, `%p`, with flags and width such as `%08x`) is refused
  with `400` by the gateway controller. A plain `%` (`50% off`) is accepted.
- `kbName` is the only field read. Other body fields and any query parameter are
  ignored, so a body without `kbName` (an empty object, no body, or only unknown
  fields) is refused by the connector service with `400` `No fields to update`.


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

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `kb_id`                                                                                                                         | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | Knowledge base ID (UUID)                                                                                                        | 8a095180-2989-4018-b448-70eb75fba1c7                                                                                            |
| `kb_name`                                                                                                                       | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | New name for the knowledge base. Whitespace around it is removed first, so<br/>a name made only of whitespace is refused as empty.<br/> | Updated Documentation Hub                                                                                                       |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.UpdateKnowledgeBaseByID](../../models/updateknowledgebasebyid.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
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

**Request:** only the `kbId` path parameter is read; any query string or body is ignored.


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
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_record_by_id

Retrieve detailed information about a specific record.

**Overview:**

Returns complete record metadata including name, type, indexing status, storage information, and version history.

**Query parameters:**

`convertTo` and `version` are checked by the request validator but not used by this
endpoint: the response is the same JSON metadata whatever they hold. They take effect
on `GET /knowledgeBase/stream/record/{recordId}`, which shares the validator. Any other
query parameter is ignored.

**Not found:**

A record that does not exist, one the caller has no access to and one that is in the
trash all answer `404` with the same message, so a record's existence is not revealed.


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

    res = pipeshub.knowledge_base.get_record_by_id(record_id="<id>", convert_to="txt", version="2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | Record ID                                                                                                                                                                                            |                                                                                                                                                                                                      |
| `convert_to`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | Accepted as any single string and not used by this endpoint (no conversion happens here). Sending it more than once is rejected with `400`.                                                          | txt                                                                                                                                                                                                  |
| `version`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | Registry version number of an artifact record: digits only. Checked and then not used by this endpoint; a value that is not all digits (empty, negative or decimal included) is rejected with `400`. | 2                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.GetRecordByIDResponseSchema](../../models/getrecordbyidresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_record_multipart

Update a record's name and/or file content.

**Overview:**

Allows updating the display name and optionally replacing the file content. Triggers re-indexing when content changes.

**Required permission:**

WRITER or higher on the record's knowledge base. A READER is answered `403`; a caller
with no role is answered `404`.

**Renaming:**

Send `recordName` as a multipart field or in a JSON body. There is no length limit.
A request with no body, an empty JSON object or an empty `recordName` changes nothing
and still answers `200`. In a JSON body the name is trimmed first (so a blank name is
read as empty and changes nothing); in a multipart form it is not, and a blank name
is refused with `400`. Fields other than `recordName` and `file` are ignored.

**Updating file content:**

Include a new file in a multipart request to replace the existing content. The file
extension must match the original: a file with another extension is answered `500`,
not `400`. When a file is sent, `recordName` is ignored and the record is named after
the file (without its extension).

**Side effects:**

- Updates `updatedAtTimestamp`
- A new file is stored as the next version of the record's storage document and the
  record is queued for indexing again. The record's own `version` and `sizeInBytes`
  are not updated by this call.

**Known gaps:**

- Renaming a record that is in the trash is not refused: the answer is `200` with the
  success message, but nothing changes, and `record` is the trashed record (`isDeleted: true`,
  with `deletedAtTimestamp`, `deleteBatchId` and `deleteSource`).
- `fileBuffer` is an internal field filled by the upload parser. A JSON body that
  supplies an object under that name (`buffer`, `originalname`, `mimetype`, `size`,
  `lastModified`) is treated as an uploaded file and stored as the new version.

**OAuth scopes:** `kb:write`, plus `kb:read`: replacing the file first reads the record and its knowledge base with the caller's token.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateRecord_multipart" method="put" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_record_multipart(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                                               | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Record ID                                                                                                                                 |
| `record_name`                                                                                                                             | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | New name for the record. Ignored when `file` is sent. Must not contain<br/>HTML, an inline event handler or a printf-style format specifier.<br/> |
| `file`                                                                                                                                    | [Optional[models.UpdateRecordMultipartFile]](../../models/updaterecordmultipartfile.md)                                                   | :heavy_minus_sign:                                                                                                                        | Replacement file content; at most one file, with the stored file's extension.                                                             |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.UpdateRecordResponseSchema](../../models/updaterecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_record

Update a record's name and/or file content.

**Overview:**

Allows updating the display name and optionally replacing the file content. Triggers re-indexing when content changes.

**Required permission:**

WRITER or higher on the record's knowledge base. A READER is answered `403`; a caller
with no role is answered `404`.

**Renaming:**

Send `recordName` as a multipart field or in a JSON body. There is no length limit.
A request with no body, an empty JSON object or an empty `recordName` changes nothing
and still answers `200`. In a JSON body the name is trimmed first (so a blank name is
read as empty and changes nothing); in a multipart form it is not, and a blank name
is refused with `400`. Fields other than `recordName` and `file` are ignored.

**Updating file content:**

Include a new file in a multipart request to replace the existing content. The file
extension must match the original: a file with another extension is answered `500`,
not `400`. When a file is sent, `recordName` is ignored and the record is named after
the file (without its extension).

**Side effects:**

- Updates `updatedAtTimestamp`
- A new file is stored as the next version of the record's storage document and the
  record is queued for indexing again. The record's own `version` and `sizeInBytes`
  are not updated by this call.

**Known gaps:**

- Renaming a record that is in the trash is not refused: the answer is `200` with the
  success message, but nothing changes, and `record` is the trashed record (`isDeleted: true`,
  with `deletedAtTimestamp`, `deleteBatchId` and `deleteSource`).
- `fileBuffer` is an internal field filled by the upload parser. A JSON body that
  supplies an object under that name (`buffer`, `originalname`, `mimetype`, `size`,
  `lastModified`) is treated as an uploaded file and stored as the new version.

**OAuth scopes:** `kb:write`, plus `kb:read`: replacing the file first reads the record and its knowledge base with the caller's token.


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

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `record_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | Record ID                                                               |
| `record_name`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | New name for the record (rename only; a file needs the multipart form). |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UpdateRecordResponseSchema](../../models/updaterecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_record_form

Update a record's name and/or file content.

**Overview:**

Allows updating the display name and optionally replacing the file content. Triggers re-indexing when content changes.

**Required permission:**

WRITER or higher on the record's knowledge base. A READER is answered `403`; a caller
with no role is answered `404`.

**Renaming:**

Send `recordName` as a multipart field or in a JSON body. There is no length limit.
A request with no body, an empty JSON object or an empty `recordName` changes nothing
and still answers `200`. In a JSON body the name is trimmed first (so a blank name is
read as empty and changes nothing); in a multipart form it is not, and a blank name
is refused with `400`. Fields other than `recordName` and `file` are ignored.

**Updating file content:**

Include a new file in a multipart request to replace the existing content. The file
extension must match the original: a file with another extension is answered `500`,
not `400`. When a file is sent, `recordName` is ignored and the record is named after
the file (without its extension).

**Side effects:**

- Updates `updatedAtTimestamp`
- A new file is stored as the next version of the record's storage document and the
  record is queued for indexing again. The record's own `version` and `sizeInBytes`
  are not updated by this call.

**Known gaps:**

- Renaming a record that is in the trash is not refused: the answer is `200` with the
  success message, but nothing changes, and `record` is the trashed record (`isDeleted: true`,
  with `deletedAtTimestamp`, `deleteBatchId` and `deleteSource`).
- `fileBuffer` is an internal field filled by the upload parser. A JSON body that
  supplies an object under that name (`buffer`, `originalname`, `mimetype`, `size`,
  `lastModified`) is treated as an uploaded file and stored as the new version.

**OAuth scopes:** `kb:write`, plus `kb:read`: replacing the file first reads the record and its knowledge base with the caller's token.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateRecord_form" method="put" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_record_form(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `record_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | Record ID                                                               |
| `record_name`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | New name for the record (rename only; a file needs the multipart form). |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UpdateRecordResponseSchema](../../models/updaterecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_record

Delete a record from the knowledge base.

**Required permission:**

WRITER or higher on the record's knowledge base. A READER is answered `403`; a caller
with no role, an unknown id and a record that is already in the trash are all answered `404`.
The query string and any request body are ignored.

**What gets deleted:**

- Record metadata
- Associated storage file
- Indexed content and embeddings

**Trash:** With "Move Deleted Records to the Trash" on in Labs, the record
goes to the trash instead: it disappears from search, chat and lists at once,
its embeddings are removed, and the record and its file stay until the scheduled
purge. The response then carries `softDeleted: true` and the `batchId`, and the
record can be brought back with `POST /knowledgeBase/record/{recordId}/restore`.
With the setting off, the delete is immediate and cannot be undone.
A folder sent to the trash this way goes alone: the records inside it stay live and
readable. `DELETE /knowledgeBase/{kbId}/folder/{folderId}` trashes a folder with its
contents.


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
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## restore_record

Bring a record back from the trash, together with everything deleted in the
same action: a folder comes back with its contents, a file with its
attachments, a multi-select delete with every item it removed.

Needs "Move Deleted Records to the Trash" on in Labs.

**Required permission:** the role the delete needed. A single file needs
OWNER, WRITER or FILEORGANIZER on its collection; a folder or several items
need OWNER or WRITER.

**Names:** an item whose name another item next to it now uses comes back
as "name (restored)" (a file keeps its extension: "report (restored).pdf").

**Search:** restored files are indexed again, so they return to search and
chat once indexing finishes. `reindexPending` lists any that could not be
queued; reindex those by hand. A file that is back but whose indexing never
started is queued again when it is restored again, and the indexing service
queues it on its own after about an hour.

A record that is not in the trash answers 200 with nothing restored.
The query string and any request body are ignored.


### Example Usage

<!-- UsageSnippet language="python" operationID="restoreRecord" method="post" path="/knowledgeBase/record/{recordId}/restore" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.restore_record(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID of any item in the delete batch                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RestoreRecordResponseSchema](../../models/restorerecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## restore_records

Restore up to 100 records from the trash. Each id is restored as
`POST /knowledgeBase/record/{recordId}/restore` restores it, with everything
deleted along with it; ids from one delete are restored once. Every id gets its
own outcome in `results`, so one refusal does not hold the others back, and the
answer is 200 whatever the outcomes: with the trash turned off in Labs every id is
refused with `code: 403` inside a 200. An id listed twice is answered once. Body
fields other than `recordIds` are ignored.


### Example Usage

<!-- UsageSnippet language="python" operationID="restoreRecords" method="post" path="/knowledgeBase/records/restore" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.restore_records(record_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `record_ids`                                                                        | List[*str*]                                                                         | :heavy_check_mark:                                                                  | Record ids to restore. An id listed more than once is restored, and answered, once. |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.RestoreRecordsResponseSchema](../../models/restorerecordsresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 409          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_trash

One page of what was deleted from a collection and can still be restored,
newest first. Each item is what one delete removed, as a restore brings it back
whole: a folder deleted with its contents is one item, and so is a multi-select
delete (`rootCount` items selected, some named in `otherRootNames`). `itemCount`
says how many records it holds, the folder included.

A folder deleted with `DELETE /knowledgeBase/{kbId}/folder/{folderId}` takes its
contents along. A folder deleted with `DELETE /knowledgeBase/record/{recordId}`
goes to the trash alone (`itemCount` 1): the records inside it stay live.
Restore an item with `POST /knowledgeBase/record/{recordId}/restore`, using its `id`.

Needs "Move Deleted Records to the Trash" on in Labs.

**Who sees what:** the list holds what the caller may restore. OWNER and
WRITER see every item; FILEORGANIZER sees single files only; other roles are
refused. The workspace and user always come from the sign-in.

**Removed for good:** the scheduled cleanup may remove an item from
`removableAfterTimestamp` on (at least 14 days after it was deleted by
default; it runs every 14 days, so an item stays 14 to 28 days). It is
absent when the retention settings can't be read.

An item whose folder is also in the trash (`parentInTrash`) can only be
restored after that folder.

**Request:** query parameters other than `page` and `limit` are ignored. A page past
the last one is answered `200` with no items.


### Example Usage

<!-- UsageSnippet language="python" operationID="listTrash" method="get" path="/knowledgeBase/{kbId}/trash" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.list_trash(kb_id="<id>", page=1, limit=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Collection (knowledge base) ID                                      |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTrashResponseSchema](../../models/listtrashresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream_record_buffer

Stream the binary content of a record's file.

**Overview:**

Returns the stored file's bytes with the file's own `Content-Type` (for an uploaded
file, the MIME type it was uploaded with, followed by `; charset=utf-8`, for example
`text/plain; charset=utf-8` or `application/json; charset=utf-8`). No
`Content-Disposition` header is sent for uploaded files.

**Use cases:**

- File downloads
- Inline document preview
- Content extraction pipelines

**Format conversion:**

`convertTo=application/pdf` asks for a PDF rendering of documents that can be
converted. Any other value, and the conversion request for a plain-text file, is
ignored: the original file is returned.

**Access:** the caller needs access to the record (any role on its knowledge base).
Without it, and for a record in the trash, the answer is `403`. An unknown record, or
an id that is not a record (a knowledge base id), is `404`. A folder has no content:
the answer is `502`.

**Errors** that come from the connector service are relayed with its status as
`{"error": "<message>"}` (`StreamRecordErrorResponse`); errors raised by the gateway
itself (`400`, `401`, scope `403`, malformed body `500`) use `ErrorResponse`.

**Request:** unknown query parameters are ignored.


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

| Parameter                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                        | Record ID                                                                                                                                                                                                                                                 |
| `convert_to`                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                        | Target format for conversion. Only `application/pdf` has an effect, and only for<br/>documents that can be converted. Sending it more than once is refused with `400`.<br/>                                                                               |
| `version`                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                        | Registry version to pin ARTIFACT record content to. Omit to stream<br/>the latest version. Ignored for non-artifact records. Must be written as digits<br/>only; anything else (`-1`, `1.5`, an empty value) or sending it more than once is<br/>refused with `400`.<br/> |
| `retries`                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                       |

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
| errors.ErrorResponse             | 500                              | application/json                 |
| errors.StreamRecordErrorResponse | 502                              | application/json                 |
| errors.PipeshubDefaultError      | 4XX, 5XX                         | \*/\*                            |

## create_folder

Create a folder in a knowledge base. Omit `folderId` to create at the KB root;
pass `folderId` as a query parameter to create a nested subfolder inside an
existing parent folder.

**Required permission:** WRITER or higher

**Folder features:**

- Organize records hierarchically
- Support nested subfolders, up to 20 levels deep
- Inherit parent KB permissions

**Naming rules:**

- Whitespace around the name is removed first; then 1–255 characters
- A name holding an HTML tag, a `javascript:` URL or an inline event handler is
  refused with `400` before authentication; one holding a printf-style format
  specifier (`%s`, `%x`, `%n`, `%p`) is refused with `400` by the gateway controller
- Spaces and special characters allowed
- A name already used by a folder in the same parent is refused with `409`, ignoring
  case (`Reports` and `rEPORTS` clash). A file of the same name, or a folder of the
  same name under another parent, does not clash.

**Request:** only `folderName` and the `folderId` query parameter are read; other body
fields and query parameters are ignored, except a `folderId`, `parentId` or
`parent_id` in the body and a `parentId` or `parent_id` query parameter, which are
refused with `400`.

**Access:** a caller with no role on the knowledge base gets `404`
(`Knowledge base <kbId> not found`), a `READER` gets `403`.

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

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kb_id`                                                                                                                                                                                | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Knowledge base ID                                                                                                                                                                      |                                                                                                                                                                                        |
| `folder_name`                                                                                                                                                                          | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Name of the folder. Whitespace around it is removed first, so a name made<br/>only of whitespace is refused as empty.<br/>It cannot contain `/` or `\`, which folder paths use as separators.<br/> | Project Documents                                                                                                                                                                      |
| `folder_id`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Parent folder ID. Omit to create at the knowledge base root. An id that is not a<br/>folder of this knowledge base (unknown, or a file) is answered `404`.<br/>                        |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.FolderCreateResponseSchema](../../models/foldercreateresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_subfolder

Create a nested subfolder inside an existing parent folder, named by the `folderId`
path parameter. It runs the same validator and handler as
`POST /knowledgeBase/{kbId}/folder`. A `folderId` query parameter is still read: one
that names a different folder than the path is refused with `400`.

**Required permission:** WRITER or higher

**Folder features:**

- Organize records hierarchically
- Support nested subfolders, up to 20 levels deep
- Inherit parent KB permissions

**Naming rules:**

- Whitespace around the name is removed first; then 1–255 characters
- A name holding an HTML tag, a `javascript:` URL or an inline event handler is
  refused with `400` before authentication; one holding a printf-style format
  specifier (`%s`, `%x`, `%n`, `%p`) is refused with `400` by the gateway controller
- Spaces and special characters allowed
- A name already used by a folder in the same parent is refused with `409`, ignoring
  case (`Reports` and `rEPORTS` clash). A file of the same name, or a folder of the
  same name under another parent, does not clash.

**Request:** only `folderName` and the `folderId` query parameter are read; other body
fields and query parameters are ignored, except a `folderId`, `parentId` or
`parent_id` in the body and a `parentId` or `parent_id` query parameter, which are
refused with `400`.

**Access:** a caller with no role on the knowledge base gets `404`
(`Knowledge base <kbId> not found`), a `READER` gets `403`.

**Response:** Returns `id` and `name` for the created folder.


### Example Usage

<!-- UsageSnippet language="python" operationID="createSubfolder" method="post" path="/knowledgeBase/{kbId}/folder/{folderId}/subfolder" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.create_subfolder(kb_id="<id>", folder_id_path_parameter="<id>", folder_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kb_id`                                                                                                                                                                                | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Knowledge base ID                                                                                                                                                                      |                                                                                                                                                                                        |
| `folder_id_path_parameter`                                                                                                                                                             | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Parent folder ID. An id that is not a folder of this knowledge base (unknown, or a<br/>file) is answered `404`.<br/>                                                                   |                                                                                                                                                                                        |
| `folder_name`                                                                                                                                                                          | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Name of the folder. Whitespace around it is removed first, so a name made<br/>only of whitespace is refused as empty.<br/>It cannot contain `/` or `\`, which folder paths use as separators.<br/> | Project Documents                                                                                                                                                                      |
| `folder_id_query_parameter`                                                                                                                                                            | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Optional. When sent, it must equal the `folderId` path parameter (`Conflicting<br/>folderId in path and query parameters`).<br/>                                                       |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.FolderCreateResponseSchema](../../models/foldercreateresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_folder

Rename a folder, at the root or nested.

**Required permission:** WRITER or higher. A `READER` gets `403`; a caller with no
role on the knowledge base gets `404` (`Knowledge base not found`).

**Naming rules:** the same as for creating a folder. Whitespace around the name is
removed first; HTML is refused with `400` before authentication and a printf-style
format specifier with `400` by the gateway controller. A name already used by another
folder in the same parent is refused with `409`, ignoring case; renaming a folder to
its own name, or to the name of a file, is allowed.

**Request:** `kbId` and `folderId` are only checked to be non-empty (an id that is not
a UUID is looked up and answered `404`). Only `folderName` is read; other body fields
and any query parameter are ignored.


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

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `kb_id`                                                                                                                                                                                    | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |
| `folder_id`                                                                                                                                                                                | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |
| `folder_name`                                                                                                                                                                              | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | New name of the folder. Whitespace around it is removed first, so a name<br/>made only of whitespace is refused as empty.<br/>It cannot contain `/` or `\`, which folder paths use as separators.<br/> |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

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

**Required permission:** WRITER or higher. A `READER` gets `403`; a caller with no
role on the knowledge base gets `404`.

**Cascade delete:**

All subfolders and records within are deleted for good, unless "Move Deleted Records
to the Trash" (Labs flag `ENABLE_SOFT_DELETE`) is on: then they all go to the trash and
can be brought back with `POST /knowledgeBase/record/{folderId}/restore`. The response
is the same in both cases. Known gap: while in the trash, the folder is still listed
in `folders` by `GET /knowledgeBase/{kbId}`, although its records answer `404`.

**Request:** `kbId` and `folderId` are only checked to be non-empty; any query string
or body is ignored.


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
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
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
A path with folders (`docs/2026/a.txt`) creates those folders, as a folder upload does.

**Rejected files**

A file whose extension is not supported, or that is larger than the size limit, does
not fail the request: it is reported as a `file:failed` event (`reason`
`UNSUPPORTED_TYPE` or `EXCEEDS_SIZE_LIMIT`, `stage: upload`) and the other files go on.
A file whose name is already used in the same place fails the same way with `reason`
`DUPLICATE_NAME` and `stage: index`. The request still answers `200` when every file
failed. There is no `413`.

**Ignored fields**

`recordName`, `recordType` and `origin` are validated (non-empty, and `recordName` is
checked for HTML and format specifiers) but do not affect the records: each record is
named after its file, with origin `UPLOAD` and type `FILE`. Other fields and unknown
query parameters are ignored; `rejectedFiles` and `fileBuffers` are set by the gateway
itself, so a value sent for them is replaced.

**Access**

`OWNER` and `WRITER` may upload. A `READER` gets `403`; a caller with no role on the
knowledge base gets `404`. Only a multipart body is read: a JSON body has no files and
is refused with `400`.

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

    res = pipeshub.knowledge_base.upload_records(kb_id="<id>", files=[], files_metadata=[
        {
            "file_path": "/docs/report.pdf",
            "last_modified": 2024.0,
        },
    ], is_versioned="true", record_type="FILE")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `kb_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Knowledge base ID (UUID)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `files`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | List[[models.UploadRecordsFile](../../models/uploadrecordsfile.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Files to upload (max 1000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `folder_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Target folder ID. Omit to upload to the KB root. A folder that is not in this<br/>knowledge base is answered `404`.<br/>                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `files_metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | List[[models.FilesMetadatum](../../models/filesmetadatum.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | JSON text: an array with one entry per file, in the order of the `files`<br/>parts, each `{file_path, last_modified}` with `last_modified` in epoch<br/>milliseconds (a number, not a date string). A file without an entry is<br/>named after its part and timed at the upload. Text that is not JSON, or an<br/>array whose length differs from the number of files, is refused with `400`<br/>(`HTTP_BAD_REQUEST`); an entry without a string `file_path` or a numeric<br/>`last_modified` is refused with `400` (`VALIDATION_ERROR`).<br/> | [{"file_path":"docs/report.pdf","last_modified":1705314600000}]                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `is_versioned`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[models.IsVersioned]](../../models/isversioned.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Enable version tracking. `true`/`1` and `false`/`0`/empty are read as<br/>booleans; any other text is answered `500` (the validator throws a plain<br/>error).<br/>                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `record_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Validated, then ignored (records are named after their files).                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `origin`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Validated, then ignored (records get origin `UPLOAD`).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `record_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Validated, then ignored (records get type `FILE`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Response

**[Union[eventstreaming.EventStream[models.UploadStreamSSEEvent], eventstreaming.EventStreamAsync[models.UploadStreamSSEEvent]]](../../models/.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500                          | application/json             |
| errors.PipeshubDefaultError  | 4XX, 5XX                     | \*/\*                        |

## get_upload_limits

Retrieve current upload constraints for the organization.

**Use case:** Call this before uploads to validate file sizes on the client
side and display appropriate limits to users.

`maxFilesPerRequest` is a fixed 1000. `maxFileSizeBytes` is the organization's
`fileUploadMaxSizeBytes` platform setting, read on every call (30 MB when the
setting cannot be read). Any signed-in member gets the same values; no knowledge
base role is needed.

**Request:** there is no validator and nothing from the request is read; any query
string is ignored.


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
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_record

Trigger reindexing for a specific record.

**Overview:**

Reprocesses the record's content to update search indexes and AI embeddings. Useful after content changes or to fix indexing failures.

**Depth parameter:**

Controls processing depth for complex documents (`-1` for full depth, `0`–`100` for limited).

**Status filters:**

Optional `statusFilters` array limits reindex to records in matching indexing states
(e.g. `FAILED`, `AUTO_INDEX_OFF`, `PASSWORD_PROTECTED`). Any string is accepted.

**Access:** any role on the record's knowledge base may reindex it, `READER` included.
For a connector record, read access to the record is enough. A record of a disabled
connector is refused with `409`, a record in the trash with `400`.

**Request:** only `depth` and `statusFilters` are read; other body fields (`force`
included) and any query parameter are ignored. The body is optional.


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

    res = pipeshub.knowledge_base.reindex_record(record_id="<id>", depth=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                                                          | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | N/A                                                                                                                                                  |
| `depth`                                                                                                                                              | *Optional[int]*                                                                                                                                      | :heavy_minus_sign:                                                                                                                                   | Child traversal depth (`0` = record only; higher values include<br/>descendants; `-1` = all of them; `100` is used by clients for folder-like reindex).<br/> |
| `status_filters`                                                                                                                                     | List[*str*]                                                                                                                                          | :heavy_minus_sign:                                                                                                                                   | When set, only records whose indexing status matches one of these<br/>values are reindexed (applies to the record and its descendants per `depth`).<br/> |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[models.ReIndexRecordResponseSchema](../../models/reindexrecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_record_group

Trigger reindexing for all records in a record group.

**Overview:**

Batch reindex operation for a connector's container (a drive, a space, a channel, a
crawled site). Record groups are written by connector syncs only: a knowledge base id
or a knowledge base folder id is not a record group and is answered `404` (reindex
those with `POST /knowledgeBase/reindex/record/{recordId}` and a depth).

**Status filters:**

Optional `statusFilters` limit which child records are queued (e.g. failed-only or
manual-indexing). Any string is accepted.

**Access:** the caller needs access to the record group (an organization-wide
connector gives it to every member; a personal one only to its owner); without it the
answer is `403`. A record group of a disabled connector is refused with `409`.

**Request:** only `depth` and `statusFilters` are read; other body fields (`force`
included) and any query parameter are ignored. The body is optional.


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

    res = pipeshub.knowledge_base.reindex_record_group(record_group_id="<id>", depth=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `record_group_id`                                                                                          | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Record group ID (from a connector sync; not a knowledge base or folder id)                                 |
| `depth`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | Depth of records under the record group to include. `-1` (everything) is applied,<br/>and answered, as `100`.<br/> |
| `status_filters`                                                                                           | List[*str*]                                                                                                | :heavy_minus_sign:                                                                                         | When set, only records matching these indexing statuses are reindexed.<br/>                                |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

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

Set `newParentId` to a folder ID to move the record into that folder, or `null` (or an
empty string) to move it to the knowledge base root. A folder moves with everything in
it. Moving a record to where it already is answers `200` with the same body.

**Required Permission:** OWNER or WRITER. A `READER` gets `403`; a caller with no role
on the knowledge base gets `404` (`Knowledge base not found`).

**Request:** only `newParentId` is read; other body fields and any query parameter
are ignored.


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

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `kb_id`                                                                                                                          | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | Knowledge base UUID                                                                                                              |
| `record_id`                                                                                                                      | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | Record identifier (file or folder). A record that is not in this knowledge base<br/>(unknown, or in another one) is answered `404`.<br/> |
| `new_parent_id`                                                                                                                  | *Nullable[str]*                                                                                                                  | :heavy_check_mark:                                                                                                               | Target folder ID, or null to move the record to the knowledge base root                                                          |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.KnowledgeBaseMoveRecordResponse](../../models/knowledgebasemoverecordresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
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

**A connected app with a limit**

A token that may see only some sources pages and counts only what
its limit lets it see:
- Limited to whole sources (apps or collections) only: the listing
  and the search cover those, with exact totals and counts.
- Limited to any spaces, folders or files, alone or beside whole
  sources: the listing returns each whole source, space (record
  group), folder and file the limit names, one item each, to open
  by its `id`. `totalItems` counts those items, not what is inside
  them. A search reads
  forward only (`prevCursor` is always null), and takes a `page`
  number up to 5; for later pages, send `nextCursor`. Its `totalItems` counts
  the matches found so far and can grow from page to page; it is
  final once `hasNext` is false. `counts` is returned only when the
  whole result fits in the first page read, and is `null` otherwise.
- An item can sit in a folder the limit leaves out, as a file the
  limit names does. Its `parentId` and `parent` are then `null`: the
  item is returned, and the folder above it is not named.
- A `nextCursor` or `prevCursor` belongs to the limit it was read
  under. A token with a different limit that sends it gets a `400`;
  start that listing again without a cursor.

**Access control**

Requires a valid bearer token. For OAuth tokens the `kb:read` scope
must be present; regular JWT bearer tokens pass through without scope
enforcement. Only nodes the caller can access are listed.

**Request checking**

This route has no request validator of its own; the query is passed on and
checked by the connector service. Query parameters not listed here are
ignored. A wrong type for `page`, `limit`, `onlyContainers` or `flattened`
(or `page` below 1 or `limit` outside 1-200, or either sent more than once) is answered
`422`; a refused filter value is answered `400`.


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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `only_containers`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | When `true`, only nodes that have children are returned (useful for<br/>building sidebar / tree navigation). Leaf nodes are excluded.<br/>`yes`/`no`, `on`/`off` and `1`/`0` are read as booleans too; anything<br/>else is answered `422`.<br/>                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Page number (1-indexed, at most 50). Combined with `limit` to paginate results.<br/>Prefer `cursor`: a page number is reached by reading the pages before it.<br/>A search by a connected app whose limit names any spaces, folders or files<br/>takes a page number of at most 5; for later pages, send `nextCursor`.<br/>                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Opaque cursor from `pagination.nextCursor` or `pagination.prevCursor` of a previous<br/>response. It decides the listing mode, parent, filters and sort. `include` and<br/>`limit` come from this request. A next cursor returns the following page, and a previous<br/>cursor returns the page before. A cursor whose parent disagrees with the URL, or<br/>that was issued for another user, is refused with 400.<br/>                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Maximum number of items to return per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sort_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.GetKnowledgeHubRootNodesSortBy]](../../models/getknowledgehubrootnodessortby.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Field to sort results by. Omitted → default `updatedAt`.<br/>Any other value is answered `400` ("Invalid sort_by: ...").<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sort_order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[models.GetKnowledgeHubRootNodesSortOrder]](../../models/getknowledgehubrootnodessortorder.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Sort direction. Omitted → default `desc`. Read case-insensitively;<br/>any other value is answered `400` ("Invalid sort_order: ...").<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `q`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Full-text search query. Must be between 2 and 500 characters<br/>(inclusive) after surrounding whitespace is removed, otherwise `400`.<br/>When provided, the endpoint searches across the entire<br/>node tree regardless of the current browse level.<br/>A repeated `q` is joined with commas into one query, and a `q` sent as an object<br/>(`q[a]=b`) is refused with `400` ("Search query must be text").<br/>                                                                                                                                                           | quarterly report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `node_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of node types to include. An unknown value is<br/>answered `400` ("Invalid node_types value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `folder`, `app`, `recordGroup`, `record`<br/>                                                                                                                                                                                                                                                                                                                                                             | app,recordGroup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `record_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of record types to include. An unknown value is<br/>answered `400` ("Invalid record_types value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `FILE`, `DRIVE`, `WEBPAGE`, `DATABASE`, `DATASOURCE`,<br/>`MESSAGE`, `MAIL`, `GROUP_MAIL`, `TICKET`, `COMMENT`,<br/>`INLINE_COMMENT`, `CONFLUENCE_PAGE`, `CONFLUENCE_BLOGPOST`,<br/>`SHAREPOINT_PAGE`, `SHAREPOINT_LIST`, `SHAREPOINT_LIST_ITEM`,<br/>`SHAREPOINT_DOCUMENT_LIBRARY`, `LINK`, `PROJECT`, `PULL_REQUEST`,<br/>`MEETING`, `PRODUCT`, `DEAL`, `CASE`, `TASK`, `ARTIFACT`,<br/>`CODE_FILE`, `SQL_TABLE`, `SQL_VIEW`, `OTHERS`<br/> | FILE,CONFLUENCE_PAGE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `origins`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of origin types to include. An unknown value is<br/>answered `400` ("Invalid origins value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `COLLECTION`, `CONNECTOR`<br/>                                                                                                                                                                                                                                                                                                                                                                             | CONNECTOR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `connector_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of connector instance IDs (UUIDs) to filter by.<br/>Maximum 100 items. No enum validation — any string is accepted, but<br/>non-existent IDs simply yield zero results.<br/>                                                                                                                                                                                                                                                                                                                                                                               | f3a4b5b6-5b6c-4e85-9097-3202cfe696fc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `indexing_status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of indexing statuses to include. An unknown value<br/>is answered `400` ("Invalid indexing_status value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `NOT_STARTED`, `PAUSED`, `IN_PROGRESS`, `COMPLETED`,<br/>`FAILED`, `FILE_TYPE_NOT_SUPPORTED`, `AUTO_INDEX_OFF`, `EMPTY`,<br/>`ENABLE_MULTIMODAL_MODELS`, `QUEUED`, `SKIPPED`, `PASSWORD_PROTECTED`<br/>                                                                                                                                                                                       | COMPLETED,FAILED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Created-date range filter. Format: `gte:<epochMs>,lte:<epochMs>`.<br/>Both bounds are optional (you may send just `gte:...` or just<br/>`lte:...`). Timestamps must be in the range 0 to 9999999999999 and<br/>`gte` must be less than or equal to `lte` when both are present;<br/>a bound that is not a whole number, is out of range, or an inverted<br/>range is answered `400`. A value with no `gte:`/`lte:` part is ignored.<br/>                                                                                                                                        | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `updated_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Updated-date range filter. Same format and constraints as `createdAt`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | File-size range filter in bytes. Format: `gte:<bytes>,lte:<bytes>`.<br/>Both bounds are optional. Values must be non-negative and at most<br/>1099511627776 (1 TB). `gte` must be less than or equal to `lte`<br/>when both are present.<br/>                                                                                                                                                                                                                                                                                                                                   | gte:0,lte:10485760                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `flattened`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Force flattened/recursive search (`true`) or direct top-level<br/>listing (`false`). When omitted, it's computed from whether any<br/>of `q`, `nodeTypes`, `recordTypes`, `origins`, `connectorIds`,<br/>`indexingStatus`, `createdAt`, `updatedAt`, or `size` are present —<br/>if any are, results are flattened automatically; otherwise only<br/>top-level nodes are returned.<br/>                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `include`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of additional response sections to include.<br/>An unknown value is answered `400` ("Invalid include value(s): ...").<br/>Maximum 100 items.<br/><br/>Valid values: `breadcrumbs`, `counts`, `availableFilters`, `permissions`<br/>                                                                                                                                                                                                                                                                                                                        | availableFilters,counts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.GetKnowledgeHubRootNodesResponse](../../models/getknowledgehubrootnodesresponse.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| errors.ErrorResponse                                    | 400, 401, 403                                           | application/json                                        |
| errors.GetKnowledgeHubRootNodesUnprocessableEntityError | 422                                                     | application/json                                        |
| errors.ErrorResponse                                    | 500                                                     | application/json                                        |
| errors.GetKnowledgeHubRootNodesServiceUnavailableError  | 503                                                     | application/json                                        |
| errors.PipeshubDefaultError                             | 4XX, 5XX                                                | \*/\*                                                   |

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
- `parentId` must be a standard UUID

**Filtering and searching**

All query-param filters from the root endpoint are available here and
operate within the scope of the parent node's subtree. When `q` is
provided, the search spans all descendants of the parent node.

**Response extras**

When `include=breadcrumbs` is set, the response contains a
`breadcrumbs` array tracing the path from the root to the current
node. The `currentNode` object is always populated for non-root
requests. `parentNode` is too, except at the top of a source and for
a connected app whose limit leaves that parent out: it is `null` then.

**Access control**

Requires a valid bearer token. For OAuth tokens the `kb:read` scope
must be present; regular JWT bearer tokens pass through without scope
enforcement.

A parent the caller may not see, one in the trash, and one that does not
exist are all answered `404` with the same body, so the route does not reveal
whether the node exists.

**Request checking**

This route has no request validator of its own; the path values and the query
are checked by the connector service. Query parameters not listed here are
ignored. A wrong type for `page`, `limit`, `onlyContainers` or `flattened`
(or `page` below 1 or `limit` outside 1-200) is answered `422`; other refusals,
`page` above 50 and an unusable `cursor` included, are `400`.


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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `parent_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [models.ParentType](../../models/parenttype.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Type of the parent node whose children to retrieve.<br/><br/>Must be one of: `app`, `recordGroup`, `folder`, `record` (case-sensitive).<br/>Any other value returns a 400 error, and so does a type that does not<br/>match what `parentId` is (for example `folder` with a knowledge base id).<br/>                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `parent_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Identifier of the parent node. Must be a valid UUID<br/>(e.g. `f3a4b5b6-5b6c-4e85-9097-3202cfe696fc`).<br/><br/>Any value that does not match this format returns a 400 error. The format<br/>check ignores letter case but ids are stored in lower case, so an<br/>upper-case UUID passes the check and is answered 404.<br/>                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `only_containers`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | When `true`, only nodes that have children are returned (useful for<br/>building sidebar / tree navigation). Leaf nodes are excluded.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Page number (1-indexed, at most 50). Combined with `limit` to paginate results.<br/>Prefer `cursor`: a page number is reached by reading the pages before it.<br/>                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Opaque cursor from `pagination.nextCursor` or `pagination.prevCursor` of a previous<br/>response. It decides the listing mode, parent, filters and sort. `include` and<br/>`limit` come from this request. A next cursor returns the following page, and a previous<br/>cursor returns the page before. A cursor whose parent disagrees with the URL, or<br/>that was issued for another user, is refused with 400.<br/>                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Maximum number of items to return per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sort_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.GetKnowledgeHubChildNodesSortBy]](../../models/getknowledgehubchildnodessortby.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Field to sort results by. Omitted → default `updatedAt`.<br/>Any other value is answered `400` ("Invalid sort_by: ...").<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sort_order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[models.GetKnowledgeHubChildNodesSortOrder]](../../models/getknowledgehubchildnodessortorder.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Sort direction. Omitted → default `desc`. Read case-insensitively;<br/>any other value is answered `400` ("Invalid sort_order: ...").<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `q`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Full-text search query. Must be between 2 and 500 characters<br/>(inclusive) after surrounding whitespace is removed, otherwise `400`.<br/>When provided, the endpoint searches across all<br/>descendants of the parent node.<br/>A repeated `q` is joined with commas into one query, and a `q` sent as an object<br/>(`q[a]=b`) is refused with `400` ("Search query must be text").<br/>                                                                                                                                                                                    | quarterly report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `node_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of node types to include. An unknown value is<br/>answered `400` ("Invalid node_types value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `folder`, `app`, `recordGroup`, `record`<br/>                                                                                                                                                                                                                                                                                                                                                             | recordGroup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `record_types`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of record types to include. An unknown value is<br/>answered `400` ("Invalid record_types value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `FILE`, `DRIVE`, `WEBPAGE`, `DATABASE`, `DATASOURCE`,<br/>`MESSAGE`, `MAIL`, `GROUP_MAIL`, `TICKET`, `COMMENT`,<br/>`INLINE_COMMENT`, `CONFLUENCE_PAGE`, `CONFLUENCE_BLOGPOST`,<br/>`SHAREPOINT_PAGE`, `SHAREPOINT_LIST`, `SHAREPOINT_LIST_ITEM`,<br/>`SHAREPOINT_DOCUMENT_LIBRARY`, `LINK`, `PROJECT`, `PULL_REQUEST`,<br/>`MEETING`, `PRODUCT`, `DEAL`, `CASE`, `TASK`, `ARTIFACT`,<br/>`CODE_FILE`, `SQL_TABLE`, `SQL_VIEW`, `OTHERS`<br/> | FILE,CONFLUENCE_PAGE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `origins`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of origin types to include. An unknown value is<br/>answered `400` ("Invalid origins value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `COLLECTION`, `CONNECTOR`<br/>                                                                                                                                                                                                                                                                                                                                                                             | CONNECTOR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `connector_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of connector instance IDs (UUIDs) to filter by.<br/>Maximum 100 items. No enum validation — any string is accepted, but<br/>non-existent IDs simply yield zero results.<br/>                                                                                                                                                                                                                                                                                                                                                                               | f3a4b5b6-5b6c-4e85-9097-3202cfe696fc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `indexing_status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of indexing statuses to include. An unknown value<br/>is answered `400` ("Invalid indexing_status value(s): ..."). Maximum 100 items.<br/><br/>Valid values: `NOT_STARTED`, `PAUSED`, `IN_PROGRESS`, `COMPLETED`,<br/>`FAILED`, `FILE_TYPE_NOT_SUPPORTED`, `AUTO_INDEX_OFF`, `EMPTY`,<br/>`ENABLE_MULTIMODAL_MODELS`, `QUEUED`, `SKIPPED`, `PASSWORD_PROTECTED`<br/>                                                                                                                                                                                       | COMPLETED,FAILED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Created-date range filter. Format: `gte:<epochMs>,lte:<epochMs>`.<br/>Both bounds are optional (you may send just `gte:...` or just<br/>`lte:...`). Timestamps must be in the range 0 to 9999999999999 and<br/>`gte` must be less than or equal to `lte` when both are present.<br/>                                                                                                                                                                                                                                                                                            | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `updated_at`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Updated-date range filter. Same format and constraints as `createdAt`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | gte:1700000000000,lte:1710000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | File-size range filter in bytes. Format: `gte:<bytes>,lte:<bytes>`.<br/>Both bounds are optional. Values must be non-negative and at most<br/>1099511627776 (1 TB). `gte` must be less than or equal to `lte`<br/>when both are present.<br/>                                                                                                                                                                                                                                                                                                                                   | gte:0,lte:10485760                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `flattened`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Force flattened/recursive search (`true`) or direct top-level<br/>listing (`false`). When omitted, it's computed from whether any<br/>of `q`, `nodeTypes`, `recordTypes`, `origins`, `connectorIds`,<br/>`indexingStatus`, `createdAt`, `updatedAt`, or `size` are present —<br/>if any are, results are flattened automatically; otherwise only<br/>top-level nodes are returned.<br/>                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `include`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Comma-separated list of additional response sections to include.<br/>An unknown value is answered `400` ("Invalid include value(s): ...").<br/>Maximum 100 items.<br/><br/>Valid values: `breadcrumbs`, `counts`, `availableFilters`, `permissions`<br/>                                                                                                                                                                                                                                                                                                                        | breadcrumbs,availableFilters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.GetKnowledgeHubChildNodesResponse](../../models/getknowledgehubchildnodesresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.ErrorResponse                                     | 400, 401, 403, 404                                       | application/json                                         |
| errors.GetKnowledgeHubChildNodesUnprocessableEntityError | 422                                                      | application/json                                         |
| errors.ErrorResponse                                     | 500                                                      | application/json                                         |
| errors.GetKnowledgeHubChildNodesServiceUnavailableError  | 503                                                      | application/json                                         |
| errors.PipeshubDefaultError                              | 4XX, 5XX                                                 | \*/\*                                                    |