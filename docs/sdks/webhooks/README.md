# Webhooks

## Overview

Webhook handlers for real-time updates

### Available Operations

* [verify_gmail](#verify_gmail) - [Connector Service] Gmail webhook verification
* [gmail](#gmail) - [Connector Service] Gmail webhook
* [admin](#admin) - [Connector Service] Google Workspace Admin webhook

## verify_gmail

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

GET handler for Gmail Pub/Sub webhook verification.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> None required - uses Google Pub/Sub verification<br><br>

<b>Note:</b> Google Pub/Sub may send GET requests for subscription verification.


### Example Usage

<!-- UsageSnippet language="python" operationID="gmailWebhookVerify" method="get" path="/connector/gmail/webhook" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.webhooks.verify_gmail()

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

## gmail

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Webhook endpoint for Gmail Pub/Sub notifications.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> None required - uses Google Pub/Sub verification<br><br>

<b>Note:</b> This endpoint receives notifications when new emails arrive
or email labels change.


### Example Usage

<!-- UsageSnippet language="python" operationID="gmailWebhook" method="post" path="/connector/gmail/webhook" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.webhooks.gmail()

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

## admin

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Webhook endpoint for Google Workspace Admin push notifications.<br><br>

<b>Service:</b> Connector Service<br>
<b>Port:</b> 8088<br>
<b>Base URL:</b> <code>http://localhost:8088</code><br><br>

<b>Authentication:</b> Verified via Google Workspace webhook signature<br><br>

<b>Note:</b> This endpoint receives notifications about user and group
changes from Google Workspace Admin directory (e.g., user created,
deleted, suspended, group membership changes).


### Example Usage

<!-- UsageSnippet language="python" operationID="adminWebhook" method="post" path="/connector/admin/webhook" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.webhooks.admin()

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