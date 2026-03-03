# StorageConfiguration

## Overview

Configure storage backend for file uploads and documents. Supports AWS S3, Azure Blob Storage, or local filesystem.

### Available Operations

* [get_storage_config](#get_storage_config) - Get current storage configuration

## get_storage_config

Retrieve the current storage backend configuration. Returns the configuration for whichever storage type is currently active (Local, S3, or Azure Blob).

### Example Usage

<!-- UsageSnippet language="python" operationID="getStorageConfig" method="get" path="/configurationManager/storageConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.storage_configuration.get_storage_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageConfigResponse](../../models/getstorageconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |