# AIModelsProviders

## Overview

### Available Operations

* [get_available_models_by_type](#get_available_models_by_type) - Get available models by type

## get_available_models_by_type

Returns a **flattened list** of individual AI models of the requested type,
suitable for use in selection dropdowns and model-picker UIs.

Each provider configuration entry may specify multiple comma-separated model
names; this endpoint expands those into one object per model name so callers
receive a flat, enumerable collection.

**Flattening rules:**
- Only the **first** model in a multi-model provider entry is marked
  `isDefault: true`; all subsequent models from the same entry get `false`.
- `modelFriendlyName` is included **only** when the provider entry contains
  exactly one model name (not a comma-separated list).
- When no providers of the requested type are configured the endpoint still
  returns HTTP **200** with an empty `models` array — this is **not** an error.

**Access control:** requires a valid bearer token. For OAuth tokens the
`config:read` scope must be present; regular JWT bearer tokens pass through
without scope enforcement.


### Example Usage: no_models_configured

<!-- UsageSnippet language="python" operationID="getAvailableModelsByType" method="get" path="/configurationManager/ai-models/available/{modelType}" example="no_models_configured" -->
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
### Example Usage: two_llm_models

<!-- UsageSnippet language="python" operationID="getAvailableModelsByType" method="get" path="/configurationManager/ai-models/available/{modelType}" example="two_llm_models" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.ai_models_providers.get_available_models_by_type(model_type="embedding")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_type`                                                                                                                                      | [models.ModelType](../../models/modeltype.md)                                                                                                     | :heavy_check_mark:                                                                                                                                | Category of AI model to retrieve.<br/><br/>Must be one of: `llm`, `embedding`, `ocr`, `slm`, `reasoning`, `multiModal`, `imageGeneration`, `tts`, `stt`.<br/> |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.GetAvailableModelsByTypeResponse](../../models/getavailablemodelsbytyperesponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.GetAvailableModelsByTypeBadRequestError     | 400                                                | application/json                                   |
| errors.GetAvailableModelsByTypeUnauthorizedError   | 401                                                | application/json                                   |
| errors.GetAvailableModelsByTypeForbiddenError      | 403                                                | application/json                                   |
| errors.GetAvailableModelsByTypeInternalServerError | 500                                                | application/json                                   |
| errors.PipeshubDefaultError                        | 4XX, 5XX                                           | \*/\*                                              |