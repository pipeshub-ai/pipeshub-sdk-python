# AIModelsProviders

## Overview

Manage individual AI model providers - add, update, delete, and set defaults.

### Available Operations

* [get_models_by_type](#get_models_by_type) - Get models by type
* [get_available_models_by_type](#get_available_models_by_type) - Get available models for selection
* [add_ai_model_provider](#add_ai_model_provider) - Add new AI model provider
* [update_ai_model_provider](#update_ai_model_provider) - Update AI model provider
* [delete_ai_model_provider](#delete_ai_model_provider) - Delete AI model provider
* [set_default_ai_model](#set_default_ai_model) - Set default AI model

## get_models_by_type

Get all configured models of a specific type.

### Example Usage

<!-- UsageSnippet language="python" operationID="getModelsByType" method="get" path="/configurationManager/ai-models/{modelType}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_providers.get_models_by_type(model_type="embedding")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_type`                                                        | [models.ModelType](../../models/modeltype.md)                       | :heavy_check_mark:                                                  | Type of AI model                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetModelsByTypeResponse](../../models/getmodelsbytyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_available_models_by_type

Get available models in a flattened format for UI selection dropdowns.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAvailableModelsByType" method="get" path="/configurationManager/ai-models/available/{modelType}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_providers.get_available_models_by_type(model_type="llm")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_type`                                                        | [models.ModelType](../../models/modeltype.md)                       | :heavy_check_mark:                                                  | Type of AI model                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAvailableModelsByTypeResponse](../../models/getavailablemodelsbytyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_ai_model_provider

Add a new AI model provider configuration. Performs a health check before saving to verify connectivity. Supported providers: openai, anthropic, azure-openai, aws-bedrock, google-vertex, ollama, huggingface.

### Example Usage

<!-- UsageSnippet language="python" operationID="addAIModelProvider" method="post" path="/configurationManager/ai-models/providers" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_providers.add_ai_model_provider(model_type="embedding", provider="openai", configuration={
        "model": "gpt-4",
    }, is_multimodal=False, is_reasoning=False, is_default=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `model_type`                                                                                            | [models.ModelType](../../models/modeltype.md)                                                           | :heavy_check_mark:                                                                                      | Type of AI model                                                                                        |                                                                                                         |
| `provider`                                                                                              | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Provider name (e.g., openai, anthropic, azure-openai, aws-bedrock)                                      | openai                                                                                                  |
| `configuration`                                                                                         | [models.AddAIModelProviderRequestConfiguration](../../models/addaimodelproviderrequestconfiguration.md) | :heavy_check_mark:                                                                                      | Provider-specific configuration                                                                         |                                                                                                         |
| `is_multimodal`                                                                                         | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Whether the model supports multimodal inputs                                                            |                                                                                                         |
| `is_reasoning`                                                                                          | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Whether this is a reasoning model                                                                       |                                                                                                         |
| `is_default`                                                                                            | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | Set as default model for this type                                                                      |                                                                                                         |
| `context_length`                                                                                        | *OptionalNullable[int]*                                                                                 | :heavy_minus_sign:                                                                                      | Maximum context length (tokens)                                                                         |                                                                                                         |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.AIModelProviderResponse](../../models/aimodelproviderresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_ai_model_provider

Update an existing AI model provider configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAIModelProvider" method="put" path="/configurationManager/ai-models/providers/{modelType}/{modelKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.ai_models_providers.update_ai_model_provider(model_type="reasoning", model_key="<value>", provider="<value>", configuration={})

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `model_type`                                                                                                  | [models.ModelType](../../models/modeltype.md)                                                                 | :heavy_check_mark:                                                                                            | Type of AI model                                                                                              |
| `model_key`                                                                                                   | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Unique model key (UUID)                                                                                       |
| `provider`                                                                                                    | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Provider name                                                                                                 |
| `configuration`                                                                                               | [models.UpdateAIModelProviderRequestConfiguration](../../models/updateaimodelproviderrequestconfiguration.md) | :heavy_check_mark:                                                                                            | Updated provider configuration                                                                                |
| `is_multimodal`                                                                                               | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `is_reasoning`                                                                                                | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `is_default`                                                                                                  | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `context_length`                                                                                              | *OptionalNullable[int]*                                                                                       | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_ai_model_provider

Remove an AI model provider configuration. Cannot delete the default model if it's the only one.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAIModelProvider" method="delete" path="/configurationManager/ai-models/providers/{modelType}/{modelKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.ai_models_providers.delete_ai_model_provider(model_type="reasoning", model_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_type`                                                        | [models.ModelType](../../models/modeltype.md)                       | :heavy_check_mark:                                                  | Type of AI model                                                    |
| `model_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_default_ai_model

Set a model as the default for its type.

### Example Usage

<!-- UsageSnippet language="python" operationID="setDefaultAIModel" method="put" path="/configurationManager/ai-models/default/{modelType}/{modelKey}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.ai_models_providers.set_default_ai_model(model_type="ocr", model_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_type`                                                        | [models.ModelType](../../models/modeltype.md)                       | :heavy_check_mark:                                                  | Type of AI model                                                    |
| `model_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |