# CrawlingJobs

## Overview

### Available Operations

* [schedule](#schedule) - Schedule a crawling job
* [get_status](#get_status) - Get crawling job status
* [remove](#remove) - Remove a crawling job
* [pause](#pause) - Pause a crawling job
* [resume](#resume) - Resume a paused crawling job
* [list_all_statuses](#list_all_statuses) - Get all crawling job statuses
* [remove_all](#remove_all) - Remove all crawling jobs

## schedule

Schedule a new crawling job for a specific connector instance.<br><br>

<b>Overview:</b><br>
Creates a scheduled crawling job that will sync data from the specified connector into
PipesHub's search index. The job is added to a BullMQ queue and will execute according
to the specified schedule configuration.<br><br>

<b>Schedule Types:</b><br>
<ul>
<li><b>hourly:</b> Run every X hours at specified minute (e.g., every 2 hours at :30)</li>
<li><b>daily:</b> Run once per day at specified time (e.g., 2:00 AM daily)</li>
<li><b>weekly:</b> Run on specific days of the week (e.g., Mon/Wed/Fri at 3:00 AM)</li>
<li><b>monthly:</b> Run on specific day of month (e.g., 1st of each month at 4:00 AM)</li>
<li><b>custom:</b> Use cron expression for complex schedules</li>
<li><b>once:</b> Run once at a specific future datetime</li>
</ul>

<b>Access Control:</b><br>
<ul>
<li>Team-scoped connectors: Requires admin privileges</li>
<li>Personal-scoped connectors: Only the creator can schedule jobs</li>
</ul>

<b>Job Behavior:</b><br>
<ul>
<li>If a job already exists for this connector, it will be replaced</li>
<li>Disabled schedules (<code>isEnabled: false</code>) will throw an error</li>
<li>Jobs use exponential backoff for retries (5s, 10s, 20s, etc.)</li>
<li>Only last 10 completed/failed jobs are retained per connector</li>
</ul>

<b>Related Endpoints:</b><br>
<ul>
<li><code>GET /crawlingManager/{connector}/{connectorId}/schedule</code> - Get job status</li>
<li><code>POST /crawlingManager/{connector}/{connectorId}/pause</code> - Pause job</li>
<li><code>DELETE /crawlingManager/{connector}/{connectorId}/remove</code> - Remove job</li>
</ul>


### Example Usage: customCron

<!-- UsageSnippet language="python" operationID="scheduleCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/schedule" example="customCron" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.schedule(connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
        "schedule_type": "custom",
        "is_enabled": True,
        "timezone": "UTC",
        "cron_expression": "0 */6 * * *",
        "description": "Every 6 hours",
    }, priority=5, max_retries=3, timeout=300000)

    # Handle response
    print(res)

```
### Example Usage: dailySync

<!-- UsageSnippet language="python" operationID="scheduleCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/schedule" example="dailySync" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.schedule(connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
        "schedule_type": "daily",
        "is_enabled": True,
        "timezone": "UTC",
        "hour": 2,
        "minute": 0,
    }, priority=5, max_retries=3, timeout=300000)

    # Handle response
    print(res)

```
### Example Usage: hourlySync

<!-- UsageSnippet language="python" operationID="scheduleCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/schedule" example="hourlySync" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.schedule(connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
        "schedule_type": "hourly",
        "is_enabled": True,
        "timezone": "America/New_York",
        "minute": 30,
        "interval": 4,
    }, priority=3, max_retries=5, timeout=300000)

    # Handle response
    print(res)

```
### Example Usage: oneTimeSync

<!-- UsageSnippet language="python" operationID="scheduleCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/schedule" example="oneTimeSync" -->
```python
import os
from pipeshub import Pipeshub
from pipeshub.utils import parse_datetime


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.schedule(connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
        "schedule_type": "once",
        "is_enabled": True,
        "timezone": "UTC",
        "scheduled_time": parse_datetime("2024-12-25T10:00:00Z"),
    }, priority=1, max_retries=3, timeout=300000)

    # Handle response
    print(res)

```
### Example Usage: weeklySync

<!-- UsageSnippet language="python" operationID="scheduleCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/schedule" example="weeklySync" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.schedule(connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
        "schedule_type": "weekly",
        "is_enabled": True,
        "timezone": "Europe/London",
        "days_of_week": [
            1,
            3,
            5,
        ],
        "hour": 3,
        "minute": 0,
    }, priority=5, max_retries=3, timeout=300000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Connector type identifier (e.g., "drive", "onedrive", "slack", "jira")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | drive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `connector_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Unique identifier of the connector instance (MongoDB ObjectId)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 507f1f77bcf86cd799439011                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `schedule_config`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [models.ScheduleConfig](../../models/scheduleconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schedule configuration for crawling jobs. The structure varies based on <code>scheduleType</code>.<br><br><br/><b>Schedule Type Configurations:</b><br><br/><ul><br/><li><b>hourly:</b> <code>minute</code>, <code>interval</code> (optional)</li><br/><li><b>daily:</b> <code>hour</code>, <code>minute</code></li><br/><li><b>weekly:</b> <code>daysOfWeek</code>, <code>hour</code>, <code>minute</code></li><br/><li><b>monthly:</b> <code>dayOfMonth</code>, <code>hour</code>, <code>minute</code></li><br/><li><b>custom:</b> <code>cronExpression</code>, <code>description</code> (optional)</li><br/><li><b>once:</b> <code>scheduledTime</code></li><br/></ul><br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `priority`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Job priority (1=highest, 10=lowest). Higher priority jobs are processed first.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `max_retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Maximum number of retry attempts on failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `timeout`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Job timeout in milliseconds (default 5 minutes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ScheduleCrawlingJobResponse](../../models/schedulecrawlingjobresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_status

Retrieve the current status of a scheduled crawling job for a specific connector.<br><br>

<b>Overview:</b><br>
Returns detailed information about the most recent crawling job for the specified connector,
including its current state, progress, timing information, and any error details.<br><br>

<b>Job States:</b><br>
<ul>
<li><b>waiting:</b> Job is queued and waiting to be processed</li>
<li><b>active:</b> Job is currently being processed by a worker</li>
<li><b>completed:</b> Job finished successfully</li>
<li><b>failed:</b> Job failed after exhausting retry attempts</li>
<li><b>delayed:</b> Job is scheduled for future execution</li>
<li><b>paused:</b> Job has been manually paused</li>
</ul>

<b>Access Control:</b><br>
Same as scheduling - team connectors require admin, personal connectors require creator.


### Example Usage

<!-- UsageSnippet language="python" operationID="getCrawlingJobStatus" method="get" path="/crawlingManager/{connector}/{connectorId}/schedule" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.get_status(connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Connector type identifier                                           | drive                                                               |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the connector instance                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCrawlingJobStatusResponse](../../models/getcrawlingjobstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove

Permanently remove a scheduled crawling job for a specific connector.<br><br>

<b>Overview:</b><br>
Removes the crawling job and all associated data from the queue. This includes
removing repeatable job configurations and cleaning up job history.<br><br>

<b>What Gets Removed:</b><br>
<ul>
<li>Active or waiting job instances</li>
<li>Repeatable job configuration (for recurring schedules)</li>
<li>Paused job information</li>
<li>Job mappings and metadata</li>
</ul>

<b>Note:</b> Completed and failed job records may be retained for audit purposes.

<b>Related Endpoints:</b><br>
<ul>
<li><code>DELETE /crawlingManager/schedule/all</code> - Remove all jobs for organization</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrawlingJob" method="delete" path="/crawlingManager/{connector}/{connectorId}/remove" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.remove(connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Connector type identifier                                           | drive                                                               |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the connector instance                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RemoveCrawlingJobResponse](../../models/removecrawlingjobresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## pause

Pause a running or scheduled crawling job without losing its configuration.<br><br>

<b>Overview:</b><br>
Pausing a job stores its complete configuration and removes it from the active queue.
The job can be resumed later with <code>POST /crawlingManager/{connector}/{connectorId}/resume</code>,
which will restore the exact same schedule configuration.<br><br>

<b>How Pausing Works:</b><br>
<ol>
<li>Current job configuration is stored in memory</li>
<li>Active/repeatable job is removed from BullMQ queue</li>
<li>Job state changes to "paused"</li>
<li>No new job executions will occur until resumed</li>
</ol>

<b>Use Cases:</b><br>
<ul>
<li>Temporarily stop crawling during maintenance</li>
<li>Pause data sync while investigating issues</li>
<li>Stop crawling for a connector being reconfigured</li>
</ul>

<b>Note:</b> If a job is currently active (processing), it will complete before pausing.


### Example Usage

<!-- UsageSnippet language="python" operationID="pauseCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/pause" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.pause(connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Connector type identifier                                           | drive                                                               |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the connector instance                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PauseCrawlingJobResponse](../../models/pausecrawlingjobresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## resume

Resume a previously paused crawling job using its stored configuration.<br><br>

<b>Overview:</b><br>
Restores a paused job to active state using the exact configuration it had when paused.
A new job is created in BullMQ with the same schedule settings.<br><br>

<b>How Resuming Works:</b><br>
<ol>
<li>Retrieve stored job configuration from pause state</li>
<li>Create new scheduled job with same configuration</li>
<li>Remove from paused jobs tracking</li>
<li>Job will execute according to its original schedule</li>
</ol>

<b>Note:</b> The job will resume according to its schedule, not immediately execute
(unless it's a one-time job that hasn't run yet).


### Example Usage

<!-- UsageSnippet language="python" operationID="resumeCrawlingJob" method="post" path="/crawlingManager/{connector}/{connectorId}/resume" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.resume(connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Connector type identifier                                           | drive                                                               |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the connector instance                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ResumeCrawlingJobResponse](../../models/resumecrawlingjobresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_all_statuses

Retrieve the status of all scheduled crawling jobs for the current organization.<br><br>

<b>Overview:</b><br>
Returns a list of all crawling jobs across all connectors for the authenticated user's
organization. This includes active, waiting, paused, completed, and failed jobs.<br><br>

<b>Response Details:</b><br>
<ul>
<li>Jobs are grouped by connector type</li>
<li>Last 10 jobs per connector type are returned</li>
<li>Includes both active queue jobs and paused jobs</li>
</ul>

<b>Use Cases:</b><br>
<ul>
<li>Dashboard overview of all crawling activities</li>
<li>Monitoring job health across connectors</li>
<li>Identifying failed or stuck jobs</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllCrawlingJobStatus" method="get" path="/crawlingManager/schedule/all" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.list_all_statuses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllCrawlingJobStatusResponse](../../models/getallcrawlingjobstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_all

Remove all scheduled crawling jobs for the current organization.<br><br>

<b>Overview:</b><br>
Bulk operation to remove all crawling jobs across all connectors for the organization.
This is useful when decommissioning an organization or doing a complete reset.<br><br>

<b>What Gets Removed:</b><br>
<ul>
<li>All active and waiting jobs</li>
<li>All repeatable job configurations</li>
<li>All paused jobs</li>
<li>All job mappings for the organization</li>
</ul>

<b>Warning:</b> This operation cannot be undone. All job configurations will need
to be recreated manually.


### Example Usage

<!-- UsageSnippet language="python" operationID="removeAllCrawlingJobs" method="delete" path="/crawlingManager/schedule/all" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.crawling_jobs.remove_all()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoveAllCrawlingJobsResponse](../../models/removeallcrawlingjobsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |