# ConnectorFilters

## Overview

### Available Operations

* [get](#get) - Get filter options
* [save](#save) - Save filter selections
* [get_options](#get_options) - Get dynamic filter options

## get

Get available filter options for a connector.<br><br>
<b>Overview:</b><br>
Returns filter fields that can be used to limit what data is synced.
For example, a Google Drive connector might offer filters for
specific folders or file types.<br><br>
<b>Dynamic Filters:</b><br>
Some filter fields have <code>dynamic: true</code>, meaning their
options are loaded separately via the filter options endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorFilters" method="get" path="/connectors/{connectorId}/filters" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_filters.get(connector_id="<id>")

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
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## save

Save the user's filter selections for a connector.<br><br>
<b>Overview:</b><br>
After viewing filter options, use this endpoint to save the
selected values. These determine what data will be synced.


### Example Usage

<!-- UsageSnippet language="python" operationID="saveConnectorFilters" method="post" path="/connectors/{connectorId}/filters" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_filters.save(connector_id="<id>", filters={
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
| `filters`                                                                                                                                                                | Dict[str, *Any*]                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                       | Filter values to save (structure depends on connector's filter schema)                                                                                                   | {<br/>"folders": [<br/>{<br/>"id": "folder_123",<br/>"name": "Documents"<br/>},<br/>{<br/>"id": "folder_456",<br/>"name": "Reports"<br/>}<br/>],<br/>"fileTypes": [<br/>"pdf",<br/>"docx"<br/>],<br/>"modifiedAfter": "2024-01-01"<br/>} |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |                                                                                                                                                                          |

### Response

**[models.SaveConnectorFiltersResponse](../../models/saveconnectorfiltersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_options

Get options for a dynamic filter field with pagination.<br><br>
<b>Overview:</b><br>
For filters with <code>dynamic: true</code>, options are loaded
from the connected service. This supports pagination and search.<br><br>
<b>Examples:</b><br>
<ul>
<li>Google Drive folders list</li>
<li>Slack channels list</li>
<li>Confluence spaces list</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getFilterFieldOptions" method="get" path="/connectors/{connectorId}/filters/{filterKey}/options" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.connector_filters.get_options(connector_id="<id>", filter_key="folders", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connector_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `filter_key`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Filter field key                                                    | folders                                                             |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search term for filtering options                                   |                                                                     |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor for cursor-based pagination                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetFilterFieldOptionsResponse](../../models/getfilterfieldoptionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |