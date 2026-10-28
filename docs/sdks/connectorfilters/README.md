# ConnectorFilters

## Overview

Dynamic filter options for selecting which data to sync

### Available Operations

* [get_connector_filters](#get_connector_filters) - Get filter options
* [~~save_connector_filters~~](#save_connector_filters) - Save filter selections (deprecated) :warning: **Deprecated**
* [get_filter_field_options](#get_filter_field_options) - Get dynamic filter options

## get_connector_filters

Get available filter options for a connector.<br><br>
<b>Overview:</b><br>
Returns filter fields that can be used to limit what data is synced.
For example, a Google Drive connector might offer filters for
specific folders or file types.<br><br>
<b>Dynamic Filters:</b><br>
Some filter fields have <code>dynamic: true</code> (i.e.
<code>optionSourceType: dynamic</code>), meaning their options are
loaded separately via the filter options endpoint.
For such fields, call
<code>GET /connectors/{connectorId}/filters/{filterKey}/options</code>.
When scoping options to a specific parent (e.g. GitLab projects within
a selected group), pass the parent paths via the
<code>contextGroupPath</code> query parameter on that endpoint.<br><br>
<b>Which connectors answer:</b><br>
An <code>OAUTH</code> connector answers once it has completed sign-in. A connector with
any other auth type (<code>API_TOKEN</code>, <code>BEARER_TOKEN</code>,
<code>OAUTH_ADMIN_CONSENT</code>, <code>BASIC_AUTH</code>, <code>ACCESS_KEY</code>,
<code>ACCOUNT_KEY</code>, <code>CONNECTION_STRING</code>, <code>ENTRA_ID</code>, <code>CUSTOM</code>) answers once its settings,
including the auth section, are saved. A <code>NONE</code> connector (for example RSS)
needs saved settings but no auth section. Otherwise the request is refused with
<code>400</code>.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorFilters" method="get" path="/connectors/{connectorId}/filters" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_filters.get_connector_filters(connector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                               | *str*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | Connector instance ID: 1-64 letters, digits, `_` or `-`<br/>(`400 VALIDATION_ERROR` otherwise). An ID that decodes to an unsafe<br/>path segment is refused with `400` before the token is checked.<br/> |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |

### Response

**[models.GetConnectorFiltersResponse](../../models/getconnectorfiltersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~save_connector_filters~~

<b>Deprecated.</b> Save filters with
<code>PUT /connectors/{connectorId}/config/filters-sync</code> instead, which is what the
PipesHub app uses. That route takes <code>{sync?, filters?: {sync, indexing}}</code>. It ignores the
flat <code>filters</code> map this one takes: the call still returns 200, but nothing is saved.
It also refuses while the connector is active, so disable it first.
This endpoint will be removed in a future release.<br><br>
What this endpoint saves goes to <code>filters.values</code>, which sync does not read:
sync reads <code>filters.sync</code> and <code>filters.indexing</code>.<br><br>
Save the user's filter selections for a connector.<br><br>
<b>Request:</b><br>
<code>filters</code> must hold at least one entry: <code>{"filters": {}}</code> is
refused with <code>400</code>. The server stores whatever it is given under the
connector's saved filter values without checking it against the filter schema.
Use <code>PUT /connectors/{connectorId}/config/filters-sync</code> to save typed
sync and indexing filters.


> :warning: **DEPRECATED**: Use PUT /connectors/{connectorId}/config/filters-sync instead, with a body of {sync?, filters?: {sync, indexing}} (the flat filters map this route takes is ignored there: the call returns 200 and saves none of it), and only while the connector is disabled. This endpoint will be removed in a future release..

### Example Usage

<!-- UsageSnippet language="python" operationID="saveConnectorFilters" method="post" path="/connectors/{connectorId}/filters" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_filters.save_connector_filters(connector_id="<id>", filters={
        "folders": [
            {
                "id": "folder_123",
                "name": "Documents",
            },
            {
                "id": "folder_456",
                "name": "Reports",
            },
        ],
        "fileTypes": [
            "pdf",
            "docx",
        ],
        "modifiedAfter": "2024-01-01",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | Connector instance ID. Unlike `GET` on this path, not checked for<br/>shape: an ID that matches no instance is a `404`. An ID that decodes<br/>to an unsafe path segment is refused with `400` before the token is checked.<br/> |                                                                                                                                                                                                                      |
| `filters`                                                                                                                                                                                                            | Dict[str, *Any*]                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                   | Filter values to save (structure depends on connector's filter schema). Must not be empty.                                                                                                                           | {<br/>"folders": [<br/>{<br/>"id": "folder_123",<br/>"name": "Documents"<br/>},<br/>{<br/>"id": "folder_456",<br/>"name": "Reports"<br/>}<br/>],<br/>"fileTypes": [<br/>"pdf",<br/>"docx"<br/>],<br/>"modifiedAfter": "2024-01-01"<br/>} |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.SaveConnectorFiltersResponse](../../models/saveconnectorfiltersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_filter_field_options

Get options for a dynamic filter field with pagination.<br><br>
<b>Overview:</b><br>
For filters with <code>optionSourceType: dynamic</code>, options are loaded
from the connected service. This supports pagination and search. The
connector is started on demand with its saved credentials, so the
connected service must be reachable.<br><br>
<b>Scoped options (GitLab):</b><br>
When fetching options for the <code>project_ids</code> filter key, pass
one or more <code>contextGroupPath</code> query parameters to restrict
the returned repositories to those that belong to the specified GitLab
group namespace paths (e.g. <code>myorg/team</code>). This is used to
populate the project filter after the user has selected groups. Other
connectors accept and ignore both group path parameters.<br><br>
<b>Examples:</b><br>
<ul>
<li>Google Drive folders list</li>
<li>Slack channels list</li>
<li>Confluence spaces list</li>
<li>GitLab groups list (<code>filterKey=group_ids</code>)</li>
<li>GitLab projects scoped to groups (<code>filterKey=project_ids&amp;contextGroupPath=myorg/team</code>)</li>
</ul>
Query parameters other than the six below are dropped without an error.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFilterFieldOptions" method="get" path="/connectors/{connectorId}/filters/{filterKey}/options" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector_filters.get_filter_field_options(connector_id="<id>", filter_key="buckets", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                  | Connector instance ID                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                     |
| `filter_key`                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                  | Filter field key, the `name` of a field in the connector type's<br/>`config.filters` (`GET /connectors/registry/{connectorType}/schema`).<br/>An unsafe path segment is refused with `400` before the token is checked.<br/>                                                                                                                                        | buckets                                                                                                                                                                                                                                                                                                                                                             |
| `page`                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Page number. An empty value is refused.                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                     |
| `limit`                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Page size, 1 to 100. A value above 100 or an empty value is refused<br/>by the gateway's validator ("Limit must be between 1 and 100.").<br/>                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                     |
| `search`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Search term for filtering options                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                     |
| `cursor`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Cursor for cursor-based pagination, passed on to connectors that page by cursor                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| `context_group_path`                                                                                                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | One or more GitLab group namespace paths (e.g. `myorg/team`).<br/>When provided for the `project_ids` filter key, the returned<br/>options are scoped to repositories that belong to those groups.<br/>Repeat the parameter for multiple groups:<br/>`?contextGroupPath=groupA&contextGroupPath=groupB`. Blank values<br/>are dropped.<br/>                         |                                                                                                                                                                                                                                                                                                                                                                     |
| `exclude_context_group_path`                                                                                                                                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | One or more GitLab group namespace paths to exclude. When provided<br/>for the `project_ids` filter key, the returned options omit<br/>repositories that belong to those groups (used when the<br/>`group_ids` sync filter is `not_in`). Repeat the parameter for<br/>multiple groups:<br/>`?excludeContextGroupPath=groupA&excludeContextGroupPath=groupB`.<br/>Blank values are dropped.<br/> |                                                                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                     |

### Response

**[models.GetFilterFieldOptionsResponse](../../models/getfilterfieldoptionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |