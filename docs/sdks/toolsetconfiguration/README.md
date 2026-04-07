# ToolsetConfiguration

## Overview

Configure authentication and settings for toolset instances

### Available Operations

* [get_toolset_config](#get_toolset_config) - Get toolset configuration
* [~~save_toolset_config~~](#save_toolset_config) - Save toolset configuration :warning: **Deprecated**
* [update_toolset_config](#update_toolset_config) - Update toolset configuration
* [delete_toolset_config](#delete_toolset_config) - Delete toolset configuration

## get_toolset_config

Get configuration for a specific toolset instance

### Example Usage

<!-- UsageSnippet language="python" operationID="getToolsetConfig" method="get" path="/toolsets/{toolsetId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.toolset_configuration.get_toolset_config(toolset_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~save_toolset_config~~

Save or update toolset configuration (deprecated - use PUT)

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="saveToolsetConfig" method="post" path="/toolsets/{toolsetId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.toolset_configuration.save_toolset_config(toolset_id="<id>", auth={})

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `toolset_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `auth`                                                                | [models.SaveToolsetConfigAuth](../../models/savetoolsetconfigauth.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `base_url`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_toolset_config

Update toolset configuration

### Example Usage

<!-- UsageSnippet language="python" operationID="updateToolsetConfig" method="put" path="/toolsets/{toolsetId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.toolset_configuration.update_toolset_config(toolset_id="<id>", auth={})

    # Use the SDK ...

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `toolset_id`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `auth`                                                                    | [models.UpdateToolsetConfigAuth](../../models/updatetoolsetconfigauth.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `base_url`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_toolset_config

Delete a toolset instance and its configuration

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteToolsetConfig" method="delete" path="/toolsets/{toolsetId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.toolset_configuration.delete_toolset_config(toolset_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |