# OAuthConfiguration

## Overview

Admin management of OAuth credentials for connector types

### Available Operations

* [get_o_auth_registry](#get_o_auth_registry) - List OAuth-capable connector types
* [get_o_auth_connector_type](#get_o_auth_connector_type) - Get OAuth connector type details
* [list_o_auth_configs](#list_o_auth_configs) - List OAuth configurations
* [list_o_auth_configs_by_type](#list_o_auth_configs_by_type) - List OAuth configs for connector type
* [create_o_auth_config](#create_o_auth_config) - Create OAuth configuration
* [get_o_auth_config](#get_o_auth_config) - Get OAuth configuration
* [update_o_auth_config](#update_o_auth_config) - Update OAuth configuration
* [delete_o_auth_config](#delete_o_auth_config) - Delete OAuth configuration

## get_o_auth_registry

Get all connector types that support OAuth authentication.<br><br>
<b>Admin Use:</b><br>
Admins use this to see which connector types need OAuth credentials
to be configured before users can authenticate.


### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthRegistry" method="get" path="/oauth/registry" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.get_o_auth_registry(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Matches the connector type's name, group or description             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthRegistryResponse](../../models/getoauthregistryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_o_auth_connector_type

Get details for a specific OAuth-capable connector type.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthConnectorType" method="get" path="/oauth/registry/{connectorType}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.get_o_auth_connector_type(connector_type="<value>")

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
| errors.ErrorResponse        | 401, 403, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_o_auth_configs

List the saved OAuth apps of every connector type in the organization.<br><br>
Every caller, admin or not, gets the same essential fields (ID, name, connector type, app
metadata, timestamps). Credentials are never included; an admin reads them per app with
<code>GET /oauth/{connectorType}/{configId}</code>.


### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthConfigs" method="get" path="/oauth" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.list_o_auth_configs(page=1, limit=20)

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
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_o_auth_configs_by_type

Get all OAuth configurations for a specific connector type.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOAuthConfigsByType" method="get" path="/oauth/{connectorType}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.list_o_auth_configs_by_type(connector_type="<value>", scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `scope`                                                                                                                                                                                                                                           | [Optional[models.ConnectorScope]](../../models/connectorscope.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                | Only OAuth apps usable for this connector scope                                                                                                                                                                                                   | team                                                                                                                                                                                                                                              |
| `page`                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `limit`                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `search`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `reveal`                                                                                                                                                                                                                                          | [Optional[models.RevealStoredSecrets]](../../models/revealstoredsecrets.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | Set to `true` to receive stored secrets instead of placeholders. Honoured only for an<br/>admin's own configuration where the deployment allows it (see `GET<br/>/configurationManager/secretReveal`); ignored for OAuth-app tokens and any other value.<br/> |                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ListOAuthConfigsByTypeResponse](../../models/listoauthconfigsbytyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_o_auth_config

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.create_o_auth_config(connector_type="<value>", oauth_instance_name="Production Google OAuth Credentials", config={
        "client_id": "123456789-abc.apps.googleusercontent.com",
        "client_secret": "GOCSPX-xxxxxxxxxxxxx",
        "tenant_id": "12345678-1234-1234-1234-123456789abc",
    }, base_url="https://gitlab.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `oauth_instance_name`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | Display name for this OAuth configuration (e.g., 'Production Google OAuth')                                                                                                                                                       | Production Google OAuth Credentials                                                                                                                                                                                               |
| `config`                                                                                                                                                                                                                          | [models.CreateOAuthConfigRequestConfig](../../models/createoauthconfigrequestconfig.md)                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                | OAuth application credentials                                                                                                                                                                                                     |                                                                                                                                                                                                                                   |
| `base_url`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | PipesHub's public origin, prefixed to the connector's redirect path to build the stored redirectUri. When omitted, the frontend public endpoint is used. Not the provider's URL; a self-hosted provider's address goes in config. | https://pipeshub.mycompany.com                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                               |                                                                                                                                                                                                                                   |

### Response

**[models.CreateOAuthConfigResponse](../../models/createoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 409          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_o_auth_config

Get a specific OAuth configuration by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthConfig" method="get" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.get_o_auth_config(connector_type="<value>", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |
| `config_id`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |
| `reveal`                                                                                                                                                                                                                                          | [Optional[models.RevealStoredSecrets]](../../models/revealstoredsecrets.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | Set to `true` to receive stored secrets instead of placeholders. Honoured only for an<br/>admin's own configuration where the deployment allows it (see `GET<br/>/configurationManager/secretReveal`); ignored for OAuth-app tokens and any other value.<br/> |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |

### Response

**[models.GetOAuthConfigResponse](../../models/getoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_o_auth_config

Update an OAuth configuration.<br><br>
<b>Admin Only:</b><br>
Only an admin can update, including apps another admin created.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateOAuthConfig" method="put" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.update_o_auth_config(connector_type="<value>", config_id="<id>", body=models.RequestBody1(
        oauth_instance_name="<value>",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                            | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `config_id`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `body`                                                                                                      | [models.UpdateOAuthConfigRequestBody](../../models/updateoauthconfigrequestbody.md)                         | :heavy_check_mark:                                                                                          | Send `oauthInstanceName`, `config`, or both; a body with neither is<br/>refused, even if it carries `baseUrl`.<br/> |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.UpdateOAuthConfigResponse](../../models/updateoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_o_auth_config

Delete an OAuth configuration.<br><br>
<b>Admin Only:</b><br>
Only admins can delete OAuth configurations.<br><br>
<b>Warning:</b><br>
The server does not check whether connectors still use the configuration:
it is deleted either way, and those connectors lose their OAuth app.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOAuthConfig" method="delete" path="/oauth/{connectorType}/{configId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_configuration.delete_o_auth_config(connector_type="<value>", config_id="<id>")

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
| errors.ErrorResponse        | 401, 403, 404               | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |