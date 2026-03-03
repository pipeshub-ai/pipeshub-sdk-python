# PlatformSettings

## Overview

Platform-wide settings including file upload limits, feature flags, and custom system prompts.

### Available Operations

* [set_platform_settings](#set_platform_settings) - Update platform settings
* [get_platform_settings](#get_platform_settings) - Get platform settings
* [get_available_feature_flags](#get_available_feature_flags) - Get available feature flags
* [set_custom_system_prompt](#set_custom_system_prompt) - Update custom system prompt
* [get_custom_system_prompt](#get_custom_system_prompt) - Get custom system prompt

## set_platform_settings

Configure platform-wide settings including file upload limits and feature flags.

**File Upload Limits:**
- Default: 30MB (31457280 bytes)
- Maximum: 1GB (1073741824 bytes)

**Available Feature Flags:**
- ENABLE_BETA_CONNECTORS: Enable beta connector integrations (default: false)


### Example Usage: default30MB

<!-- UsageSnippet language="python" operationID="setPlatformSettings" method="post" path="/configurationManager/platform/settings" example="default30MB" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.platform_settings.set_platform_settings(file_upload_max_size_bytes=31457280, feature_flags={
        "ENABLE_BETA_CONNECTORS": False,
    })

    # Use the SDK ...

```
### Example Usage: enableBetaFeatures

<!-- UsageSnippet language="python" operationID="setPlatformSettings" method="post" path="/configurationManager/platform/settings" example="enableBetaFeatures" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.platform_settings.set_platform_settings(file_upload_max_size_bytes=31457280, feature_flags={
        "ENABLE_BETA_CONNECTORS": True,
    })

    # Use the SDK ...

```
### Example Usage: increased100MB

<!-- UsageSnippet language="python" operationID="setPlatformSettings" method="post" path="/configurationManager/platform/settings" example="increased100MB" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.platform_settings.set_platform_settings(file_upload_max_size_bytes=104857600, feature_flags={
        "ENABLE_BETA_CONNECTORS": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `file_upload_max_size_bytes`                                             | *int*                                                                    | :heavy_check_mark:                                                       | Maximum file upload size in bytes                                        | 31457280                                                                 |
| `feature_flags`                                                          | Dict[str, *bool*]                                                        | :heavy_check_mark:                                                       | Key-value map of feature flags. Set to true to enable, false to disable. | {<br/>"ENABLE_BETA_CONNECTORS": false<br/>}                              |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |                                                                          |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_platform_settings

Retrieve current platform settings including file upload limits and feature flag states.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlatformSettings" method="get" path="/configurationManager/platform/settings" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.platform_settings.get_platform_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformSettings](../../models/platformsettings.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_available_feature_flags

List all available feature flags with their descriptions and default values.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAvailableFeatureFlags" method="get" path="/configurationManager/platform/feature-flags/available" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.platform_settings.get_available_feature_flags()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAvailableFeatureFlagsResponse](../../models/getavailablefeatureflagsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_custom_system_prompt

Set a custom system prompt that will be used by AI models.

### Example Usage

<!-- UsageSnippet language="python" operationID="setCustomSystemPrompt" method="put" path="/configurationManager/prompts/system" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.platform_settings.set_custom_system_prompt()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_system_prompt`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Custom system prompt text for AI models                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_custom_system_prompt

Get custom system prompt.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCustomSystemPrompt" method="get" path="/configurationManager/prompts/system" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.platform_settings.get_custom_system_prompt()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomSystemPrompt](../../models/customsystemprompt.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |