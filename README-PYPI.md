# PipesHub Python SDK

[![PyPI version](https://img.shields.io/pypi/v/pipeshub-sdk.svg)](https://pypi.org/project/pipeshub-sdk/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://pypi.org/project/pipeshub-sdk/)
[![License](https://img.shields.io/github/license/pipeshub-ai/pipeshub-sdk-python.svg)](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/main/LICENSE)

This is the official Python SDK for [PipesHub](https://pipeshub.com). Search your company's knowledge and get answers with citations, run agents, and manage knowledge bases and connectors, all from your Python code.

PipesHub connects workplace apps such as Google Drive, Slack, Confluence and Jira and indexes their content. The SDK supports Python 3.10 and later, has type hints for every request and response, and offers both synchronous and asynchronous clients.

## Documentation

- [API reference](https://docs.pipeshub.com/developer/api-reference): the PipesHub HTTP API.
- [Available methods](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#available-resources-and-operations): every SDK method, linked to its parameters, response and errors.
- [Examples](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/examples/): runnable programs for search, chat, agents, knowledge bases and connectors.

The client signs in with a [personal access token](https://docs.pipeshub.com/developer/personal-access-tokens) and connects to PipesHub Cloud (`https://app.pipeshub.com`) by default. For a self-hosted instance, pass `server_url="https://<your-instance>/api/v1"` (see [Server Selection](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#server-selection)).

<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [PipesHub Python SDK](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#pipeshub-python-sdk)
  * [Documentation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#documentation)
  * [SDK Installation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#sdk-installation)
  * [SDK Example Usage](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#sdk-example-usage)
  * [Retrieval for RAG and agent frameworks](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#retrieval-for-rag-and-agent-frameworks)
  * [Authentication](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#authentication)
  * [Server-sent event streaming](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#server-sent-event-streaming)
  * [File uploads](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#file-uploads)
  * [Retries](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#resource-management)
  * [Debugging](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#debugging)
  * [IDE Support](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#ide-support)
  * [Available Resources and Operations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#available-resources-and-operations)
  * [Support](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#support)
  * [Contributing](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#contributing)
  * [License](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#license)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add pipeshub-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install pipeshub-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add pipeshub-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from pipeshub-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pipeshub-sdk",
# ]
# ///

from pipeshub_sdk import Pipeshub

sdk = Pipeshub(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Retrieve passages with citations

```python
# Synchronous Example
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.retrieve(query="how do we roll back a canary?", limit=8, rewrite_query=False)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os
from pipeshub_sdk import Pipeshub, models

async def main():

    async with Pipeshub(
        security=models.Security(
            bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
        ),
    ) as pipeshub:

        res = await pipeshub.semantic_search.retrieve_async(query="how do we roll back a canary?", limit=8, rewrite_query=False)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

## Retrieval for RAG and agent frameworks

`semantic_search.retrieve` returns permission-filtered passages ("chunks"), each with its record and a citation link. It stores no search history, so you can call it on every request your application serves. See the [Retrieval API](https://docs.pipeshub.com/developer/retrieval-api) docs.

Ready-made retrievers ship as extras:

```bash
pip install "pipeshub-sdk[langchain]"    # pipeshub_sdk.integrations.langchain.PipesHubRetriever
pip install "pipeshub-sdk[llamaindex]"   # pipeshub_sdk.integrations.llamaindex.PipesHubRetriever
```

```python
from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.integrations.langchain import PipesHubRetriever

with Pipeshub(server_url="https://your-pipeshub-instance.com/api/v1",
              security=models.Security(bearer_auth="phpat_...")) as client:
    docs = PipesHubRetriever(client=client, limit=5).invoke("How do we roll back a canary deploy?")
```

Each result carries the chunk text and, in its metadata, the record (`recordId`, `name`, `connector`, `mimeType`, `updatedAt`), the citation (`url`, `recordUrl`, `pageNum`, `blockIndex`) and `score`. Both retrievers take `limit`, `filters`, `max_chunks_per_record` and `rewrite_query`, and support async. Examples: [`examples/retrievers/`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/examples/retrievers/).

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type   | Scheme       | Environment Variable   |
| ------------- | ------ | ------------ | ---------------------- |
| `bearer_auth` | http   | HTTP Bearer  | `PIPESHUB_BEARER_AUTH` |
| `oauth2`      | oauth2 | OAuth2 token | `PIPESHUB_OAUTH2`      |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.refresh_token(security=models.RefreshTokenSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ))

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.upload_records(kb_id="<id>", files=[], files_metadata=[
        {
            "file_path": "/docs/report.pdf",
            "last_modified": 2024.0,
        },
    ], is_versioned="true", record_type="FILE")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.knowledge_base.update_record_multipart(record_id="<id>")

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from pipeshub_sdk import Pipeshub
from pipeshub_sdk.utils import BackoffStrategy, RetryConfig


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from pipeshub_sdk import Pipeshub
from pipeshub_sdk.utils import BackoffStrategy, RetryConfig


with Pipeshub(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`PipeshubError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/pipeshuberror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#error-classes). |

### Example
```python
from pipeshub_sdk import Pipeshub, errors


with Pipeshub() as pipeshub:
    res = None
    try:

        res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

        # Handle response
        print(res)


    except errors.PipeshubError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorResponse):
            print(e.data.error)  # models.ErrorResponseError
```

### Error Classes
**Primary errors:**
* [`PipeshubError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/pipeshuberror.py): The base class for HTTP error responses.
  * [`ErrorResponse`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/errorresponse.py): Standard error envelope returned by all errors routed through `ErrorMiddleware`. Applies to all `BaseError` subclasses including `HttpError`, `ValidationError`, and others. The `code` field is a machine-readable string identifying the error type (e.g. `HTTP_UNAUTHORIZED`, `HTTP_NOT_FOUND`, `VALIDATION_ERROR`, `INTERNAL_ERROR`). *

<details><summary>Less common errors (21)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`PipeshubError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/pipeshuberror.py)**:
* [`OAuthClientManagementRateLimitError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/oauthclientmanagementratelimiterror.py): JSON body when OAuth client management routes exceed the per-minute rate limit (same limiter as other `/oauth-clients/*` routes). Status code `429`. Applicable to 20 of 141 methods.*
* [`ApplicationJSONErrorResponse`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/applicationjsonerrorresponse.py): Standard JSON error envelope from `ErrorMiddleware` for `BaseError` subclasses (`error.middleware.ts`). Returned for most API 4xx errors (unauthorized, forbidden, not found, validation failures, etc.). Applicable to 17 of 141 methods.*
* [`OAuthErrorResponse`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/oautherrorresponse.py): OAuth 2.0 Error Response (RFC 6749 Section 5.2). Standard error format for OAuth endpoints. Applicable to 3 of 141 methods.*
* [`RateLimitErrorResponse`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/ratelimiterrorresponse.py): Rate-limit error payload (shape differs from standard error responses). Status code `429`. Applicable to 3 of 141 methods.*
* [`LocalFsDesktopRefusalError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/localfsdesktoprefusalerror.py): 409 body returned when a Local FS connector cannot sync because of its owner device. Status code `409`. Applicable to 2 of 141 methods.*
* [`BadRequestError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/badrequesterror.py): Error envelope for a failed request. Status code `400`. Applicable to 1 of 141 methods.*
* [`UnauthorizedError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/unauthorizederror.py): Error envelope for a failed request. Status code `401`. Applicable to 1 of 141 methods.*
* [`OAuthBearerTokenError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/oauthbearertokenerror.py): Error body written by the OAuth bearer-token middleware (RFC 6750 Section 3.1) on routes that accept only an OAuth access token, such as `GET /oauth2/userinfo`. The same `error`, `error_description` and `scope` values are repeated in the `WWW-Authenticate` response header. This is not the standard `ErrorResponse` envelope: `error` is a string. Applicable to 1 of 141 methods.*
* [`ForbiddenError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/forbiddenerror.py): Error envelope for a failed request. Status code `403`. Applicable to 1 of 141 methods.*
* [`StreamRecordErrorResponse`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/streamrecorderrorresponse.py): Error payload returned by the legacy record-stream proxy when the downstream streaming request fails after route middleware has passed. Applicable to 1 of 141 methods.*
* [`GetKnowledgeHubRootNodesUnprocessableEntityError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/getknowledgehubrootnodesunprocessableentityerror.py): Either of: - A typed query parameter could not be read: `page` or `limit` is not an   integer or is out of range (`page` below 1, `limit` outside 1-200),   `onlyContainers` or `flattened` is not a boolean, or `page`/`limit` was   sent more than once. `error.message` is the connector service's own   validation text. - A listing that spans a whole connector (a flattened listing, a search or a filter) was too large for the   database to hold in memory, so it was refused instead of cut short. No page is returned. Open a folder   (`GET /knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}`) to see its records, or add a search (`q`),   which keeps only matching records in memory. Choosing a connector, or a filter that keeps most records (such as   `nodeTypes`), does not help. Sorting by name with no filters is served from stored visibility where the   connector allows it and is not affected. Status code `422`. Applicable to 1 of 141 methods.*
* [`GetKnowledgeHubChildNodesUnprocessableEntityError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/getknowledgehubchildnodesunprocessableentityerror.py): Either of: - A typed query parameter could not be read: `page` or `limit` is not an   integer or is out of range (`page` below 1, `limit` outside 1-200), or   `onlyContainers` or `flattened` is not a boolean. `error.message` is the   connector service's own validation text. - A listing that spans a whole connector (a flattened listing, a search or a filter) was too large for the   database to hold in memory, so it was refused instead of cut short. No page is returned. Open a folder   (`GET /knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}`) to see its records, or add a search (`q`),   which keeps only matching records in memory. Choosing a connector, or a filter that keeps most records (such as   `nodeTypes`), does not help. Sorting by name with no filters is served from stored visibility where the   connector allows it and is not affected. Status code `422`. Applicable to 1 of 141 methods.*
* [`UploadAgentConversationChatAttachmentsUnprocessableEntityError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/uploadagentconversationchatattachmentsunprocessableentityerror.py): A PDF that could not be read within the upload's 50-second budget, or whose parse ran out of memory, is not attached (`<name> is too large or complex to read right now, so it wasn't attached. ...`). Only that upload fails. Status code `422`. Applicable to 1 of 141 methods.*
* [`SearchHistoryInternalServerError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/searchhistoryinternalservererror.py): Error envelope for a failed request. Status code `500`. Applicable to 1 of 141 methods.*
* [`GetKnowledgeHubRootNodesServiceUnavailableError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/getknowledgehubrootnodesserviceunavailableerror.py): The database could not give this listing the memory it needs right now, because other requests were using it (nothing is wrong with the request). Retry after `Retry-After` seconds; the web app retries by itself. The body is the gateway's own busy message, not the service's wording. Status code `503`. Applicable to 1 of 141 methods.*
* [`GetKnowledgeHubChildNodesServiceUnavailableError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/getknowledgehubchildnodesserviceunavailableerror.py): The database could not give this listing the memory it needs right now, because other requests were using it (nothing is wrong with the request). Retry after `Retry-After` seconds; the web app retries by itself. The body is the gateway's own busy message, not the service's wording. Status code `503`. Applicable to 1 of 141 methods.*
* [`ResponseValidationError`](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/./src/pipeshub_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                          | Variables      | Description                                       |
| --- | ------------------------------- | -------------- | ------------------------------------------------- |
| 0   | `https://{instance_url}/api/v1` | `instance_url` | Base API URL                                      |
| 1   | `https://{instance_url}`        | `instance_url` | Root URL (used for MCP endpoints mounted at /mcp) |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable       | Parameter           | Default              | Description                                                                                                                                                  |
| -------------- | ------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `instance_url` | `instance_url: str` | `"app.pipeshub.com"` | Host name, with an optional port, of a PipesHub instance served over HTTPS. For a plain-HTTP instance, such as a local one, set the full server URL instead. |

#### Example

```python
from pipeshub_sdk import Pipeshub


with Pipeshub(
    server_idx=0,
    instance_url="app.pipeshub.com",
) as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from pipeshub_sdk import Pipeshub


with Pipeshub(
    server_url="https://app.pipeshub.com",
) as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from pipeshub_sdk import Pipeshub
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Pipeshub(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from pipeshub_sdk import Pipeshub
from pipeshub_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Pipeshub(async_client=CustomClient(httpx.AsyncClient()))
```
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from pipeshub_sdk import Pipeshub

s = Pipeshub()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Pipeshub` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from pipeshub_sdk import Pipeshub, models
def main():

    with Pipeshub(
        security=models.Security(
            bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
        ),
    ) as pipeshub:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Pipeshub(
        security=models.Security(
            bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
        ),
    ) as pipeshub:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from pipeshub_sdk import Pipeshub
import logging

logging.basicConfig(level=logging.DEBUG)
s = Pipeshub(debug_logger=logging.getLogger("pipeshub_sdk"))
```

You can also enable a default debug logger by setting an environment variable `PIPESHUB_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md)

* [list_agents](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#list_agents) - List agents
* [create_agent](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#create_agent) - Create agent
* [get_agent](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#get_agent) - Get agent
* [update_agent](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#update_agent) - Update agent
* [delete_agent](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#delete_agent) - Delete agent
* [list_agent_archived_conversations_grouped](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#list_agent_archived_conversations_grouped) - List archived agent conversations grouped by agent
* [list_agent_conversation_archives](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#list_agent_conversation_archives) - List archived conversations for an agent
* [upload_agent_conversation_chat_attachments](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#upload_agent_conversation_chat_attachments) - Upload agent chat attachments
* [delete_agent_conversation_chat_attachment](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#delete_agent_conversation_chat_attachment) - Delete an agent chat attachment
* [stream_agent_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#stream_agent_conversation) - Create agent conversation with streaming response
* [stream_agent_conversation_message](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#stream_agent_conversation_message) - Add message to agent conversation with streaming response
* [regenerate_agent_conversation_message](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#regenerate_agent_conversation_message) - Regenerate agent conversation message
* [fork_agent_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#fork_agent_conversation) - Fork agent conversation from a message
* [cancel_agent_conversation_stream](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#cancel_agent_conversation_stream) - Cancel an in-flight agent chat stream
* [update_agent_conversation_message_feedback](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#update_agent_conversation_message_feedback) - Submit feedback for an agent message
* [add_agent_conversation_message](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#add_agent_conversation_message) - Add message to agent conversation (non-streaming)
* [archive_agent_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#archive_agent_conversation) - Archive an agent conversation
* [unarchive_agent_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#unarchive_agent_conversation) - Unarchive an agent conversation
* [update_agent_conversation_title](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#update_agent_conversation_title) - Update agent conversation title
* [delete_agent_conversation_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#delete_agent_conversation_by_id) - Delete an agent conversation
* [get_agent_conversation_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#get_agent_conversation_by_id) - Get agent conversation by ID
* [list_agent_conversations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#list_agent_conversations) - List agent conversations
* [create_agent_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/agents/README.md#create_agent_conversation) - Create agent conversation (non-streaming)

### [AIModelsProviders](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/aimodelsproviders/README.md)

* [get_available_models_by_type](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/aimodelsproviders/README.md#get_available_models_by_type) - Get available models by type

### [Connector](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connector/README.md)

* [get_record_content](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connector/README.md#get_record_content) - Get a record's full parsed content and metadata
* [navigate_knowledge_graph](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connector/README.md#navigate_knowledge_graph) - Browse the knowledge graph from a node
* [lookup_record_by_identifier](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connector/README.md#lookup_record_by_identifier) - Resolve a URL, issue key or external ID to a Record ID

### [ConnectorConfiguration](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorconfiguration/README.md)

* [get_connector_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorconfiguration/README.md#get_connector_config) - Get connector configuration
* [update_connector_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorconfiguration/README.md#update_connector_config) - Update connector configuration
* [update_connector_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorconfiguration/README.md#update_connector_auth_config) - Update authentication configuration
* [update_connector_filters_sync_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorconfiguration/README.md#update_connector_filters_sync_config) - Update filters and sync configuration

### [ConnectorControl](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorcontrol/README.md)

* [toggle_connector](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorcontrol/README.md#toggle_connector) - Toggle connector sync or agent

### [ConnectorFilters](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorfilters/README.md)

* [get_connector_filters](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorfilters/README.md#get_connector_filters) - Get filter options
* [~~save_connector_filters~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorfilters/README.md#save_connector_filters) - Save filter selections (deprecated) :warning: **Deprecated**
* [get_filter_field_options](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorfilters/README.md#get_filter_field_options) - Get dynamic filter options

### [ConnectorInstances](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md)

* [list_connector_instances](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#list_connector_instances) - List connector instances
* [create_connector_instance](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#create_connector_instance) - Create connector instance
* [get_connector_instance](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#get_connector_instance) - Get connector instance
* [delete_connector_instance](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#delete_connector_instance) - Delete connector instance
* [get_connector_stats](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#get_connector_stats) - Get connector statistics
* [resync_connector](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#resync_connector) - Resync connector
* [stop_connector_sync](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorinstances/README.md#stop_connector_sync) - Stop the running sync for a connector

### [ConnectorOAuth](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectoroauth/README.md)

* [get_o_auth_authorization_url](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectoroauth/README.md#get_o_auth_authorization_url) - Get OAuth authorization URL
* [handle_o_auth_callback](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectoroauth/README.md#handle_o_auth_callback) - OAuth callback handler

### [ConnectorRegistry](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorregistry/README.md)

* [get_connector_registry](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorregistry/README.md#get_connector_registry) - List available connector types
* [get_connector_schema](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorregistry/README.md#get_connector_schema) - Get connector configuration schema
* [test_connector_connection](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorregistry/README.md#test_connector_connection) - Test connector credentials before saving
* [get_connector_egress_ips](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/connectorregistry/README.md#get_connector_egress_ips) - Get the IP addresses connectors connect from

### [Conversations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md)

* [create_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#create_conversation) - Create conversation (non-streaming)
* [stream_chat](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#stream_chat) - Create conversation with streaming response
* [get_all_conversations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#get_all_conversations) - List all conversations
* [get_archived_conversations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#get_archived_conversations) - List archived conversations
* [search_archived_conversations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#search_archived_conversations) - Search archived conversations
* [get_conversation_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#get_conversation_by_id) - Get conversation by ID
* [delete_conversation_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#delete_conversation_by_id) - Delete conversation
* [add_message](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#add_message) - Add message (non-streaming)
* [add_message_stream](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#add_message_stream) - Add message to a conversation with streaming response
* [update_conversation_title](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#update_conversation_title) - Update conversation title
* [archive_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#archive_conversation) - Archive conversation
* [unarchive_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#unarchive_conversation) - Unarchive conversation
* [pin_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#pin_conversation) - Pin conversation
* [unpin_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#unpin_conversation) - Unpin conversation
* [regenerate_answer](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#regenerate_answer) - Regenerate AI response
* [fork_conversation](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#fork_conversation) - Fork conversation from a message
* [cancel_conversation_stream](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#cancel_conversation_stream) - Cancel an in-flight chat stream
* [update_message_feedback](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/conversations/README.md#update_message_feedback) - Submit feedback on AI response

### [KnowledgeBase](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md)

* [create_knowledge_base](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#create_knowledge_base) - Create a new knowledge base
* [list_knowledge_bases](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#list_knowledge_bases) - List all knowledge bases
* [get_knowledge_base](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#get_knowledge_base) - Get knowledge base by ID
* [update_knowledge_base](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#update_knowledge_base) - Update knowledge base
* [delete_knowledge_base](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#delete_knowledge_base) - Delete knowledge base
* [get_record_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#get_record_by_id) - Get record by ID
* [update_record_multipart](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#update_record_multipart) - Update record
* [update_record](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#update_record) - Update record
* [update_record_form](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#update_record_form) - Update record
* [delete_record](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#delete_record) - Delete record
* [restore_record](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#restore_record) - Restore a deleted record
* [restore_records](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#restore_records) - Restore several deleted records
* [list_trash](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#list_trash) - List a collection's recently deleted items
* [stream_record_buffer](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#stream_record_buffer) - Stream record content
* [create_folder](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#create_folder) - Create folder
* [create_subfolder](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#create_subfolder) - Create subfolder
* [update_folder](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#update_folder) - Update folder
* [delete_folder](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#delete_folder) - Delete folder
* [upload_records](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#upload_records) - Upload files to knowledge base or folder
* [get_upload_limits](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#get_upload_limits) - Get knowledge base upload limits
* [reindex_record](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#reindex_record) - Reindex single record
* [reindex_record_group](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#reindex_record_group) - Reindex record group
* [move_record](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#move_record) - Move record to another location
* [~~get_knowledge_hub_root_nodes~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes :warning: **Deprecated**
* [~~get_knowledge_hub_child_nodes~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgebasesdk/README.md#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes :warning: **Deprecated**

### [~~KnowledgeHub~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgehub/README.md)

* [~~get_knowledge_hub_root_nodes~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgehub/README.md#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes :warning: **Deprecated**
* [~~get_knowledge_hub_child_nodes~~](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/knowledgehub/README.md#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes :warning: **Deprecated**

### [OAuthApps](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md)

* [list_o_auth_apps](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#list_o_auth_apps) - List OAuth apps
* [create_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#create_o_auth_app) - Create OAuth app
* [list_o_auth_scopes](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#list_o_auth_scopes) - List available scopes
* [get_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#get_o_auth_app) - Get OAuth app details
* [update_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#update_o_auth_app) - Update OAuth app
* [delete_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#delete_o_auth_app) - Delete OAuth app
* [regenerate_o_auth_app_secret](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#regenerate_o_auth_app_secret) - Regenerate client secret
* [suspend_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#suspend_o_auth_app) - Suspend OAuth app
* [activate_o_auth_app](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#activate_o_auth_app) - Activate suspended OAuth app
* [list_o_auth_app_tokens](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#list_o_auth_app_tokens) - List app tokens
* [revoke_all_o_auth_app_tokens](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthapps/README.md#revoke_all_o_auth_app_tokens) - Revoke all app tokens

### [OAuthConfiguration](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md)

* [get_o_auth_registry](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#get_o_auth_registry) - List OAuth-capable connector types
* [get_o_auth_connector_type](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#get_o_auth_connector_type) - Get OAuth connector type details
* [list_o_auth_configs](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#list_o_auth_configs) - List OAuth configurations
* [list_o_auth_configs_by_type](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#list_o_auth_configs_by_type) - List OAuth configs for connector type
* [create_o_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#create_o_auth_config) - Create OAuth configuration
* [get_o_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#get_o_auth_config) - Get OAuth configuration
* [update_o_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#update_o_auth_config) - Update OAuth configuration
* [delete_o_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthconfiguration/README.md#delete_o_auth_config) - Delete OAuth configuration

### [OAuthProvider](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthprovider/README.md)

* [oauth_token](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthprovider/README.md#oauth_token) - Exchange authorization code for tokens
* [oauth_revoke](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthprovider/README.md#oauth_revoke) - Revoke an access or refresh token
* [oauth_introspect](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/oauthprovider/README.md#oauth_introspect) - Introspect a token

### [OpenIDConnect](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/openidconnect/README.md)

* [oauth_user_info](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/openidconnect/README.md#oauth_user_info) - Get authenticated user information

### [OrganizationAuthConfig](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizationauthconfig/README.md)

* [get_auth_methods](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizationauthconfig/README.md#get_auth_methods) - Get organization authentication methods
* [update_auth_method](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizationauthconfig/README.md#update_auth_method) - Update organization authentication methods
* [set_up_auth_config](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizationauthconfig/README.md#set_up_auth_config) - Set up auth configuration

### [Organizations](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizations/README.md)

* [get_current_organization](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/organizations/README.md#get_current_organization) - Get current organization

### [PersonalAccessTokens](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md)

* [list_personal_access_tokens](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#list_personal_access_tokens) - List your own personal access tokens
* [create_personal_access_token](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#create_personal_access_token) - Create a personal access token
* [list_personal_access_token_scopes](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#list_personal_access_token_scopes) - List scopes available for a new personal access token
* [revoke_personal_access_token](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#revoke_personal_access_token) - Revoke one of your own personal access tokens
* [admin_list_personal_access_tokens](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#admin_list_personal_access_tokens) - Admin: list every active personal access token in the org
* [admin_revoke_personal_access_token](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/personalaccesstokens/README.md#admin_revoke_personal_access_token) - Admin: revoke any user's personal access token by id

### [SemanticSearch](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md)

* [retrieve](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#retrieve) - Retrieve chunks with citations
* [search](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#search) - Perform semantic search
* [search_history](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#search_history) - Get search history
* [delete_search_history](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#delete_search_history) - Clear all search history
* [get_search_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#get_search_by_id) - Get search by ID
* [delete_search_by_id](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#delete_search_by_id) - Delete search by ID
* [archive_search](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#archive_search) - Archive a search
* [unarchive_search](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/semanticsearch/README.md#unarchive_search) - Unarchive a search

### [UserAccount](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md)

* [init_auth](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#init_auth) - Initialize authentication session
* [authenticate](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#authenticate) - Authenticate user with credentials
* [refresh_token](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#refresh_token) - Refresh access token
* [get_password_status](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#get_password_status) - Get password status
* [send_password_setup_email](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#send_password_setup_email) - Email a link to set a first password
* [reset_password](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/useraccount/README.md#reset_password) - Reset password

### [WebSearch](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/websearchsdk/README.md)

* [get_web_search_providers](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/docs/sdks/websearchsdk/README.md#get_web_search_providers) - Get all web search providers

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

## Support

- Bugs and feature requests: [open an issue](https://github.com/pipeshub-ai/pipeshub-sdk-python/issues).
- Questions: the [PipesHub Discord](https://discord.com/invite/K5RskzJBm2).
- PipesHub itself: [pipeshub-ai/pipeshub-ai](https://github.com/pipeshub-ai/pipeshub-ai).

## Contributing

Most of this SDK is generated, so direct changes to generated files are overwritten by the next release. Please open an issue instead. See [CONTRIBUTING.md](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/CONTRIBUTING.md).

## License

Licensed under the [Apache License 2.0](https://github.com/pipeshub-ai/pipeshub-sdk-python/blob/master/LICENSE).
