# SmtpConfigurations

## Overview

### Available Operations

* [create_or_update](#create_or_update) - Create or update SMTP configuration

## create_or_update

Configure SMTP email server for sending system emails including user invitations, notifications, and password resets.

Common SMTP providers and their settings:
- Gmail: host=smtp.gmail.com, port=587 (requires App Password)
- SendGrid: host=smtp.sendgrid.net, port=587
- Amazon SES: host=email-smtp.{region}.amazonaws.com, port=587
- Microsoft 365: host=smtp.office365.com, port=587

Configuration is encrypted before storage.


### Example Usage: amazonSes

<!-- UsageSnippet language="python" operationID="createSMTPConfig" method="post" path="/configurationManager/smtpConfig" example="amazonSes" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.smtp_configurations.create_or_update(host="email-smtp.us-east-1.amazonaws.com", port=587, username="AKIAIOSFODNN7EXAMPLE", password="your-ses-smtp-password", from_email="noreply@yourcompany.com")

    # Use the SDK ...

```
### Example Usage: gmail

<!-- UsageSnippet language="python" operationID="createSMTPConfig" method="post" path="/configurationManager/smtpConfig" example="gmail" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.smtp_configurations.create_or_update(host="smtp.gmail.com", port=587, username="notifications@yourcompany.com", password="your-app-password", from_email="noreply@yourcompany.com")

    # Use the SDK ...

```
### Example Usage: office365

<!-- UsageSnippet language="python" operationID="createSMTPConfig" method="post" path="/configurationManager/smtpConfig" example="office365" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.smtp_configurations.create_or_update(host="smtp.office365.com", port=587, username="notifications@yourcompany.onmicrosoft.com", password="your-password", from_email="notifications@yourcompany.onmicrosoft.com")

    # Use the SDK ...

```
### Example Usage: sendgrid

<!-- UsageSnippet language="python" operationID="createSMTPConfig" method="post" path="/configurationManager/smtpConfig" example="sendgrid" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.smtp_configurations.create_or_update(host="smtp.sendgrid.net", port=587, username="apikey", password="SG.your-sendgrid-api-key", from_email="noreply@yourcompany.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             | Example                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `host`                                                                                                                  | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | SMTP server hostname or IP address                                                                                      | smtp.gmail.com                                                                                                          |
| `port`                                                                                                                  | *Optional[int]*                                                                                                         | :heavy_minus_sign:                                                                                                      | SMTP server port. Common ports are 25 (unencrypted), 465 (SSL), 587 (TLS/STARTTLS)                                      | 587                                                                                                                     |
| `username`                                                                                                              | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | SMTP authentication username. Usually an email address for services like Gmail, SendGrid, etc.                          | notifications@yourcompany.com                                                                                           |
| `password`                                                                                                              | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | SMTP authentication password or app-specific password. For Gmail, use an App Password instead of your account password. | your-app-password                                                                                                       |
| `from_email`                                                                                                            | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | Default sender email address that appears in the "From" field of outgoing emails                                        | noreply@yourcompany.com                                                                                                 |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |                                                                                                                         |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |