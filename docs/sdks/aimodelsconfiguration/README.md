# AiModelsConfiguration

## Overview

### Available Operations

* [create](#create) - Bulk create AI models configuration
* [get](#get) - Get all AI models configuration

## create

Configure multiple AI model providers at once. Performs health checks on each model before saving. Use this for initial setup - for individual model management, use /ai-models/providers endpoints.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAIModelsConfig" method="post" path="/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.ai_models_configuration.create()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `ocr`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding`                                                                           | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `slm`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `llm`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `reasoning`                                                                           | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `multi_modal`                                                                         | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve all configured AI model providers grouped by type.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAIModelsConfig" method="get" path="/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.ai_models_configuration.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AIModelsConfig](../../models/aimodelsconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |