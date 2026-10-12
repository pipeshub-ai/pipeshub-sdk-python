# WebSearch

## Overview

Manage web search providers (DuckDuckGo, Serper, Tavily, Exa) and settings for internet search.

### Available Operations

* [get_web_search_providers](#get_web_search_providers) - Get all web search providers

## get_web_search_providers

Retrieve all configured web search providers and current web search settings.

**Authentication:** Session JWT or OAuth 2.0 access token via `Authorization: Bearer`.
OAuth tokens must include the `config:read` scope. Admin role is not required.

**API keys:** for anyone who isn't an org admin, each provider's `configuration.apiKey`
comes back as the placeholder `****************`. Admins get the stored key, unless the
server hides secrets from everyone (`HIDE_SECRET_CONFIG=true`). When updating a provider,
sending the placeholder back keeps the stored key.


### Example Usage

<!-- UsageSnippet language="python" operationID="getWebSearchProviders" method="get" path="/configurationManager/web-search" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.web_search.get_web_search_providers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebSearchProvidersResponse](../../models/websearchprovidersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 403                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |