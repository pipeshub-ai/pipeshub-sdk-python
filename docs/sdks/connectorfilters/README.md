# ConnectorFilters

## Overview

Dynamic filter options for selecting which data to sync

### Available Operations

* [get_connector_filters](#get_connector_filters) - Get filter options
* [save_connector_filters](#save_connector_filters) - Save filter selections
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
Only connectors with auth type <code>API_TOKEN</code>, <code>USERNAME_PASSWORD</code>
or <code>OAUTH_ADMIN_CONSENT</code> (and saved settings), and <code>OAUTH</code>
connectors that have completed sign-in. Every other connector is refused with <code>400</code>:
those with auth type <code>NONE</code> (for example RSS), <code>BASIC_AUTH</code>,
<code>ACCESS_KEY</code>, <code>CONNECTION_STRING</code> or <code>CUSTOM</code>
(<code>Unsupported authentication type: ...</code>), an OAUTH connector that has not
signed in, and a token or password connector with no saved settings.
Their filter fields are in the registry schema; dynamic values come from
<code>GET /connectors/{connectorId}/filters/{filterKey}/options</code>.


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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectorFiltersResponse](../../models/getconnectorfiltersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## save_connector_filters

Save the user's filter selections for a connector.<br><br>
<b>Overview:</b><br>
After viewing filter options, use this endpoint to save the
selected values. These determine what data will be synced.<br><br>
<b>Request:</b><br>
<code>filters</code> must hold at least one entry: <code>{"filters": {}}</code> is
refused with <code>400</code>. The server stores whatever it is given under the
connector's saved filter values without checking it against the filter schema.
Use <code>PUT /connectors/{connectorId}/config/filters-sync</code> to save typed
sync and indexing filters.


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

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              | Example                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `connector_id`                                                                                                                                                           | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `filters`                                                                                                                                                                | Dict[str, *Any*]                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                       | Filter values to save (structure depends on connector's filter schema). Must not be empty.                                                                               | {<br/>"folders": [<br/>{<br/>"id": "folder_123",<br/>"name": "Documents"<br/>},<br/>{<br/>"id": "folder_456",<br/>"name": "Reports"<br/>}<br/>],<br/>"fileTypes": [<br/>"pdf",<br/>"docx"<br/>],<br/>"modifiedAfter": "2024-01-01"<br/>} |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |                                                                                                                                                                          |

### Response

**[models.SaveConnectorFiltersResponse](../../models/saveconnectorfiltersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404, 409     | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_filter_field_options

Get options for a dynamic filter field with pagination.<br><br>
<b>Overview:</b><br>
For filters with <code>optionSourceType: dynamic</code>, options are loaded
from the connected service. This supports pagination and search.<br><br>
<b>Scoped options (GitLab):</b><br>
When fetching options for the <code>project_ids</code> filter key, pass
one or more <code>contextGroupPath</code> query parameters to restrict
the returned repositories to those that belong to the specified GitLab
group namespace paths (e.g. <code>myorg/team</code>). This is used to
populate the project filter after the user has selected groups.<br><br>
<b>Examples:</b><br>
<ul>
<li>Google Drive folders list</li>
<li>Slack channels list</li>
<li>Confluence spaces list</li>
<li>GitLab groups list (<code>filterKey=group_ids</code>)</li>
<li>GitLab projects scoped to groups (<code>filterKey=project_ids&amp;contextGroupPath=myorg/team</code>)</li>
</ul>


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

| Parameter                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector_id`                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                       | Connector instance ID                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                          |
| `filter_key`                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                       | Filter field key                                                                                                                                                                                                                                                                                                                         | buckets                                                                                                                                                                                                                                                                                                                                  |
| `page`                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                          |
| `search`                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | Search term for filtering options                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                          |
| `cursor`                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | Cursor for cursor-based pagination                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                          |
| `context_group_path`                                                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | One or more GitLab group namespace paths (e.g. `myorg/team`).<br/>When provided for the `project_ids` filter key, the returned<br/>options are scoped to repositories that belong to those groups.<br/>Repeat the parameter for multiple groups:<br/>`?contextGroupPath=groupA&contextGroupPath=groupB`<br/>                             |                                                                                                                                                                                                                                                                                                                                          |
| `exclude_context_group_path`                                                                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | One or more GitLab group namespace paths to exclude. When provided<br/>for the `project_ids` filter key, the returned options omit<br/>repositories that belong to those groups (used when the<br/>`group_ids` sync filter is `not_in`). Repeat the parameter for<br/>multiple groups:<br/>`?excludeContextGroupPath=groupA&excludeContextGroupPath=groupB`<br/> |                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.GetFilterFieldOptionsResponse](../../models/getfilterfieldoptionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |