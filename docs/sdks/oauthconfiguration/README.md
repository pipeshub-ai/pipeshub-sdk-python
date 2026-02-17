# OauthConfiguration

## Overview

### Available Operations

* [list_registry](#list_registry) - List OAuth-capable connector types
* [get_connector_type](#get_connector_type) - Get OAuth connector type details
* [list](#list) - List OAuth configurations
* [list_by_type](#list_by_type) - List OAuth configs for connector type
* [create](#create) - Create OAuth configuration
* [get](#get) - Get OAuth configuration
* [update](#update) - Update OAuth configuration
* [delete](#delete) - Delete OAuth configuration

## list_registry

Get all connector types that support OAuth authentication.<br><br>
<b>Admin Use:</b><br>
Admins use this to see which connector types need OAuth credentials
to be configured before users can authenticate.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthRegistry" method="get" path="/oauth/registry" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.list_registry(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthRegistryResponse](../../models/getoauthregistryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_type

Get details for a specific OAuth-capable connector type.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthConnectorType" method="get" path="/oauth/registry/{connectorType}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.get_connector_type(connector_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthConnectorTypeResponse](../../models/getoauthconnectortyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list

List all OAuth configurations for the organization.<br><br>
<b>Security:</b><br>
<ul>
<li>Admins see full configuration including credentials</li>
<li>Non-admins see only essential fields (client ID, not secret)</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthConfigs" method="get" path="/oauth" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.list(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOAuthConfigsResponse](../../models/listoauthconfigsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_by_type

Get all OAuth configurations for a specific connector type.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthConfigsByType" method="get" path="/oauth/{connectorType}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.list_by_type(connector_type="<value>", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOAuthConfigsByTypeResponse](../../models/listoauthconfigsbytyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create a new OAuth configuration for a connector type.<br><br>
<b>Admin Only:</b><br>
Only admins can create OAuth configurations. These provide the
OAuth credentials needed for users to authenticate connectors.<br><br>
<b>Use Case:</b><br>
Before users can create Google Drive connectors with OAuth,
an admin must create an OAuth configuration with the Google
OAuth client ID and secret.


### Example Usage

<!-- UsageSnippet language="python" operationID="createOAuthConfig" method="post" path="/oauth/{connectorType}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.create(connector_type="<value>", oauth_instance_name="Production Google OAuth Credentials", config={
        "client_id": "123456789-abc.apps.googleusercontent.com",
        "client_secret": "GOCSPX-xxxxxxxxxxxxx",
        "tenant_id": "12345678-1234-1234-1234-123456789abc",
    }, base_url="https://gitlab.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `connector_type`                                                                        | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `oauth_instance_name`                                                                   | *str*                                                                                   | :heavy_check_mark:                                                                      | Display name for this OAuth configuration (e.g., 'Production Google OAuth')             | Production Google OAuth Credentials                                                     |
| `config`                                                                                | [models.CreateOAuthConfigRequestConfig](../../models/createoauthconfigrequestconfig.md) | :heavy_check_mark:                                                                      | OAuth application credentials                                                           |                                                                                         |
| `base_url`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Base URL for self-hosted instances (e.g., GitLab Self-Managed)                          | https://gitlab.mycompany.com                                                            |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.CreateOAuthConfigResponse](../../models/createoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Get a specific OAuth configuration by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthConfig" method="get" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.get(connector_type="<value>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthConfigResponse](../../models/getoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update an OAuth configuration.<br><br>
<b>Admin Only:</b><br>
Only the creator or another admin can update.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateOAuthConfig" method="put" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.update(connector_type="<value>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `connector_type`                                                                    | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `config_id`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `oauth_instance_name`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `config`                                                                            | [Optional[models.UpdateOAuthConfigConfig]](../../models/updateoauthconfigconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UpdateOAuthConfigResponse](../../models/updateoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete an OAuth configuration.<br><br>
<b>Warning:</b><br>
Cannot delete if the configuration is used by active connectors.
Disable or delete dependent connectors first.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOAuthConfig" method="delete" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.oauth_configuration.delete(connector_type="<value>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOAuthConfigResponse](../../models/deleteoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |