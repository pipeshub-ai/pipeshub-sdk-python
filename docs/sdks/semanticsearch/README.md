# SemanticSearch

## Overview

### Available Operations

* [search](#search) - Perform semantic search
* [search_history](#search_history) - Get search history
* [delete_search_history](#delete_search_history) - Clear all search history
* [get_search_by_id](#get_search_by_id) - Get search by ID
* [delete_search_by_id](#delete_search_by_id) - Delete search by ID
* [archive_search](#archive_search) - Archive a search
* [unarchive_search](#unarchive_search) - Unarchive a search

## search

Run a semantic search across your organization's knowledge base.
Matching is meaning-based, so relevant results surface even when
the wording differs from the query.

Use optional `filters` to narrow the scope:

- `filters.apps` — restrict to specific connector apps (for
  example Google Drive or Confluence).
- `filters.kb` — restrict to specific knowledge bases.

The response returns a `searchId` for the persisted search along
with ranked matches, each carrying a relevance score and the
source document's metadata. Past searches can be retrieved via
`GET /search`.


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

    res = pipeshub.semantic_search.search(query="API documentation examples", filters={
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

    res = pipeshub.semantic_search.search(query="company vacation policy", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Natural language search query. The system understands<br/>semantic meaning, not just keywords.<br/>                                                                                                                                                                                                                                                                                                                                                                               | employee onboarding procedures                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.Filters]](../../models/filters.md)                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | App connector instance ids and knowledge-base / record-group ids that narrow retrieval<br/>for a turn. For **org assistant** chat streams, send explicit `apps` / `kb` lists.<br/>For **agent** chat streams, send explicit id lists, or **omit** `filters` (and `tools`)<br/>to let the service use the agent’s stored knowledge and tool configuration. Sending<br/>`{ "apps": [], "kb": [] }` on an agent stream means **no** knowledge sources for that<br/>turn (it is not “full org default”).<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Maximum number of results to return                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | AI model to use for embeddings                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Display name of the model                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model_friendly_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Friendly display name of the model                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `chat_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Processing mode configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.SemanticSearchExecuteResponse](../../models/semanticsearchexecuteresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## search_history

Retrieve the authenticated user's persisted search history.

Returns searches the user owns along with searches shared with them,
scoped to the caller's organization. Archived and deleted entries are
excluded. Citation references on this endpoint are returned as raw
identifier strings; use `GET /search/{searchId}` to fetch a single
search with its citations fully expanded.

Pagination defaults to `page=1, limit=20` (maximum `limit` is 100).
Results are sorted by most recent activity by default.


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

    res = pipeshub.semantic_search.search_history(page=1, limit=20, sort_by="lastActivityAt", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Page number to return. Must be within `[1, 1000]`.                                                                                                                                                                              |
| `limit`                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Number of items per page. Values are clamped to the range `[1, 100]`.                                                                                                                                                           |
| `sort_by`                                                                                                                                                                                                                       | [Optional[models.SearchHistorySortBy]](../../models/searchhistorysortby.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | Field used to sort results. Any value other than `createdAt`,<br/>`lastActivityAt`, or `title` is treated as `lastActivityAt`.<br/>                                                                                             |
| `sort_order`                                                                                                                                                                                                                    | [Optional[models.SearchHistorySortOrder]](../../models/searchhistorysortorder.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                              | Sort direction applied to `sortBy`.                                                                                                                                                                                             |
| `search`                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | Case-insensitive substring to match against a search's title and<br/>message content. Regex metacharacters are escaped automatically.<br/>Values longer than 1000 characters are rejected with `400`.<br/>                      |
| `shared`                                                                                                                                                                                                                        | [Optional[models.SearchHistoryShared]](../../models/searchhistoryshared.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                              | Filter results by their shared status. Accepted values are<br/>`'true'` / `'1'` (return only shared searches) and<br/>`'false'` / `'0'` (exclude shared searches). Matching is<br/>case-insensitive and surrounding whitespace is trimmed.<br/> |
| `start_date`                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                              | ISO 8601 timestamp used as the lower bound for a search's creation date.                                                                                                                                                        |
| `end_date`                                                                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                              | ISO 8601 timestamp used as the upper bound for a search's creation date.                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                             |

### Response

**[models.SemanticSearchHistoryResponse](../../models/semanticsearchhistoryresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.SearchHistoryBadRequestError     | 400                                     | application/json                        |
| errors.SearchHistoryUnauthorizedError   | 401                                     | application/json                        |
| errors.SearchHistoryForbiddenError      | 403                                     | application/json                        |
| errors.SearchHistoryInternalServerError | 500                                     | application/json                        |
| errors.PipeshubDefaultError             | 4XX, 5XX                                | \*/\*                                   |

## delete_search_history

Permanently delete every persisted search row owned by, or shared
with, the authenticated user, along with the citation rows those
searches reference. The action cannot be undone.

Scoped to the caller's org and limited to rows where
`isDeleted: false` and `isArchived: false`. If nothing matches
(including the case where every row is already archived), the
endpoint returns `404` rather than a successful no-op.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSearchHistory" method="delete" path="/search" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.delete_search_history()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                           | Type                                                                                                                                                                                                                | Required                                                                                                                                                                                                            | Description                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search`                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | Restrict the deletion to rows whose `title` or `messages.content`<br/>matches this case-insensitive substring. Special regex characters<br/>are escaped before the lookup; values over 1000 chars are<br/>rejected with `400`.<br/> |
| `shared`                                                                                                                                                                                                            | [Optional[models.DeleteSearchHistoryShared]](../../models/deletesearchhistoryshared.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                  | Restrict the deletion to rows with this `isShared` value<br/>(`'true'` / `'false'`).<br/>                                                                                                                           |
| `start_date`                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                  | ISO 8601 lower bound for `createdAt`. Combined with `endDate`<br/>to scope which rows are deleted.<br/>                                                                                                             |
| `end_date`                                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                  | ISO 8601 upper bound for `createdAt`.                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                 |

### Response

**[models.DeleteSearchHistoryResponse](../../models/deletesearchhistoryresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_search_by_id

Retrieve a previously persisted search by its id, scoped to the
caller's org.

The response body is always an **array** containing zero or one
persisted search document. An unknown id returns an empty array
with a `200` status — callers should check array length rather
than relying on a `404`.


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

    res = pipeshub.semantic_search.get_search_by_id(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique search identifier                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.PersistedSemanticSearch]](../../models/.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetSearchByIDBadRequestError     | 400                                     | application/json                        |
| errors.GetSearchByIDUnauthorizedError   | 401                                     | application/json                        |
| errors.GetSearchByIDForbiddenError      | 403                                     | application/json                        |
| errors.GetSearchByIDNotFoundError       | 404                                     | application/json                        |
| errors.GetSearchByIDInternalServerError | 500                                     | application/json                        |
| errors.PipeshubDefaultError             | 4XX, 5XX                                | \*/\*                                   |

## delete_search_by_id

Permanently delete a single persisted search row, plus every
citation row referenced by its `citationIds`. The caller must
either own the row or have it shared with them.

Scoped to the caller's org and limited to rows where
`isDeleted: false` and `isArchived: false`; archived or
already-deleted rows surface as `404`.


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

    res = pipeshub.semantic_search.delete_search_by_id(search_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_id`                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                              | ObjectId of the persisted search row to delete.                                                                                                                                                                                                                 |
| `search`                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                              | Additional substring filter against `title` / `messages.content`.<br/>The row is only deleted if the `searchId` row also matches this<br/>filter; otherwise `404`. Special regex characters are escaped;<br/>values over 1000 chars or tripping the XSS guard yield `400`.<br/> |
| `shared`                                                                                                                                                                                                                                                        | [Optional[models.DeleteSearchByIDShared]](../../models/deletesearchbyidshared.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                              | Additional `isShared` filter (`'true'` / `'false'`). The row is<br/>only deleted if it also matches this value.<br/>                                                                                                                                            |
| `start_date`                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                              | ISO 8601 lower bound for `createdAt`. The row is only deleted<br/>if its `createdAt` is on or after this value.<br/>                                                                                                                                            |
| `end_date`                                                                                                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                              | ISO 8601 upper bound for `createdAt`. The row is only deleted<br/>if its `createdAt` is on or before this value.<br/>                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                             |

### Response

**[models.DeleteSearchByIDResponse](../../models/deletesearchbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive_search

Archive a specific search result. Archived searches are hidden
from the default search history view but remain retrievable via
the archive-aware listing endpoints.


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

    res = pipeshub.semantic_search.archive_search(search_id="<value>")

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

## unarchive_search

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

    res = pipeshub.semantic_search.unarchive_search(search_id="<value>")

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