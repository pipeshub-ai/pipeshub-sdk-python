# MetricsCollection

## Overview

### Available Operations

* [get_config](#get_config) - Get metrics collection configuration
* [toggle](#toggle) - Enable or disable metrics collection
* [set_push_interval](#set_push_interval) - Set metrics push interval
* [set_server_url](#set_server_url) - Set metrics remote server URL

## get_config

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

    res = pipeshub.metrics_collection.get_config()

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

## toggle

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

    res = pipeshub.metrics_collection.toggle(enable_metric_collection=False)

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

    res = pipeshub.metrics_collection.toggle(enable_metric_collection=True)

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

## set_push_interval

Configure the interval for pushing metrics to the collection server.


### Example Usage

<!-- UsageSnippet language="python" operationID="setMetricsCollectionPushInterval" method="patch" path="/configurationManager/metricsCollection/pushInterval" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.metrics_collection.set_push_interval(push_interval_ms=60000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `push_interval_ms`                                                  | *float*                                                             | :heavy_check_mark:                                                  | Push interval in milliseconds                                       | 60000                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsCollectionPushIntervalResponse](../../models/setmetricscollectionpushintervalresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_server_url

Configure the remote server URL for metrics collection.


### Example Usage

<!-- UsageSnippet language="python" operationID="setMetricsCollectionRemoteServer" method="patch" path="/configurationManager/metricsCollection/serverUrl" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.metrics_collection.set_server_url(server_url_="https://metrics-collector.example.com/collect-metrics")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_url`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | https://metrics-collector.example.com/collect-metrics               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsCollectionRemoteServerResponse](../../models/setmetricscollectionremoteserverresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |