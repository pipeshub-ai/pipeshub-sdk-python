# Connector

## Overview

Connector-related operations

### Available Operations

* [reindex_record](#reindex_record) - Reindex single record
* [reindex_record_group](#reindex_record_group) - Reindex record group
* [reindex_failed_records](#reindex_failed_records) - Reindex failed connector records
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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector.reindex_record(record_id="<id>", depth=-1)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `depth`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Processing depth (-1 for unlimited)                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector.reindex_record_group(record_group_id="<id>", depth=-1)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_group_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Folder ID or KB ID                                                  |
| `depth`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_failed_records

Retry indexing for all failed records from a specific connector.<br><br>
<b>Use Case:</b><br>
After fixing connectivity issues or configuration problems, use this to reprocess all records that failed during the initial sync.


### Example Usage

<!-- UsageSnippet language="python" operationID="reindexFailedConnectorRecords" method="post" path="/knowledgeBase/reindex-failed/connector" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.connector.reindex_failed_records(app="GOOGLE_DRIVE", connector_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `app`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Connector app name                                                  | GOOGLE_DRIVE                                                        |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector.get_stats(connector_id="<id>")

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