# SemanticSearch

## Overview

### Available Operations

* [post](#post) - Perform semantic search
* [history](#history) - Get search history
* [delete_all_history](#delete_all_history) - Clear all search history
* [get_by_id](#get_by_id) - Get search by ID
* [delete](#delete) - Delete search by ID
* [share](#share) - Share a search
* [unshare](#unshare) - Unshare a search
* [archive](#archive) - Archive a search
* [unarchive](#unarchive) - Unarchive a search

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.post(query="API documentation examples", filters={
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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.post(query="company vacation policy", filters={
        "apps": [
            "550e8400-e29b-41d4-a716-446655440000",
        ],
    }, limit=10)

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.history(limit=10, page=1)

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.delete_all_history()

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

Retrieve a specific search result by its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSearchById" method="get" path="/search/{searchId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.get_by_id(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.SearchResult]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete a specific search result by its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSearchById" method="delete" path="/search/{searchId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.delete(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSearchByIDResponse](../../models/deletesearchbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## share

Share a specific search result, making it accessible to other users.


### Example Usage

<!-- UsageSnippet language="python" operationID="shareSearch" method="patch" path="/search/{searchId}/share" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.share(search_id="<value>", user_ids=[
        "507f1f77bcf86cd799439011",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |                                                                     |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 | [<br/>"507f1f77bcf86cd799439011"<br/>]                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ShareSearchResponse](../../models/sharesearchresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unshare

Revoke sharing for a specific search result, making it private again.


### Example Usage

<!-- UsageSnippet language="python" operationID="unshareSearch" method="patch" path="/search/{searchId}/unshare" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.unshare(search_id="<value>", user_ids=[
        "507f1f77bcf86cd799439011",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |                                                                     |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 | [<br/>"507f1f77bcf86cd799439011"<br/>]                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnshareSearchResponse](../../models/unsharesearchresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive

Archive a specific search result. Archived searches are hidden from the default search history view.


### Example Usage

<!-- UsageSnippet language="python" operationID="archiveSearch" method="patch" path="/search/{searchId}/archive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.archive(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ArchiveSearchResponse](../../models/archivesearchresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive

Restore a previously archived search result back to the active search history.


### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveSearch" method="patch" path="/search/{searchId}/unarchive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.unarchive(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnarchiveSearchResponse](../../models/unarchivesearchresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |