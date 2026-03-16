# AiModelsConfiguration

## Overview

### Available Operations

* [get](#get) - Get AI models configuration
* [create](#create) - Create AI models configuration

## get

Retrieve the AI models configuration for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAIModelsConfig" method="get" path="/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_configuration.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAIModelsConfigResponse](../../models/getaimodelsconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create or initialize AI models configuration for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="createAIModelsConfig" method="post" path="/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_configuration.create(ocr=[
        {
            "model_key": "5ede6150-da0e-46b1-9220-c3dc8dacd6cd",
            "provider": "openAI",
            "configuration": {
                "model": "gpt-4o",
            },
        },
    ], embedding=[
        {
            "model_key": "5ede6150-da0e-46b1-9220-c3dc8dacd6cd",
            "provider": "openAI",
            "configuration": {
                "model": "gpt-4o",
            },
        },
    ], llm=[
        {
            "provider": "groq",
            "configuration": {
                "model": "gpt-4o",
                "api_key": "sk-example",
            },
            "is_default": True,
        },
    ], slm=[
        {
            "model_key": "5ede6150-da0e-46b1-9220-c3dc8dacd6cd",
            "provider": "openAI",
            "configuration": {
                "model": "gpt-4o",
            },
        },
    ], reasoning=[
        {
            "model_key": "5ede6150-da0e-46b1-9220-c3dc8dacd6cd",
            "provider": "openAI",
            "configuration": {
                "model": "gpt-4o",
            },
        },
    ], multi_modal=[
        {
            "model_key": "5ede6150-da0e-46b1-9220-c3dc8dacd6cd",
            "provider": "openAI",
            "configuration": {
                "model": "gpt-4o",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `ocr`                                                                     | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `embedding`                                                               | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `llm`                                                                     | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `slm`                                                                     | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `reasoning`                                                               | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `multi_modal`                                                             | List[[models.AIModelConfiguration](../../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `custom_system_prompt`                                                    | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateAIModelsConfigResponse](../../models/createaimodelsconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |