# MailConfigurations

## Overview

### Available Operations

* [reload_smtp](#reload_smtp) - Reload SMTP configuration

## reload_smtp

Dynamically reload the SMTP configuration from the application config file without restarting the service.<br><br>

<b>Overview:</b><br>
This internal endpoint allows the mail service to pick up SMTP configuration changes at runtime.
When SMTP settings are updated via <code>/configurationManager/smtpConfig</code>, this endpoint
should be called to apply the changes to the running mail service.<br><br>

<b>Authentication:</b><br>
Requires a scoped token with <code>fetch:config</code> scope. This endpoint is designed for
internal service communication only.<br><br>

<b>How It Works:</b><br>
<ol>
<li>Reads the latest configuration from the config file/etcd</li>
<li>Rebinds the AppConfig in the dependency injection container</li>
<li>Creates a new MailController instance with updated config</li>
<li>Returns the new SMTP configuration (excluding password)</li>
</ol>

<b>Use Cases:</b><br>
<ul>
<li>Apply SMTP configuration changes without service restart</li>
<li>Switch SMTP providers at runtime</li>
<li>Update SMTP credentials</li>
<li>Change sender email address</li>
</ul>

<b>Related Endpoints:</b><br>
<ul>
<li><code>POST /configurationManager/smtpConfig</code> - Create/update SMTP configuration</li>
<li><code>GET /configurationManager/smtpConfig</code> - Get current SMTP configuration</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateSmtpConfig" method="post" path="/mail/updateSmtpConfig" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.mail_configurations.reload_smtp(security=models.UpdateSMTPConfigSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `security`                                                           | [models.UpdateSMTPConfigSecurity](../../updatesmtpconfigsecurity.md) | :heavy_check_mark:                                                   | The security requirements to use for the request.                    |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.UpdateSMTPConfigResponse](../../models/updatesmtpconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |