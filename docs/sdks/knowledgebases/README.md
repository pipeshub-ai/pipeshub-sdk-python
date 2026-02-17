# KnowledgeBases

## Overview

### Available Operations

* [create](#create) - Create a new knowledge base
* [list](#list) - List all knowledge bases
* [get](#get) - Get knowledge base by ID
* [update](#update) - Update knowledge base
* [delete](#delete) - Delete knowledge base
* [get_root_nodes](#get_root_nodes) - Get knowledge hub root nodes
* [get_child_nodes](#get_child_nodes) - Get knowledge hub child nodes

## create

Create a new knowledge base for organizing and managing documents within your organization.<br><br>
<b>Overview:</b><br>
A knowledge base is a container for organizing related documents, files, and content. It provides a central location for teams to collaborate on shared information.<br><br>
<b>Features:</b><br>
<ul>
<li>Hierarchical folder structure support</li>
<li>Role-based access control (OWNER, ORGANIZER, WRITER, READER, etc.)</li>
<li>Full-text search across all records</li>
<li>Integration with external connectors (Google Drive, OneDrive, etc.)</li>
<li>Automatic content indexing for AI-powered search</li>
</ul>
<b>Naming Rules:</b><br>
<ul>
<li>Name must be 1-255 characters</li>
<li>Special characters and HTML tags are sanitized</li>
<li>Names don't need to be unique within organization</li>
</ul>
<b>Creator Permissions:</b><br>
The user creating the KB automatically becomes the OWNER with full administrative rights.


### Example Usage

<!-- UsageSnippet language="python" operationID="createKnowledgeBase" method="post" path="/knowledgeBase" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.create(kb_name="Product Documentation")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_name`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Name of the knowledge base                                          | Product Documentation                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.KnowledgeBase](../../models/knowledgebase.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list

Retrieve a paginated list of all knowledge bases accessible to the authenticated user.<br><br>
<b>Overview:</b><br>
Returns knowledge bases where the user has at least READER permission. Results include the user's role for each KB.<br><br>
<b>Filtering:</b><br>
<ul>
<li><b>search:</b> Full-text search on KB names (max 1000 chars)</li>
<li><b>permissions:</b> Filter by user's role (comma-separated: OWNER,WRITER,READER)</li>
</ul>
<b>Sorting Options:</b><br>
<ul>
<li><code>name</code> - Alphabetical by KB name</li>
<li><code>createdAtTimestamp</code> - By creation date</li>
<li><code>updatedAtTimestamp</code> - By last modification</li>
<li><code>userRole</code> - By permission level</li>
</ul>
<b>Performance:</b><br>
Uses efficient pagination with limit/offset. For large result sets, use smaller page sizes.


### Example Usage

<!-- UsageSnippet language="python" operationID="listKnowledgeBases" method="get" path="/knowledgeBase" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.list(page=1, limit=20, permissions="OWNER,ORGANIZER,WRITER", sort_by="name", sort_order="asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `page`                                                                                      | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Page number (1-indexed)                                                                     |                                                                                             |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Results per page (max 100)                                                                  |                                                                                             |
| `search`                                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Search query for KB names (max 1000 chars)                                                  |                                                                                             |
| `permissions`                                                                               | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Filter by permission roles (comma-separated)                                                | OWNER,ORGANIZER,WRITER                                                                      |
| `sort_by`                                                                                   | [Optional[models.ListKnowledgeBasesSortBy]](../../models/listknowledgebasessortby.md)       | :heavy_minus_sign:                                                                          | Field to sort by                                                                            |                                                                                             |
| `sort_order`                                                                                | [Optional[models.ListKnowledgeBasesSortOrder]](../../models/listknowledgebasessortorder.md) | :heavy_minus_sign:                                                                          | Sort direction                                                                              |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.ListKnowledgeBasesResponse](../../models/listknowledgebasesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve detailed information about a specific knowledge base.<br><br>
<b>Overview:</b><br>
Returns complete KB metadata including name, timestamps, and the requesting user's role/permissions.<br><br>
<b>Access Control:</b><br>
User must have at least READER permission to view KB details.


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeBase" method="get" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.get(kb_id="kb_550e8400-e29b-41d4-a716")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   | kb_550e8400-e29b-41d4-a716                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.KnowledgeBase](../../models/knowledgebase.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update a knowledge base's name.<br><br>
<b>Required Permission:</b> OWNER or ORGANIZER<br><br>
<b>Validation:</b><br>
<ul>
<li>Name must be 1-255 characters</li>
<li>XSS protection applied to input</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateKnowledgeBase" method="put" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.update(kb_id="<id>", kb_name="Updated Documentation Hub")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   |                                                                     |
| `kb_name`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New name for the knowledge base                                     | Updated Documentation Hub                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.KnowledgeBase](../../models/knowledgebase.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Permanently delete a knowledge base and all its contents.<br><br>
<b>Required Permission:</b> OWNER only<br><br>
<b>What Gets Deleted:</b><br>
<ul>
<li>All folders within the KB</li>
<li>All records and their indexed content</li>
<li>All permission grants</li>
<li>Associated storage files</li>
</ul>
<b>Warning:</b> This action is irreversible. Consider exporting data before deletion.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteKnowledgeBase" method="delete" path="/knowledgeBase/{kbId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.delete(kb_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteKnowledgeBaseResponse](../../models/deleteknowledgebaseresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_root_nodes

Retrieve root-level nodes for unified knowledge hub browsing.<br><br>
<b>Overview:</b><br>
Provides a unified view across all knowledge sources - KBs, connectors, and apps. Use for building file browser UIs.<br><br>
<b>Node Types:</b><br>
<ul>
<li><b>KB:</b> Knowledge bases</li>
<li><b>CONNECTOR:</b> External connector instances</li>
<li><b>APP:</b> Connected applications</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubRootNodes" method="get" path="/knowledgeBase/knowledge-hub/nodes" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.get_root_nodes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | View mode                                                           |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `node_types`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by node types (comma-separated)                              |
| `q`                                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search query                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetKnowledgeHubRootNodesResponse](../../models/getknowledgehubrootnodesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_child_nodes

Retrieve child nodes under a specific parent in the knowledge hub tree.<br><br>
<b>Navigation:</b><br>
Use this to drill down into KBs, folders, and connector hierarchies.


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubChildNodes" method="get" path="/knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.knowledge_bases.get_child_nodes(parent_type="<value>", parent_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `parent_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Type of parent node (KB, FOLDER, CONNECTOR, APP)                    |
| `parent_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of parent node                                                   |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `q`                                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search query                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetKnowledgeHubChildNodesResponse](../../models/getknowledgehubchildnodesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |