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

    res = pipeshub.configuration_manager.create_slack_bot_config(name="<value>", bot_token="<value>", signing_secret="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Bot display name                                                    |
| `bot_token`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Slack bot token                                                     |
| `signing_secret`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Slack signing secret                                                |
| `agent_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Associated agent ID                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = pipeshub.configuration_manager.update_slack_bot_config(config_id="<id>", name="<value>", bot_token="<value>", signing_secret="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Bot display name                                                    |
| `bot_token`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Slack bot token                                                     |
| `signing_secret`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Slack signing secret                                                |
| `agent_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Associated agent ID                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = pipeshub.configuration_manager.set_metrics_collection_push_interval(push_interval_ms=394545)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `push_interval_ms`                                                  | *int*                                                               | :heavy_check_mark:                                                  | Push interval in milliseconds                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = pipeshub.configuration_manager.set_metrics_collection_remote_server(server_url_="https://exhausted-perp.net/")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_url`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

**[models.AIModelsConfig](../../models/aimodelsconfig.md)**

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

    res = pipeshub.configuration_manager.create_ai_models_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `llm`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding`                                                                           | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `ocr`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `slm`                                                                                 | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `reasoning`                                                                           | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `multi_modal`                                                                         | List[[models.AIModelProviderConfigInput](../../models/aimodelproviderconfiginput.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

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