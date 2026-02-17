# IndexingServices

## Overview

### Available Operations

* [get_health](#get_health) - [Indexing Service] Health check

## get_health

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Health check endpoint for the Indexing Service (Python FastAPI).<br><br>

<b>Service:</b> Indexing Service<br>
<b>Port:</b> 8091<br>
<b>Base URL:</b> <code>http://localhost:8091</code><br><br>

<b>Authentication:</b> None required for health check<br><br>

<b>Note:</b> This is an internal service. It processes Kafka messages
for document indexing and does not expose user-facing endpoints.
Health check also verifies Connector Service connectivity.


### Example Usage

<!-- UsageSnippet language="python" operationID="indexingServiceHealth" method="get" path="/indexing/health" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.indexing_services.get_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.IndexingServiceHealthResponse](../../models/indexingservicehealthresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |