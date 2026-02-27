# CrawlingJobs

## Overview

Endpoints for scheduling, managing, and monitoring data crawling jobs for enterprise connectors.

The Crawling Manager uses BullMQ (Redis-based queue) to schedule and execute crawling jobs that
sync data from external connectors (Google Drive, OneDrive, Slack, Jira, etc.) into PipesHub's
search index.

**Key Features:**
- Schedule recurring crawls (hourly, daily, weekly, monthly) or one-time crawls
- Pause and resume crawling jobs without losing configuration
- Priority-based job execution (1-10 scale)
- Automatic retry with exponential backoff on failures
- Per-connector job isolation and tracking

**Access Control:**
- Team-scoped connectors require admin privileges
- Personal-scoped connectors can only be managed by the creator
- All operations require valid JWT authentication

**Schedule Types:**
- `hourly`: Run every X hours at specified minute
- `daily`: Run once per day at specified time
- `weekly`: Run on specified days of the week
- `monthly`: Run on specified day of the month
- `custom`: Use cron expression for complex schedules
- `once`: Run once at a specific future time


### Available Operations

* [schedule_crawling_job](#schedule_crawling_job) - Schedule a crawling job
* [get_crawling_job_status](#get_crawling_job_status) - Get crawling job status
* [remove_crawling_job](#remove_crawling_job) - Remove a crawling job

## schedule_crawling_job

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.schedule_crawling_job(security=models.ScheduleCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.schedule_crawling_job(security=models.ScheduleCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.schedule_crawling_job(security=models.ScheduleCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
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
from pipeshub import Pipeshub, models
from pipeshub.utils import parse_datetime


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.schedule_crawling_job(security=models.ScheduleCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.schedule_crawling_job(security=models.ScheduleCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011", schedule_config={
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
| `security`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [models.ScheduleCrawlingJobSecurity](../../models/schedulecrawlingjobsecurity.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
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

## get_crawling_job_status

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.get_crawling_job_status(security=models.GetCrawlingJobStatusSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.GetCrawlingJobStatusSecurity](../../models/getcrawlingjobstatussecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `connector`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | Connector type identifier                                                           | drive                                                                               |
| `connector_id`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | Unique identifier of the connector instance                                         | 507f1f77bcf86cd799439011                                                            |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.GetCrawlingJobStatusResponse](../../models/getcrawlingjobstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_crawling_job

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.crawling_jobs.remove_crawling_job(security=models.RemoveCrawlingJobSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), connector="drive", connector_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.RemoveCrawlingJobSecurity](../../models/removecrawlingjobsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |                                                                               |
| `connector`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | Connector type identifier                                                     | drive                                                                         |
| `connector_id`                                                                | *str*                                                                         | :heavy_check_mark:                                                            | Unique identifier of the connector instance                                   | 507f1f77bcf86cd799439011                                                      |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.RemoveCrawlingJobResponse](../../models/removecrawlingjobresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |