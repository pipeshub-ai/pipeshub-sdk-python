# SemanticSearch

## Overview

Enterprise semantic search across all indexed knowledge with relevance scoring

### Available Operations

* [search](#search) - Perform semantic search
* [search_history](#search_history) - Get search history
* [delete_all_search_history](#delete_all_search_history) - Clear all search history

## search

Execute a semantic search across your organization's knowledge base.<br><br>
<b>Overview:</b><br>
Semantic search uses AI embeddings to find content based on meaning,
not just keyword matching. This enables finding relevant information
even when the exact words differ.<br><br>
<b>How It Works:</b><br>
<ol>
<li>Your query is converted to a vector embedding</li>
<li>The system finds documents with similar semantic meaning</li>
<li>Results are ranked by relevance score</li>
<li>Matching chunks are returned with metadata</li>
</ol>
<b>Filtering:</b><br>
Use filters to narrow your search:
<ul>
<li><code>filters.apps</code>: Limit to specific connector apps (Google Drive, Confluence, etc.)</li>
<li><code>filters.kb</code>: Limit to specific knowledge bases</li>
</ul>
<b>Results:</b><br>
Each result includes:
<ul>
<li>Matching content chunk</li>
<li>Relevance score (0-1, higher is better)</li>
<li>Source document metadata (name, URL, type)</li>
</ul>
<b>Search History:</b><br>
All searches are saved and can be retrieved via <code>GET /search</code>.


### Example Usage: filtered

<!-- UsageSnippet language="python" operationID="search" method="post" path="/search" example="filtered" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.semantic_search.search(security=models.SearchSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), query="API documentation examples", filters={
        "apps": [
            "drive",
        ],
    }, limit=20)

    # Handle response
    print(res)

```
### Example Usage: simple

<!-- UsageSnippet language="python" operationID="search" method="post" path="/search" example="simple" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.semantic_search.search(security=models.SearchSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), query="company vacation policy", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.SearchSecurity](../../models/searchsecurity.md)                                     | :heavy_check_mark:                                                                          | N/A                                                                                         |                                                                                             |
| `query`                                                                                     | *str*                                                                                       | :heavy_check_mark:                                                                          | Natural language search query. The system understands<br/>semantic meaning, not just keywords.<br/> | employee onboarding procedures                                                              |
| `filters`                                                                                   | [Optional[models.Filters]](../../models/filters.md)                                         | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `limit`                                                                                     | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Maximum number of results to return                                                         |                                                                                             |
| `model_key`                                                                                 | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | AI model to use for embeddings                                                              |                                                                                             |
| `model_name`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Display name of the model                                                                   |                                                                                             |
| `chat_mode`                                                                                 | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Processing mode configuration                                                               |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## search_history

Retrieve your search history with pagination.<br><br>
<b>Overview:</b><br>
Returns a list of all searches performed by the authenticated user.
Each entry includes the original query, results, and metadata.<br><br>
<b>Pagination:</b><br>
Use <code>page</code> and <code>limit</code> to navigate through results.


### Example Usage

<!-- UsageSnippet language="python" operationID="searchHistory" method="get" path="/search" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.semantic_search.search_history(security=models.SearchHistorySecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), limit=10, page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.SearchHistorySecurity](../../models/searchhistorysecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Number of results per page                                            |
| `page`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Page number                                                           |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.SearchHistoryResponse](../../models/searchhistoryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_all_search_history

Delete all search history for the authenticated user.<br><br>
<b>Warning:</b><br>
This action cannot be undone. All saved searches will be permanently removed.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAllSearchHistory" method="delete" path="/search" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.semantic_search.delete_all_search_history(security=models.DeleteAllSearchHistorySecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `security`                                                                       | [models.DeleteAllSearchHistorySecurity](../../deleteallsearchhistorysecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[models.DeleteAllSearchHistoryResponse](../../models/deleteallsearchhistoryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |