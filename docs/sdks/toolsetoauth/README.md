# ToolsetOAuth

## Overview

OAuth 2.0 authorization flow for toolsets requiring user consent

### Available Operations

* [get_toolset_o_auth_url](#get_toolset_o_auth_url) - Get OAuth authorization URL
* [handle_toolset_o_auth_callback](#handle_toolset_o_auth_callback) - Handle OAuth callback
* [get_instance_o_auth_authorization_url](#get_instance_o_auth_authorization_url) - Get OAuth authorization URL for instance

## get_toolset_o_auth_url

Get OAuth authorization URL for a toolset.<br><br>
Returns a URL that the user should visit to authorize the toolset.


### Example Usage

<!-- UsageSnippet language="python" operationID="getToolsetOAuthUrl" method="get" path="/toolsets/{toolsetId}/oauth/authorize" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.toolset_o_auth.get_toolset_o_auth_url(toolset_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `toolset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetToolsetOAuthURLResponse](../../models/gettoolsetoauthurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## handle_toolset_o_auth_callback

Handle OAuth callback from the authorization server.<br><br>
This endpoint processes the authorization code and completes the OAuth flow.


### Example Usage

<!-- UsageSnippet language="python" operationID="handleToolsetOAuthCallback" method="get" path="/toolsets/oauth/callback" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.toolset_o_auth.handle_toolset_o_auth_callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `error`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HandleToolsetOAuthCallbackResponse](../../models/handletoolsetoauthcallbackresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_instance_o_auth_authorization_url

Get OAuth authorization URL for instance

### Example Usage

<!-- UsageSnippet language="python" operationID="getInstanceOAuthAuthorizationUrl" method="get" path="/toolsets/instances/{instanceId}/oauth/authorize" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.toolset_o_auth.get_instance_o_auth_authorization_url(instance_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `instance_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInstanceOAuthAuthorizationURLResponse](../../models/getinstanceoauthauthorizationurlresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |