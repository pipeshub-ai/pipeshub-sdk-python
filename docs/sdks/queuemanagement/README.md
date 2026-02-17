# QueueManagement

## Overview

### Available Operations

* [get_stats](#get_stats) - Get queue statistics

## get_stats

Retrieve aggregate statistics about the crawling job queue.<br><br>

<b>Overview:</b><br>
Returns real-time statistics about the BullMQ queue including job counts by state,
paused jobs, and repeatable job configurations. Useful for monitoring system health
and capacity planning.<br><br>

<b>Statistics Included:</b><br>
<ul>
<li><b>waiting:</b> Jobs queued and waiting to be processed</li>
<li><b>active:</b> Jobs currently being processed by workers</li>
<li><b>completed:</b> Successfully completed jobs (limited retention)</li>
<li><b>failed:</b> Failed jobs (limited retention)</li>
<li><b>delayed:</b> Jobs scheduled for future execution</li>
<li><b>paused:</b> Manually paused jobs</li>
<li><b>repeatable:</b> Number of repeatable job configurations</li>
<li><b>total:</b> Sum of all job counts</li>
</ul>

<b>Use Cases:</b><br>
<ul>
<li>Monitor queue health and throughput</li>
<li>Identify processing bottlenecks</li>
<li>Track failed job counts for alerting</li>
<li>Capacity planning based on queue depth</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getQueueStats" method="get" path="/crawlingManager/stats" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.queue_management.get_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetQueueStatsResponse](../../models/getqueuestatsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |