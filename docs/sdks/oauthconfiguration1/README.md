# OAuthConfiguration

## Overview

Admin management of OAuth credentials for connector types

### Available Operations

* [list_toolset_o_auth_configs](#list_toolset_o_auth_configs) - List OAuth configs by toolset type
* [update_toolset_o_auth_config](#update_toolset_o_auth_config) - Update OAuth config
* [delete_toolset_o_auth_config](#delete_toolset_o_auth_config) - Delete OAuth config

## list_toolset_o_auth_configs

List OAuth configs by toolset type

### Example Usage

<!-- UsageSnippet language="python" operationID="listToolsetOAuthConfigs" method="get" path="/toolsets/oauth-configs/{toolsetType}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.o_auth_configuration.list_toolset_o_auth_configs(toolset_type="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_type`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_toolset_o_auth_config

Update OAuth config

### Example Usage

<!-- UsageSnippet language="python" operationID="updateToolsetOAuthConfig" method="put" path="/toolsets/oauth-configs/{toolsetType}/{oauthConfigId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.o_auth_configuration.update_toolset_o_auth_config(toolset_type="<value>", oauth_config_id="<id>", body={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_type`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `oauth_config_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `body`                                                              | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_toolset_o_auth_config

Delete OAuth config

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteToolsetOAuthConfig" method="delete" path="/toolsets/oauth-configs/{toolsetType}/{oauthConfigId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.o_auth_configuration.delete_toolset_o_auth_config(toolset_type="<value>", oauth_config_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_type`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `oauth_config_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |