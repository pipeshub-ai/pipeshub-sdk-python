# KnowledgeHub

## Overview

Unified browse API for root and child nodes (apps, record groups, folders, records) with filtering and search

### Available Operations

* [get_knowledge_hub_root_nodes](#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes
* [get_knowledge_hub_child_nodes](#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes

## get_knowledge_hub_root_nodes

Retrieve root-level nodes (Apps) or search across all nodes for unified knowledge hub browsing.<br><br>
<b>Overview:</b><br>
Provides a unified view across all knowledge sources - Collections, connectors, and apps. Use for building file browser UIs.<br><br>
<b>Node Types:</b><br>
<ul>
<li><b>Collection:</b> Local collections (formerly Knowledge Bases)</li>
<li><b>Connector:</b> External connector instances</li>
<li><b>App:</b> Connected applications</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubRootNodes" method="get" path="/api/v1/knowledgeBase/knowledge-hub/nodes" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_hub.get_knowledge_hub_root_nodes(only_containers=False, page=1, limit=50, sort_by="updatedAt", sort_order="desc", flattened=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `only_containers`                                                                                       | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Only return nodes with children (for sidebar)                                                           |
| `page`                                                                                                  | *Optional[int]*                                                                                         | :heavy_minus_sign:                                                                                      | Page number (1-indexed)                                                                                 |
| `limit`                                                                                                 | *Optional[int]*                                                                                         | :heavy_minus_sign:                                                                                      | Items per page                                                                                          |
| `sort_by`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Sort field (name, createdAt, updatedAt, size, type)                                                     |
| `sort_order`                                                                                            | [Optional[models.GetKnowledgeHubRootNodesSortOrder]](../../models/getknowledgehubrootnodessortorder.md) | :heavy_minus_sign:                                                                                      | Sort order (asc or desc)                                                                                |
| `q`                                                                                                     | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Full-text search query                                                                                  |
| `node_types`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Filter by node types (comma-separated)                                                                  |
| `record_types`                                                                                          | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Comma-separated record types                                                                            |
| `origins`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Comma-separated origins (COLLECTION, CONNECTOR)                                                         |
| `connector_ids`                                                                                         | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Comma-separated connector instance IDs                                                                  |
| `indexing_status`                                                                                       | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Comma-separated indexing statuses                                                                       |
| `created_at`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Created date range (gte:timestamp,lte:timestamp)                                                        |
| `updated_at`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Updated date range (gte:timestamp,lte:timestamp)                                                        |
| `size`                                                                                                  | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Size range (gte:bytes,lte:bytes)                                                                        |
| `flattened`                                                                                             | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Return flattened view with all nested children                                                          |
| `include`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Comma-separated includes (breadcrumbs, counts, availableFilters, permissions)                           |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.KnowledgeHubNodesResponse](../../models/knowledgehubnodesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_knowledge_hub_child_nodes

Get children of a specific node. Retrieve child nodes under a specific parent in the knowledge hub tree.<br><br>
<b>Navigation:</b><br>
Use this to drill down into collections, folders, and connector hierarchies.<br><br>
parent_type must be one of: app, recordGroup, folder, record.


### Example Usage

<!-- UsageSnippet language="python" operationID="getKnowledgeHubChildNodes" method="get" path="/api/v1/knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_hub.get_knowledge_hub_child_nodes(parent_type="recordGroup", parent_id="<id>", only_containers=False, page=1, limit=50, sort_by="updatedAt", sort_order="desc", flattened=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `parent_type`                                                                                             | [models.ParentType](../../models/parenttype.md)                                                           | :heavy_check_mark:                                                                                        | Type of parent node (app, recordGroup, folder, record)                                                    |
| `parent_id`                                                                                               | *str*                                                                                                     | :heavy_check_mark:                                                                                        | ID of parent node (UUID or knowledgeBase_<orgId> for Collection app)                                      |
| `only_containers`                                                                                         | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Only return nodes with children (for sidebar)                                                             |
| `page`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Page number (1-indexed)                                                                                   |
| `limit`                                                                                                   | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Items per page                                                                                            |
| `sort_by`                                                                                                 | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Sort field (name, createdAt, updatedAt, size, type)                                                       |
| `sort_order`                                                                                              | [Optional[models.GetKnowledgeHubChildNodesSortOrder]](../../models/getknowledgehubchildnodessortorder.md) | :heavy_minus_sign:                                                                                        | Sort order (asc or desc)                                                                                  |
| `q`                                                                                                       | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Full-text search query                                                                                    |
| `node_types`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Filter by node types (comma-separated)                                                                    |
| `record_types`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Comma-separated record types                                                                              |
| `origins`                                                                                                 | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Comma-separated origins (COLLECTION, CONNECTOR)                                                           |
| `connector_ids`                                                                                           | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Comma-separated connector instance IDs                                                                    |
| `indexing_status`                                                                                         | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Comma-separated indexing statuses                                                                         |
| `created_at`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Created date range (gte:timestamp,lte:timestamp)                                                          |
| `updated_at`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Updated date range (gte:timestamp,lte:timestamp)                                                          |
| `size`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Size range (gte:bytes,lte:bytes)                                                                          |
| `flattened`                                                                                               | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Return flattened view with all nested children                                                            |
| `include`                                                                                                 | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Comma-separated includes (breadcrumbs, counts, availableFilters, permissions)                             |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.KnowledgeHubNodesResponse](../../models/knowledgehubnodesresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |