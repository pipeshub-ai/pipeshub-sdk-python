# Records

## Overview

Record management and operations

### Available Operations

* [get_all](#get_all) - Get all records across knowledge bases
* [get](#get) - Get records for a knowledge base
* [get_by_id](#get_by_id) - Get record by ID
* [update](#update) - Update record
* [delete](#delete) - Delete record
* [stream](#stream) - Stream record content
* [move](#move) - Move a record to another folder

## get_all

Retrieve records from all knowledge bases accessible to the user.<br><br>
<b>Overview:</b><br>
Search and filter records across your entire organization. Useful for global search, reporting, and cross-KB content discovery.<br><br>
<b>Filtering Options:</b><br>
<ul>
<li><b>search:</b> Full-text search in record names</li>
<li><b>recordTypes:</b> FILE, WEBPAGE, EMAIL, MESSAGE, TICKET, etc.</li>
<li><b>origins:</b> UPLOAD or CONNECTOR</li>
<li><b>connectors:</b> Filter by connector source</li>
<li><b>indexingStatus:</b> COMPLETED, FAILED, IN_PROGRESS, etc.</li>
<li><b>dateFrom/dateTo:</b> Filter by creation date range</li>
</ul>
<b>Response Includes:</b><br>
<ul>
<li>Paginated record list</li>
<li>Applied and available filter counts</li>
<li>Pagination metadata</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllRecords" method="get" path="/knowledgeBase/records" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.records.get_all(page=1, limit=20, record_types="FILE,WEBPAGE,EMAIL", connectors="GOOGLE_DRIVE,ONEDRIVE", indexing_status="COMPLETED,FAILED", sort_by="createdAtTimestamp", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `page`                                                                            | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |                                                                                   |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |                                                                                   |
| `search`                                                                          | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Search query (max 1000 chars)                                                     |                                                                                   |
| `record_types`                                                                    | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Filter by record types (comma-separated)                                          | FILE,WEBPAGE,EMAIL                                                                |
| `origins`                                                                         | [Optional[models.Origins]](../../models/origins.md)                               | :heavy_minus_sign:                                                                | Filter by origin (comma-separated)                                                |                                                                                   |
| `connectors`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Filter by connector names (comma-separated)                                       | GOOGLE_DRIVE,ONEDRIVE                                                             |
| `indexing_status`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Filter by indexing status (comma-separated)                                       | COMPLETED,FAILED                                                                  |
| `date_from`                                                                       | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | Start date filter (Unix timestamp ms)                                             |                                                                                   |
| `date_to`                                                                         | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | End date filter (Unix timestamp ms)                                               |                                                                                   |
| `sort_by`                                                                         | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |                                                                                   |
| `sort_order`                                                                      | [Optional[models.GetAllRecordsSortOrder]](../../models/getallrecordssortorder.md) | :heavy_minus_sign:                                                                | N/A                                                                               |                                                                                   |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |

### Response

**[models.RecordsResponse](../../models/recordsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve a paginated list of records within a specific knowledge base.<br><br>
<b>Overview:</b><br>
Returns all records (documents, files, content) stored in the specified KB, with powerful filtering and sorting capabilities.<br><br>
<b>Filtering:</b><br>
<ul>
<li><b>search:</b> Search by record name (partial match, max 1000 chars)</li>
<li><b>recordTypes:</b> FILE, WEBPAGE, COMMENT, MESSAGE, EMAIL, TICKET</li>
<li><b>origins:</b> UPLOAD (manual uploads) or CONNECTOR (synced)</li>
<li><b>indexingStatus:</b> Filter by processing state</li>
<li><b>dateFrom/dateTo:</b> Creation date range (Unix timestamps)</li>
</ul>
<b>Sorting:</b><br>
Default sorts by <code>createdAtTimestamp</code> descending (newest first).


### Example Usage

<!-- UsageSnippet language="python" operationID="getKBRecords" method="get" path="/knowledgeBase/{kbId}/records" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.records.get(kb_id="<id>", page=1, limit=20, sort_by="createdAtTimestamp", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `kb_id`                                                                         | *str*                                                                           | :heavy_check_mark:                                                              | Knowledge base ID                                                               |
| `page`                                                                          | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `search`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Search query for record names                                                   |
| `record_types`                                                                  | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Filter by record types (comma-separated)                                        |
| `origins`                                                                       | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Filter by origin                                                                |
| `indexing_status`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Filter by indexing status                                                       |
| `date_from`                                                                     | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | Start date filter (Unix timestamp)                                              |
| `date_to`                                                                       | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | End date filter (Unix timestamp)                                                |
| `sort_by`                                                                       | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `sort_order`                                                                    | [Optional[models.GetKBRecordsSortOrder]](../../models/getkbrecordssortorder.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.RecordsResponse](../../models/recordsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_id

Retrieve detailed information about a specific record.<br><br>
<b>Overview:</b><br>
Returns complete record metadata including name, type, indexing status, storage information, and version history.<br><br>
<b>File Conversion:</b><br>
Use the optional <code>convertTo</code> parameter to request file format conversion (e.g., PDF to text).


### Example Usage

<!-- UsageSnippet language="python" operationID="getRecordById" method="get" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.records.get_by_id(record_id="<id>", convert_to="txt")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID                                                           |                                                                     |
| `convert_to`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional format to convert the file to                              | txt                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Record](../../models/record.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update a record's name and/or file content.<br><br>
<b>Overview:</b><br>
Allows updating the display name and optionally replacing the file content. Triggers re-indexing when content changes.<br><br>
<b>Required Permission:</b> WRITER or higher<br><br>
<b>Updating File Content:</b><br>
Include a new file in the request to replace the existing content. The file extension must match the original.<br><br>
<b>Side Effects:</b><br>
<ul>
<li>Updates <code>updatedAtTimestamp</code></li>
<li>Increments version if file content changed</li>
<li>Triggers re-indexing for content changes</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateRecord" method="put" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.records.update(record_id="<id>")

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
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Permanently delete a record from the knowledge base.<br><br>
<b>Required Permission:</b> WRITER or higher<br><br>
<b>What Gets Deleted:</b><br>
<ul>
<li>Record metadata</li>
<li>Associated storage file</li>
<li>Indexed content and embeddings</li>
</ul>
<b>Warning:</b> This action is irreversible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteRecord" method="delete" path="/knowledgeBase/record/{recordId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.records.delete(record_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## stream

Stream the binary content of a record's file.<br><br>
<b>Overview:</b><br>
Returns the raw file content with appropriate Content-Type and Content-Disposition headers for download or inline viewing.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>File downloads</li>
<li>Inline document preview</li>
<li>Content extraction pipelines</li>
</ul>
<b>Format Conversion:</b><br>
Use <code>convertTo</code> parameter to convert between formats (e.g., DOCX to PDF).


### Example Usage

<!-- UsageSnippet language="python" operationID="streamRecordBuffer" method="get" path="/knowledgeBase/stream/record/{recordId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.records.stream(record_id="<id>")

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

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## move

Move a record (file or folder) to a different parent folder within the same knowledge base.<br><br>
<b>Required Permission:</b> WRITER or higher<br><br>
<b>Moving to Root:</b><br>
Set <code>newParentId</code> to <code>null</code> to move the record to the root level of the knowledge base.


### Example Usage: moveToFolder

<!-- UsageSnippet language="python" operationID="moveRecord" method="put" path="/knowledgeBase/{kbId}/record/{recordId}/move" example="moveToFolder" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.records.move(kb_id="702f8ff0-0a01-4354-b592-eea268f40f25", record_id="<id>", new_parent_id="folder-abc123")

    # Use the SDK ...

```
### Example Usage: moveToRoot

<!-- UsageSnippet language="python" operationID="moveRecord" method="put" path="/knowledgeBase/{kbId}/record/{recordId}/move" example="moveToRoot" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.records.move(kb_id="8bdbd4fc-ec2e-4e15-8a88-ae59a5b4bad2", record_id="<id>", new_parent_id=None)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Record ID to move                                                   |
| `new_parent_id`                                                     | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | ID of the new parent folder, or null to move to root level          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |