# Connector

## Overview

Connector-related operations

### Available Operations

* [reindex_record](#reindex_record) - Reindex single record
* [reindex_record_group](#reindex_record_group) - Reindex record group
* [get_stats](#get_stats) - Get connector statistics

## reindex_record

Trigger reindexing for a specific record.<br><br>
<b>Overview:</b><br>
Reprocesses the record's content to update search indexes and AI embeddings. Useful after content changes or to fix indexing failures.<br><br>
<b>Depth Parameter:</b><br>
Controls processing depth for complex documents (-1 for full depth, 0-100 for limited).


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

    res = pipeshub.connector.reindex_record(record_id="rec-abc123", depth=0, force=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | rec-abc123                                                          |
| `depth`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Processing depth (-1 for unlimited, 0 for only this record)         |                                                                     |
| `force`                                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Force reindexing even if already indexed                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ReindexRecordResponse](../../models/reindexrecordresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_record_group

Trigger reindexing for all records in a folder or knowledge base.<br><br>
<b>Overview:</b><br>
Batch reindex operation for entire containers. The recordGroupId can be a folder ID or KB ID.


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

    res = pipeshub.connector.reindex_record_group(record_group_id="grp-abc123", depth=0, force=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_group_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Folder ID or KB ID                                                  | grp-abc123                                                          |
| `depth`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Processing depth (-1 for unlimited, 0 for direct records only)      |                                                                     |
| `force`                                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Force reindexing even if already indexed                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ReindexRecordGroupResponse](../../models/reindexrecordgroupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_stats

Retrieve statistics for a specific connector including record counts, indexing status breakdown, and sync information.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorStats" method="get" path="/knowledgeBase/stats/{connectorId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector.get_stats(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector ID                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorStats](../../models/connectorstats.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |