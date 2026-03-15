# ConfigurationManager

## Overview

### Available Operations

* [get_slack_bot_configs](#get_slack_bot_configs) - Get Slack bot configurations
* [create_slack_bot_config](#create_slack_bot_config) - Create Slack bot configuration
* [update_slack_bot_config](#update_slack_bot_config) - Update Slack bot configuration
* [delete_slack_bot_config](#delete_slack_bot_config) - Delete Slack bot configuration

## get_slack_bot_configs

Retrieve all Slack bot configurations for the organization.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSlackBotConfigs" method="get" path="/configurationManager/slack-bot" -->
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

<!-- UsageSnippet language="python" operationID="createSlackBotConfig" method="post" path="/configurationManager/slack-bot" -->
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

<!-- UsageSnippet language="python" operationID="updateSlackBotConfig" method="put" path="/configurationManager/slack-bot/{configId}" -->
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

<!-- UsageSnippet language="python" operationID="deleteSlackBotConfig" method="delete" path="/configurationManager/slack-bot/{configId}" -->
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