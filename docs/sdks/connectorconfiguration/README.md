# ConnectorConfiguration

## Overview

Configure authentication, sync settings, and filters for connectors

### Available Operations

* [get_connector_config](#get_connector_config) - Get connector configuration
* [update_connector_config](#update_connector_config) - Update connector configuration
* [update_connector_auth_config](#update_connector_auth_config) - Update authentication configuration
* [update_connector_filters_sync_config](#update_connector_filters_sync_config) - Update filters and sync configuration

## get_connector_config

Get the current configuration for a connector instance.<br><br>
<b>Security:</b><br>
Stored credentials and OAuth tokens (<code>credentials</code>, <code>oauth</code>)
are never returned. The saved <code>auth</code> values are returned so the
form can be edited, except that each secret (an <code>isSecret</code> or
<code>PASSWORD</code> field of the connector type's auth schema, and a
legacy <code>private_key</code>) comes back as <code>••••••••</code>.
Sending that mask back on a save keeps the stored value. A personal connector's configuration is only
readable by its creator: to anyone else, admins included, it is
answered `404` as if it did not exist. A team connector of another
user is answered `404` to a member.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorConfig" method="get" path="/connectors/{connectorId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.get_connector_config(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Connector instance ID                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectorConfigResponse](../../models/getconnectorconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_connector_config

Update authentication, sync, and filter configuration.<br><br>
<b>Prerequisites:</b><br>
Connector must be <b>disabled</b> before updating configuration.
Disable it first using <code>POST /{id}/toggle</code>.<br><br>
<b>Partial Updates:</b><br>
Only provide the sections you want to update. Omitted sections
are not modified.<br><br>
<b>Secrets:</b><br>
A secret field in <code>auth</code> sent as <code>••••••••</code> keeps the
stored value, so the configuration can be sent back as it was read. The
response masks stored secrets the same way.<br><br>
<b>Signing out:</b><br>
A change to <code>auth</code>, a different top-level <code>oauthConfigId</code>,
or a linked OAuth app that now holds a different client signs the connector
out and clears its OAuth tokens. Sending <code>auth</code> back as it was read,
with secrets as the mask or in full, keeps it signed in.<br><br>
<b>OAuth apps (OAUTH connectors):</b><br>
An OAUTH connector signs in with the client ID and secret of its linked OAuth
app, so client credentials an admin sends in <code>auth</code> go into an app,
as on <code>PUT /{connectorId}/config/auth</code>:
<ul>
  <li>On a connector with no app, an app is created from them and linked
  (<code>auth.oauthConfigId</code> in the response) once every required OAuth
  field is present; until then the values are kept on the connector.</li>
  <li>On a linked connector, changed values update the app named in
  <code>auth.oauthConfigId</code>, and only the fields that changed. Without that
  field a new app is created and linked; the previously linked app, which other
  connectors may share, is not changed.</li>
  <li>The new app is named <code>auth.oauthInstanceName</code>, or else after the
  connector.</li>
</ul>
A linked connector stores no copy of its app's secret fields: they are not
stored, and not returned, in <code>config.auth</code>. Its client ID and provider
URLs are the app's. Only an admin's credentials create or change an app.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorConfig" method="put" path="/connectors/{connectorId}/config" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_config(connector_id="<id>", auth=models.ConnectorAuthConfig(
        **{
            "baseUrl": "https://mycompany.atlassian.net",
            "email": "admin@mycompany.com",
            "apiToken": "ATATT3x...",
        },
    ), base_url="https://confluence.mycompany.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |
| `auth`                                                                                                                                                                                                                                                                                                   | [Optional[models.ConnectorAuthConfig]](../../models/connectorauthconfig.md)                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Auth settings, flat: send each field listed under `auth.schemas.<authType>.fields` in GET /connectors/registry/{connectorType}/schema by its `name`. For OAuth, an admin may send the OAuth app's credentials here (the app is saved and linked), or anyone may send `oauthConfigId` to use a saved app. | {<br/>"baseUrl": "https://mycompany.atlassian.net",<br/>"email": "admin@mycompany.com",<br/>"apiToken": "ATATT3x..."<br/>}                                                                                                                                                                               |
| `sync`                                                                                                                                                                                                                                                                                                   | [Optional[models.ConnectorSyncConfig]](../../models/connectorsyncconfig.md)                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Sync strategy plus connector-specific sync settings, flat: send each field listed under `sync.customFields` in the registry schema by its `name`.                                                                                                                                                        |                                                                                                                                                                                                                                                                                                          |
| `filters`                                                                                                                                                                                                                                                                                                | [Optional[models.ConnectorFiltersConfig]](../../models/connectorfiltersconfig.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |
| `base_url`                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Base URL for self-hosted instances. Any string is accepted; it is<br/>not checked to be a URL.<br/>                                                                                                                                                                                                      | https://confluence.mycompany.com                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |

### Response

**[models.UpdateConnectorConfigResponse](../../models/updateconnectorconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_connector_auth_config

Update only the authentication configuration.<br><br>
<b>Use Case:</b><br>
Use this when you need to update credentials without changing
sync or filter settings. Useful for credential rotation.<br><br>
<b>Prerequisites:</b><br>
Connector must be disabled. This endpoint clears OAuth state,
requiring re-authentication for OAuth connectors.<br><br>
<b>Secrets:</b><br>
A secret field sent as <code>••••••••</code> keeps the stored value; send a
new value to replace it. The response masks stored secrets the same way.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorAuthConfig" method="put" path="/connectors/{connectorId}/config/auth" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_auth_config(connector_id="<id>", auth=models.ConnectorAuthConfig(
        **{
            "baseUrl": "https://mycompany.atlassian.net",
            "email": "admin@mycompany.com",
            "apiToken": "ATATT3x...",
        },
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Connector instance ID                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                          |
| `auth`                                                                                                                                                                                                                                                                                                   | [models.ConnectorAuthConfig](../../models/connectorauthconfig.md)                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Auth settings, flat: send each field listed under `auth.schemas.<authType>.fields` in GET /connectors/registry/{connectorType}/schema by its `name`. For OAuth, an admin may send the OAuth app's credentials here (the app is saved and linked), or anyone may send `oauthConfigId` to use a saved app. | {<br/>"baseUrl": "https://mycompany.atlassian.net",<br/>"email": "admin@mycompany.com",<br/>"apiToken": "ATATT3x..."<br/>}                                                                                                                                                                               |
| `base_url`                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Recomputes the OAuth redirect URI                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |

### Response

**[models.UpdateConnectorAuthConfigResponse](../../models/updateconnectorauthconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_connector_filters_sync_config

Update filter selections and sync settings without touching auth.<br><br>
<b>Use Case:</b><br>
Use this to change what data is synced or adjust sync schedule
without re-authenticating.<br><br>
<b>Merging:</b><br>
`sync` is merged key by key into the saved sync settings. Each of
`filters.sync` and `filters.indexing` that is sent replaces the saved
one. A `sync` or `filters` value that is not an object is skipped
without an error. Fields other than `sync` and `filters`, `baseUrl`
included, are dropped without an error.<br><br>
The connector must be disabled (`400` otherwise).


### Example Usage

<!-- UsageSnippet language="python" operationID="updateConnectorFiltersSyncConfig" method="put" path="/connectors/{connectorId}/config/filters-sync" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_configuration.update_connector_filters_sync_config(connector_id="<id>", body=models.UpdateConnectorFiltersSyncRequest1(
        sync=models.ConnectorSyncConfig(),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Connector instance ID                                                                                   |
| `body`                                                                                                  | [models.UpdateConnectorFiltersSyncRequestUnion](../../models/updateconnectorfilterssyncrequestunion.md) | :heavy_check_mark:                                                                                      | Request payload                                                                                         |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.UpdateConnectorFiltersSyncConfigResponse](../../models/updateconnectorfilterssyncconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |