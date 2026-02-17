# Uploads

## Overview

### Available Operations

* [get_limits](#get_limits) - Get upload limits

## get_limits

Retrieve current upload constraints for the organization.<br><br>
<b>Use Case:</b><br>
Call this before uploads to validate file sizes on the client side and display appropriate limits to users.


### Example Usage

<!-- UsageSnippet language="python" operationID="getUploadLimits" method="get" path="/knowledgeBase/limits" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.uploads.get_limits()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUploadLimitsResponse](../../models/getuploadlimitsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |