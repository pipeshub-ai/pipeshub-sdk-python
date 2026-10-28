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

List the connector and toolset types that support OAuth, from the OAuth registry.<br><br>
Each entry carries the provider URLs, the scopes requested, and the `authFields`
to collect when creating an OAuth configuration for that type.<br><br>
Any authenticated user can call this; it is not limited to admins.


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
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_o_auth_connector_type

Get the OAuth registry entry of one connector or toolset type.<br><br>
`connectorType` is the registered name and is case-sensitive (e.g. `Confluence`).


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

    res = pipeshub.o_auth_configuration.get_o_auth_connector_type(connector_type="Confluence")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                            | *str*                                                                                                       | :heavy_check_mark:                                                                                          | Registered name of the type, case-sensitive                                                                 | Confluence                                                                                                  |
| `page`                                                                                                      | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | Validated like the `page` of `GET /oauth/registry`, then ignored; the reply is the same with or without it. |                                                                                                             |
| `limit`                                                                                                     | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | Validated like the `limit` of `GET /oauth/registry`, then ignored.                                          |                                                                                                             |
| `search`                                                                                                    | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Validated as a single text value, then ignored.                                                             |                                                                                                             |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

### Response

**[models.GetOAuthConnectorTypeResponse](../../models/getoauthconnectortyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
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

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `page`                                                                                                 | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `limit`                                                                                                | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `search`                                                                                               | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Case-insensitive substring matched against the name, connector type, group, description and categories |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[models.ListOAuthConfigsResponse](../../models/listoauthconfigsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403               | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_o_auth_configs_by_type

List the organization's OAuth configurations for one connector type.<br><br>
<b>What comes back depends on the caller:</b><br>
<ul>
<li>An admin gets each stored record in full, including `config` with the client secret in clear text</li>
<li>Any other caller gets only the credential-free fields</li>
</ul>
A connector type with no configurations, or one that does not exist, yields an empty list.


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

    res = pipeshub.o_auth_configuration.list_o_auth_configs_by_type(connector_type="Confluence", scope="team", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               | Confluence                                                                                                                                                                                                                                        |
| `scope`                                                                                                                                                                                                                                           | [Optional[models.ConnectorScope]](../../models/connectorscope.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                | Only OAuth apps usable for this connector scope                                                                                                                                                                                                   | team                                                                                                                                                                                                                                              |
| `page`                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `limit`                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `search`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | Space-separated terms; every term must appear in the name, connector type, group, description or categories                                                                                                                                       |                                                                                                                                                                                                                                                   |
| `reveal`                                                                                                                                                                                                                                          | [Optional[models.RevealStoredSecrets]](../../models/revealstoredsecrets.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | Set to `true` to receive stored secrets instead of placeholders. Honoured only for an<br/>admin's own configuration where the deployment allows it (see `GET<br/>/configurationManager/secretReveal`); ignored for OAuth-app tokens and any other value.<br/> |                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ListOAuthConfigsByTypeResponse](../../models/listoauthconfigsbytyperesponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_o_auth_config

Create a new OAuth configuration for a connector type.<br><br>
<b>Admin Only:</b><br>
Only admins can create OAuth configurations. These provide the
OAuth credentials needed for users to authenticate connectors.<br><br>
<b>Use Case:</b><br>
Before users can create Google Drive connectors with OAuth,
an admin must create an OAuth configuration with the Google
OAuth client ID and secret.<br><br>
The response carries the credential-free view of the new configuration; the
credentials are never echoed back. Success is reported as `200`, not `201`.<br><br>
<b>The connector type is not checked.</b> `connectorType` is not compared with the OAuth
registry, so a misspelled or wrongly-cased name (`confluence` for `Confluence`) does not
fail: the configuration is stored under that name with the default icon and an empty
group, description and category list. It is then returned by
`GET /oauth/{connectorType}` for that same name but never by `GET /oauth`, which only
walks the registered types.<br><br>
Body fields other than `oauthInstanceName`, `config` and `baseUrl` are ignored.


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

    res = pipeshub.o_auth_configuration.create_o_auth_config(connector_type="Confluence", oauth_instance_name="Production Google OAuth Credentials", config=models.CreateOAuthConfigRequestConfig(
        client_id="123456789-abc.apps.googleusercontent.com",
        client_secret="GOCSPX-xxxxxxxxxxxxx",
        tenant_id="12345678-1234-1234-1234-123456789abc",
    ), base_url="https://gitlab.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Confluence                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `oauth_instance_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Display name for this OAuth configuration (e.g., 'Production Google OAuth'). Must be unique for the connector type within the organization. Leading and trailing whitespace is removed before validation, so a name of only whitespace is refused as empty.                                                                                                                                                                                                          | Production Google OAuth Credentials                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `config`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [models.CreateOAuthConfigRequestConfig](../../models/createoauthconfigrequestconfig.md)                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                   | OAuth application credentials, keyed by the `name` of each entry in the connector type's<br/>`authFields` (see `GET /oauth/registry/{connectorType}`), so the keys differ from one<br/>connector type to the next. Must not be empty; neither the keys nor their values are<br/>validated when the configuration is created, so a value of another type (a number,<br/>`null`, a nested object, an array of other items) is stored as sent, also for<br/>`clientId` and `clientSecret`.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `base_url`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                   | PipesHub's public origin, prefixed to the connector's redirect path to build the stored redirectUri. When omitted or empty, the frontend public endpoint is used. The value is not checked to be a URL: whatever text is sent is used as the prefix. Not the provider's URL; a self-hosted provider's address goes in config.                                                                                                                                        | https://pipeshub.mycompany.com                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.CreateOAuthConfigResponse](../../models/createoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 409          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_o_auth_config

Get a specific OAuth configuration by ID.<br><br>
An admin gets `config` with the stored credentials, client secret in clear text.
Any other caller gets the same object without `config`.


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

    res = pipeshub.o_auth_configuration.get_o_auth_config(connector_type="Confluence", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               | Confluence                                                                                                                                                                                                                                        |
| `config_id`                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `reveal`                                                                                                                                                                                                                                          | [Optional[models.RevealStoredSecrets]](../../models/revealstoredsecrets.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | Set to `true` to receive stored secrets instead of placeholders. Honoured only for an<br/>admin's own configuration where the deployment allows it (see `GET<br/>/configurationManager/secretReveal`); ignored for OAuth-app tokens and any other value.<br/> |                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.GetOAuthConfigResponse](../../models/getoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
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

    res = pipeshub.o_auth_configuration.update_o_auth_config(connector_type="Confluence", config_id="<id>", body=models.RequestBody1(
        oauth_instance_name="<value>",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `connector_type`                                                                                            | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         | Confluence                                                                                                  |
| `config_id`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |                                                                                                             |
| `body`                                                                                                      | [models.UpdateOAuthConfigRequestBody](../../models/updateoauthconfigrequestbody.md)                         | :heavy_check_mark:                                                                                          | Send `oauthInstanceName`, `config`, or both; a body with neither is<br/>refused, even if it carries `baseUrl`.<br/> |                                                                                                             |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

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

    res = pipeshub.o_auth_configuration.delete_o_auth_config(connector_type="Confluence", config_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_type`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | Confluence                                                          |
| `config_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteOAuthConfigResponse](../../models/deleteoauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |