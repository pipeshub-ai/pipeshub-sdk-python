# ConnectorService

## Overview

### Available Operations

* [health_check](#health_check) - [Connector Service] Health check
* [google_drive_webhook](#google_drive_webhook) - [Connector Service] Google Drive webhook
* [get_internal_stream_record](#get_internal_stream_record) - [Connector Service] Internal stream record
* [convert_record_buffer](#convert_record_buffer) - [Connector Service] Convert record buffer
* [get_stats](#get_stats) - [Connector Service] Get connector statistics
* [reindex_failed_records](#reindex_failed_records) - [Connector Service] Reindex all failed records
* [get_signed_url](#get_signed_url) - [Connector Service] Get signed URL for record

## health_check

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Health check endpoint for the Connector Service (Python FastAPI).<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> None required for health check<br><br>

<b>Note:</b> This is the core internal service that manages all
data source connectors and OAuth flows.


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorServiceHealth" method="get" path="/connector/health" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.health_check()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.ConnectorServiceHealthResponse](../../models/connectorservicehealthresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## google_drive_webhook

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Webhook endpoint for Google Drive push notifications.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> None required - uses Google's push notification verification<br><br>

<b>Note:</b> This endpoint receives real-time change notifications from
Google Drive when files are created, modified, or deleted.


### Example Usage

<!-- UsageSnippet language="python" operationID="driveWebhook" method="post" path="/connector/drive/webhook" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.connector_service.google_drive_webhook()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_internal_stream_record

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Internal endpoint for streaming record content (service-to-service).<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Requires scoped service token<br><br>

<b>Use Case:</b> Used by Indexing Service to fetch file content for processing.


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorInternalStreamRecord" method="get" path="/connector/api/v1/internal/stream/record/{record_id}" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.get_internal_stream_record(security=models.ConnectorInternalStreamRecordSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.ConnectorInternalStreamRecordSecurity](../../models/connectorinternalstreamrecordsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `record_id`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Record ID to stream                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |
| `server_url`                                                                                          | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | An optional server URL to use.                                                                        |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## convert_record_buffer

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Convert a record buffer to a different format.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Requires scoped service token<br><br>

<b>Supported Conversions:</b> PDF to text, DOCX to text, etc.


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorConvertRecordBuffer" method="post" path="/connector/api/v1/record/buffer/convert" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.convert_record_buffer(security=models.ConnectorConvertRecordBufferSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), buffer="<value>", convert_to="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ConnectorConvertRecordBufferSecurity](../../models/connectorconvertrecordbuffersecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `buffer`                                                                                            | *str*                                                                                               | :heavy_check_mark:                                                                                  | Base64 encoded file content                                                                         |
| `convert_to`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | Target format (e.g., 'text', 'markdown')                                                            |
| `mime_type`                                                                                         | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Original MIME type of the file                                                                      |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |
| `server_url`                                                                                        | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | An optional server URL to use.                                                                      |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_stats

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Get statistics for a specific connector.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Requires scoped service token


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorGetStats" method="get" path="/connector/api/v1/stats" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.get_stats(security=models.ConnectorGetStatsSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), org_id="<id>", connector="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.ConnectorGetStatsSecurity](../../models/connectorgetstatssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `org_id`                                                                      | *str*                                                                         | :heavy_check_mark:                                                            | Organization ID                                                               |
| `connector`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | Connector name (e.g., GOOGLE_DRIVE, ONEDRIVE)                                 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |
| `server_url`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | An optional server URL to use.                                                |

### Response

**[models.ConnectorGetStatsResponse](../../models/connectorgetstatsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## reindex_failed_records

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Trigger reindexing of all failed records for a specific connector.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Requires scoped service token


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorReindexFailedRecords" method="post" path="/connector/api/v1/records/reindex-failed" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.reindex_failed_records(security=models.ConnectorReindexFailedRecordsSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.ConnectorReindexFailedRecordsSecurity](../../models/connectorreindexfailedrecordssecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `connector`                                                                                           | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Connector name to reindex failed records for                                                          |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |
| `server_url`                                                                                          | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | An optional server URL to use.                                                                        |

### Response

**[models.ConnectorReindexFailedRecordsResponse](../../models/connectorreindexfailedrecordsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_signed_url

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Get a signed URL for direct file access from the connector source.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Requires scoped service token<br><br>

<b>Use Case:</b> Generate temporary signed URLs for file downloads from
Google Drive, OneDrive, SharePoint, etc.


### Example Usage

<!-- UsageSnippet language="python" operationID="connectorGetSignedUrl" method="get" path="/connector/api/v1/{org_id}/{user_id}/{connector}/record/{record_id}/signedUrl" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.connector_service.get_signed_url(security=models.ConnectorGetSignedURLSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), org_id="<id>", user_id="<id>", connector="<value>", record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.ConnectorGetSignedURLSecurity](../../models/connectorgetsignedurlsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `org_id`                                                                              | *str*                                                                                 | :heavy_check_mark:                                                                    | Organization ID                                                                       |
| `user_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | User ID                                                                               |
| `connector`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | Connector name                                                                        |
| `record_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | Record ID                                                                             |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        |

### Response

**[models.ConnectorGetSignedURLResponse](../../models/connectorgetsignedurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |