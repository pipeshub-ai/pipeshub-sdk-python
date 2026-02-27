# ToolsetInstances

## Overview

Create, manage, and configure toolset instances for your organization

### Available Operations

* [create_toolset](#create_toolset) - Create toolset instance
* [list_configured_toolsets](#list_configured_toolsets) - List configured toolsets
* [check_toolset_status](#check_toolset_status) - Check toolset status

## create_toolset

Create a new toolset instance with authentication configuration


### Example Usage

<!-- UsageSnippet language="python" operationID="createToolset" method="post" path="/toolsets" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as p_client:

    p_client.toolset_instances.create_toolset(name="<value>", auth={
        "type": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `auth`                                                              | [models.CreateToolsetAuth](../../models/createtoolsetauth.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_configured_toolsets

Get all configured toolsets for the authenticated user


### Example Usage

<!-- UsageSnippet language="python" operationID="listConfiguredToolsets" method="get" path="/toolsets/configured" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as p_client:

    res = p_client.toolset_instances.list_configured_toolsets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListConfiguredToolsetsResponse](../../models/listconfiguredtoolsetsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## check_toolset_status

Check authentication status of a toolset instance

### Example Usage

<!-- UsageSnippet language="python" operationID="checkToolsetStatus" method="get" path="/toolsets/{toolsetId}/status" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as p_client:

    p_client.toolset_instances.check_toolset_status(toolset_id="<id>")

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