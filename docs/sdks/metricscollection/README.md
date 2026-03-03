# MetricsCollection

## Overview

Configure telemetry and metrics collection for application monitoring and analytics.

PipesHub collects anonymized usage metrics to help improve the product. Metrics are pushed
to a configurable remote server at regular intervals.

**Collected Metrics:**
- API request counts and response times
- User activity patterns (anonymized)
- Feature usage statistics
- Error rates and types

**Configuration Options:**
- Enable/disable metrics collection entirely
- Configure push interval (minimum 1 second, default 60 seconds)
- Set custom metrics server URL for self-hosted analytics

**Privacy:**
- All metrics are anonymized before collection
- No personally identifiable information (PII) is collected
- Organization can disable collection at any time


### Available Operations

* [get_metrics_collection](#get_metrics_collection) - Get metrics collection configuration
* [toggle_metrics_collection](#toggle_metrics_collection) - Enable or disable metrics collection

## get_metrics_collection

Retrieve the current metrics collection configuration including:
- Whether collection is enabled
- Push interval settings
- Server URL configuration
- Instance identification

**Admin Access Required:** This endpoint requires administrator privileges.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMetricsCollection" method="get" path="/configurationManager/metricsCollection" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.metrics_collection.get_metrics_collection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsCollectionConfig](../../models/metricscollectionconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## toggle_metrics_collection

Toggle the master switch for metrics collection.

**When Enabled:**
- Application metrics are collected in the background
- Metrics are pushed to the configured server at regular intervals
- Activity counters track API usage patterns

**When Disabled:**
- No metrics are collected or stored
- No data is sent to the metrics server
- Existing scheduled push jobs are stopped

**Admin Access Required:** This endpoint requires administrator privileges.


### Example Usage: disable

<!-- UsageSnippet language="python" operationID="toggleMetricsCollection" method="put" path="/configurationManager/metricsCollection/toggle" example="disable" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.metrics_collection.toggle_metrics_collection(enable_metric_collection=False)

    # Handle response
    print(res)

```
### Example Usage: enable

<!-- UsageSnippet language="python" operationID="toggleMetricsCollection" method="put" path="/configurationManager/metricsCollection/toggle" example="enable" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.metrics_collection.toggle_metrics_collection(enable_metric_collection=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enable_metric_collection`                                          | *bool*                                                              | :heavy_check_mark:                                                  | Set to true to enable metrics collection, false to disable          | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ToggleMetricsCollectionResponse](../../models/togglemetricscollectionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |