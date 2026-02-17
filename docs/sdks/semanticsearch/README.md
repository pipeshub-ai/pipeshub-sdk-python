# SemanticSearch

## Overview

### Available Operations

* [post](#post) - Perform semantic search
* [history](#history) - Get search history
* [delete_all_history](#delete_all_history) - Clear all search history
* [get_by_id](#get_by_id) - Get search by ID
* [delete](#delete) - Delete search
* [share](#share) - Share search results
* [unshare](#unshare) - Revoke search access
* [archive](#archive) - Archive search
* [unarchive](#unarchive) - Unarchive search

## post

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.post(query="API documentation examples", filters={
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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.post(query="company vacation policy", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
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

## history

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
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.history(limit=10, page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results per page                                          |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchHistoryResponse](../../models/searchhistoryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_all_history

Delete all search history for the authenticated user.<br><br>
<b>Warning:</b><br>
This action cannot be undone. All saved searches will be permanently removed.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteAllSearchHistory" method="delete" path="/search" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.delete_all_history()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAllSearchHistoryResponse](../../models/deleteallsearchhistoryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_id

Retrieve a specific search result by its ID.<br><br>
<b>Overview:</b><br>
Returns the full search record including query, all results,
and any sharing/archive status.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSearchById" method="get" path="/search/{searchId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.get_by_id(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete a specific search from history.<br><br>
<b>Overview:</b><br>
Permanently removes the search record from your history.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSearch" method="delete" path="/search/{searchId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.semantic_search.delete(search_id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## share

Share search results with other users.<br><br>
<b>Overview:</b><br>
Allows sharing a search and its results with colleagues.
Useful for collaborative research or knowledge sharing.


### Example Usage

<!-- UsageSnippet language="python" operationID="shareSearch" method="patch" path="/search/{searchId}/share" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.share(search_id="<value>", user_ids=[
        "507f1f77bcf86cd799439011",
    ], access_level="read")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              | Example                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `search_id`                                                                                                                              | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | N/A                                                                                                                                      |                                                                                                                                          |
| `user_ids`                                                                                                                               | List[*str*]                                                                                                                              | :heavy_check_mark:                                                                                                                       | IDs of users to share with                                                                                                               | [<br/>"507f1f77bcf86cd799439011"<br/>]                                                                                                   |
| `access_level`                                                                                                                           | [Optional[models.ShareRequestAccessLevel]](../../models/sharerequestaccesslevel.md)                                                      | :heavy_minus_sign:                                                                                                                       | Permission level for shared users:<br/><ul><br/><li><code>read</code> - Can view only</li><br/><li><code>write</code> - Can add messages</li><br/></ul><br/> |                                                                                                                                          |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |                                                                                                                                          |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unshare

Remove sharing access from specified users.

### Example Usage

<!-- UsageSnippet language="python" operationID="unshareSearch" method="patch" path="/search/{searchId}/unshare" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.unshare(search_id="<value>", user_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive

Archive a search to hide it from the main history list.

### Example Usage

<!-- UsageSnippet language="python" operationID="archiveSearch" method="patch" path="/search/{searchId}/archive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.archive(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive

Restore an archived search to the active history list.

### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveSearch" method="patch" path="/search/{searchId}/unarchive" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.semantic_search.unarchive(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResult](../../models/searchresult.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |