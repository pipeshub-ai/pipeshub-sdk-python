# MetricsCollection

## Overview

### Available Operations

* [get_config](#get_config) - Get metrics collection configuration
* [toggle](#toggle) - Enable or disable metrics collection
* [set_push_interval](#set_push_interval) - Configure metrics push interval
* [set_server_url](#set_server_url) - Configure metrics server URL

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.get_config()

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.toggle(enable_metric_collection=False)

    # Handle response
    print(res)

```
### Example Usage: enable

<!-- UsageSnippet language="python" operationID="toggleMetricsCollection" method="put" path="/configurationManager/metricsCollection/toggle" example="enable" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.toggle(enable_metric_collection=True)

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

Set how frequently collected metrics are pushed to the remote server.

**Interval Guidelines:**
- Minimum: 1000ms (1 second) - for real-time monitoring
- Recommended: 60000ms (1 minute) - balanced performance
- Maximum: No hard limit, but longer intervals may delay insights

**Performance Considerations:**
- Shorter intervals provide more real-time data but increase network traffic
- Longer intervals reduce overhead but delay metric visibility
- Changes take effect on the next push cycle

**Admin Access Required:** This endpoint requires administrator privileges.


### Example Usage: default

<!-- UsageSnippet language="python" operationID="setMetricsPushInterval" method="patch" path="/configurationManager/metricsCollection/pushInterval" example="default" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.set_push_interval(push_interval_ms=60000)

    # Handle response
    print(res)

```
### Example Usage: lowFrequency

<!-- UsageSnippet language="python" operationID="setMetricsPushInterval" method="patch" path="/configurationManager/metricsCollection/pushInterval" example="lowFrequency" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.set_push_interval(push_interval_ms=300000)

    # Handle response
    print(res)

```
### Example Usage: realtime

<!-- UsageSnippet language="python" operationID="setMetricsPushInterval" method="patch" path="/configurationManager/metricsCollection/pushInterval" example="realtime" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.set_push_interval(push_interval_ms=10000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `push_interval_ms`                                                  | *int*                                                               | :heavy_check_mark:                                                  | Push interval in milliseconds (minimum 1000ms)                      | 60000                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsPushIntervalResponse](../../models/setmetricspushintervalresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_server_url

Set the remote server URL where metrics will be pushed.

**Use Cases:**
- Self-hosted analytics: Point to your own Prometheus-compatible endpoint
- Custom monitoring: Integrate with your organization's monitoring stack
- Development: Use a local endpoint for testing

**URL Requirements:**
- Must be a valid URL (http or https)
- Server must accept POST requests with JSON payload
- Server should return 2xx status for successful pushes

**Admin Access Required:** This endpoint requires administrator privileges.


### Example Usage: localDev

<!-- UsageSnippet language="python" operationID="setMetricsServerUrl" method="patch" path="/configurationManager/metricsCollection/serverUrl" example="localDev" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.set_server_url(server_url_="http://localhost:9090/metrics")

    # Handle response
    print(res)

```
### Example Usage: selfHosted

<!-- UsageSnippet language="python" operationID="setMetricsServerUrl" method="patch" path="/configurationManager/metricsCollection/serverUrl" example="selfHosted" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.metrics_collection.set_server_url(server_url_="https://metrics.mycompany.com/collect")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_url`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Full URL of the metrics collection server                           | https://metrics.mycompany.com/collect                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsServerURLResponse](../../models/setmetricsserverurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |