# ConfigurationManager

## Overview

### Available Operations

* [get_slack_bot_configs](#get_slack_bot_configs) - Get Slack bot configurations
* [create_slack_bot_config](#create_slack_bot_config) - Create Slack bot configuration
* [update_slack_bot_config](#update_slack_bot_config) - Update Slack bot configuration
* [delete_slack_bot_config](#delete_slack_bot_config) - Delete Slack bot configuration
* [set_metrics_collection_push_interval](#set_metrics_collection_push_interval) - Set metrics push interval
* [set_metrics_collection_remote_server](#set_metrics_collection_remote_server) - Set metrics remote server URL
* [get_ai_models_config](#get_ai_models_config) - Get AI models configuration
* [create_ai_models_config](#create_ai_models_config) - Create AI models configuration
* [get_ai_models_providers](#get_ai_models_providers) - Get AI model providers

## get_slack_bot_configs

Retrieve all Slack bot configurations for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSlackBotConfigs" method="get" path="/api/v1/configurationManager/slack-bot" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.get_slack_bot_configs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSlackBotConfigsResponse](../../models/getslackbotconfigsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_slack_bot_config

Create a new Slack bot configuration for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="createSlackBotConfig" method="post" path="/api/v1/configurationManager/slack-bot" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.create_slack_bot_config(name="PipesHub Bot", bot_token="xoxb-example-token", signing_secret="abc123signingsecret")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Slack Bot display name                                              | PipesHub Bot                                                        |
| `bot_token`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Slack Bot OAuth token                                               | xoxb-example-token                                                  |
| `signing_secret`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Slack app signing secret                                            | abc123signingsecret                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional agent ID to link to this bot                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateSlackBotConfigResponse](../../models/createslackbotconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_slack_bot_config

Update an existing Slack bot configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateSlackBotConfig" method="put" path="/api/v1/configurationManager/slack-bot/{configId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.update_slack_bot_config(config_id="<id>", name="PipesHub Bot", bot_token="xoxb-example-token", signing_secret="abc123signingsecret")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Slack Bot display name                                              | PipesHub Bot                                                        |
| `bot_token`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Slack Bot OAuth token                                               | xoxb-example-token                                                  |
| `signing_secret`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Slack app signing secret                                            | abc123signingsecret                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional agent ID to link to this bot                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateSlackBotConfigResponse](../../models/updateslackbotconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_slack_bot_config

Delete a Slack bot configuration.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSlackBotConfig" method="delete" path="/api/v1/configurationManager/slack-bot/{configId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.delete_slack_bot_config(config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSlackBotConfigResponse](../../models/deleteslackbotconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_metrics_collection_push_interval

Configure the interval for pushing metrics to the collection server.


### Example Usage

<!-- UsageSnippet language="python" operationID="setMetricsCollectionPushInterval" method="patch" path="/api/v1/configurationManager/metricsCollection/pushInterval" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.set_metrics_collection_push_interval(push_interval_ms=60000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `push_interval_ms`                                                  | *float*                                                             | :heavy_check_mark:                                                  | Push interval in milliseconds                                       | 60000                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsCollectionPushIntervalResponse](../../models/setmetricscollectionpushintervalresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_metrics_collection_remote_server

Configure the remote server URL for metrics collection.


### Example Usage

<!-- UsageSnippet language="python" operationID="setMetricsCollectionRemoteServer" method="patch" path="/api/v1/configurationManager/metricsCollection/serverUrl" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.set_metrics_collection_remote_server(server_url_="https://metrics-collector.example.com/collect-metrics")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_url`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | https://metrics-collector.example.com/collect-metrics               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetMetricsCollectionRemoteServerResponse](../../models/setmetricscollectionremoteserverresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_ai_models_config

Retrieve the AI models configuration for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAIModelsConfig" method="get" path="/api/v1/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.get_ai_models_config()

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

## create_ai_models_config

Create or initialize AI models configuration for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="createAIModelsConfig" method="post" path="/api/v1/configurationManager/aiModelsConfig" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.create_ai_models_config(ocr=[
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

## get_ai_models_providers

Retrieve all available AI model providers.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAIModelsProviders" method="get" path="/api/v1/configurationManager/ai-models" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.configuration_manager.get_ai_models_providers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAIModelsProvidersResponse](../../models/getaimodelsprovidersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |