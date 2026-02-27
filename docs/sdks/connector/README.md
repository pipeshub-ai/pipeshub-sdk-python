# Connector

## Overview

Connector-related operations

### Available Operations

* [reindex_record](#reindex_record) - Reindex single record
* [reindex_record_group](#reindex_record_group) - Reindex record group
* [resync_connector](#resync_connector) - Resync connector
* [get_connector_stats](#get_connector_stats) - Get connector statistics

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.connector.reindex_record(security=models.ReindexRecordSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), record_id="<id>", depth=-1)

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.ReindexRecordSecurity](../../models/reindexrecordsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `record_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `depth`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Processing depth (-1 for unlimited)                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.connector.reindex_record_group(security=models.ReindexRecordGroupSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), record_group_id="<id>", depth=-1)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.ReindexRecordGroupSecurity](../../models/reindexrecordgroupsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `record_group_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | Folder ID or KB ID                                                              |
| `depth`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## resync_connector

Trigger a full resync of all records from a connector.<br><br>
<b>Overview:</b><br>
Fetches all content from the external source and updates local records. Use when you suspect data is out of sync.<br><br>
<b>Warning:</b> This can be resource-intensive for large connectors.


### Example Usage

<!-- UsageSnippet language="python" operationID="resyncConnector" method="post" path="/knowledgeBase/resync/connector" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.connector.resync_connector(security=models.ResyncConnectorSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector_name="GOOGLE_DRIVE", connector_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.ResyncConnectorSecurity](../../models/resyncconnectorsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `connector_name`                                                          | *str*                                                                     | :heavy_check_mark:                                                        | Connector type name                                                       | GOOGLE_DRIVE                                                              |
| `connector_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | Connector instance ID                                                     |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_stats

Retrieve statistics for a specific connector including record counts, indexing status breakdown, and sync information.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorStats" method="get" path="/knowledgeBase/stats/{connectorId}" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector.get_connector_stats(security=models.GetConnectorStatsSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.GetConnectorStatsSecurity](../../models/getconnectorstatssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `connector_id`                                                                | *str*                                                                         | :heavy_check_mark:                                                            | Connector ID                                                                  |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ConnectorStats](../../models/connectorstats.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |