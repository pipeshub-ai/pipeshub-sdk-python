# QueryService

## Overview

### Available Operations

* [check_health](#check_health) - [Query Service] Health check
* [search](#search) - [Query Service] Semantic search
* [chat](#chat) - [Query Service] Chat with knowledge base
* [chat_stream](#chat_stream) - [Query Service] Streaming chat with knowledge base
* [health_check](#health_check) - [Query Service] AI model health check
* [list_tools](#list_tools) - [Query Service] List available agent tools

## check_health

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Health check endpoint for the Query Service (Python FastAPI).<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Authentication:</b> None required for health check<br><br>

<b>Note:</b> This is an internal service health endpoint. It also verifies
connectivity to the Connector Service as a dependency check.


### Example Usage

<!-- UsageSnippet language="python" operationID="queryServiceHealth" method="get" path="/query/health" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.query_service.check_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.QueryServiceHealthResponse](../../models/queryservicehealthresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.FailError            | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## search

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Perform semantic search across indexed documents using vector embeddings.<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Authentication:</b> Requires user JWT token (proxied from main API) or scoped service token<br><br>

<b>How It Works:</b><br>
<ol>
<li>Query is transformed and expanded using LLM</li>
<li>Embeddings are generated for search queries</li>
<li>Vector similarity search in Qdrant</li>
<li>Results filtered by user permissions</li>
<li>Optional knowledge base filtering</li>
</ol>


### Example Usage

<!-- UsageSnippet language="python" operationID="queryServiceSearch" method="post" path="/query/api/v1/search" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.query_service.search(query="How do I configure SSO?", limit=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `query`                                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | Search query text                                                                       | How do I configure SSO?                                                                 |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | Maximum number of results                                                               |                                                                                         |
| `filters`                                                                               | [Optional[models.QueryServiceSearchFilters]](../../models/queryservicesearchfilters.md) | :heavy_minus_sign:                                                                      | Optional filters (e.g., kb IDs)                                                         |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |
| `server_url`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | An optional server URL to use.                                                          | http://localhost:8080                                                                   |

### Response

**[models.QueryServiceSearchResponse](../../models/queryservicesearchresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## chat

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Conversational AI endpoint with RAG (Retrieval-Augmented Generation).<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Authentication:</b> Requires user JWT token (proxied from main API) or scoped service token<br><br>

<b>Features:</b><br>
<ul>
<li>Multi-turn conversation support</li>
<li>Context from knowledge base</li>
<li>Citation of source documents</li>
<li>Multiple chat modes (quick, analysis, deep_research, creative, precise)</li>
<li>Multi-model support (OpenAI, Anthropic, Ollama, etc.)</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="queryServiceChat" method="post" path="/query/api/v1/chat" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.query_service.chat(query="<value>", limit=50, retrieval_mode="HYBRID", quick_mode=False, chat_mode="standard")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `query`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | User's question                                                                     |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `previous_conversations`                                                            | List[[models.PreviousConversation](../../models/previousconversation.md)]           | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `filters`                                                                           | [Optional[models.QueryServiceChatFilters]](../../models/queryservicechatfilters.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retrieval_mode`                                                                    | [Optional[models.RetrievalMode]](../../models/retrievalmode.md)                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `quick_mode`                                                                        | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `model_key`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | UUID of the model configuration                                                     |
| `model_name`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Model name (e.g., gpt-4o-mini, claude-3-5-sonnet)                                   |
| `chat_mode`                                                                         | [Optional[models.ChatMode]](../../models/chatmode.md)                               | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |
| `server_url`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | An optional server URL to use.                                                      |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## chat_stream

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Streaming conversational AI endpoint with real-time token delivery.<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Authentication:</b> Requires user JWT token (proxied from main API) or scoped service token<br><br>

<b>SSE Events:</b><br>
<ul>
<li><code>status</code>: Processing status updates</li>
<li><code>chunk</code>: Token/text chunks</li>
<li><code>citations</code>: Source citations</li>
<li><code>done</code>: Stream complete</li>
<li><code>error</code>: Error occurred</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="queryServiceChatStream" method="post" path="/query/api/v1/chat/stream" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.query_service.chat_stream()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## health_check

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Validate LLM or embedding model configuration.<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Authentication:</b> Requires scoped service token<br><br>

<b>Model Types:</b>
<ul>
<li><code>llm</code> - Test LLM configuration (text generation)</li>
<li><code>embedding</code> - Test embedding model configuration</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="queryServiceHealthCheck" method="post" path="/query/api/v1/health-check/{model_type}" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.query_service.health_check(security=models.QueryServiceHealthCheckSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), model_type="llm", provider="<value>", configuration={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.QueryServiceHealthCheckSecurity](../../models/queryservicehealthchecksecurity.md)           | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `model_type`                                                                                        | [models.QueryServiceHealthCheckModelType](../../models/queryservicehealthcheckmodeltype.md)         | :heavy_check_mark:                                                                                  | Type of model to health check                                                                       |
| `provider`                                                                                          | *str*                                                                                               | :heavy_check_mark:                                                                                  | Model provider (openai, anthropic, ollama, etc.)                                                    |
| `configuration`                                                                                     | [models.QueryServiceHealthCheckConfiguration](../../models/queryservicehealthcheckconfiguration.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `is_multimodal`                                                                                     | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether model supports vision/images                                                                |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |
| `server_url`                                                                                        | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | An optional server URL to use.                                                                      |

### Response

**[models.QueryServiceHealthCheckResponse](../../models/queryservicehealthcheckresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.QueryServiceHealthCheckInternalServerError | 500                                               | application/json                                  |
| errors.PipeshubDefaultError                       | 4XX, 5XX                                          | \*/\*                                             |

## list_tools

Retrieve all available tools that can be used by AI agents.<br><br>

<b>Service:</b> Query Service<br>
<b>Port:</b> 8000<br>
<b>Base URL:</b> <code>http://localhost:8000</code><br><br>

<b>Overview:</b><br>
Returns a list of tools registered in the system, including their parameters,
descriptions, and tags. Tools are loaded from ArangoDB.<br><br>

<b>Use Cases:</b><br>
<ul>
<li>Agent configuration UI - show available tools to assign to agents</li>
<li>Tool discovery for building custom agent workflows</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="queryListTools" method="get" path="/query/api/v1/tools" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.query_service.list_tools()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[List[models.QueryListToolsResponse]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |