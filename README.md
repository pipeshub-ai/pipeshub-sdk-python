# pipeshub-sdk
pipeshub-sdk is the official python client library for integrating Pipeshub into your product and internal tools

<!-- Start Summary [summary] -->
## Summary

PipesHub API: Unified API documentation for PipesHub services.

PipesHub is an enterprise-grade platform providing:
- User authentication and management
- Document storage and version control
- Knowledge base management
- Enterprise search and conversational AI
- Third-party integrations via connectors
- System configuration management
- Crawling job scheduling
- Email services

## Authentication
Most endpoints require JWT Bearer token authentication. Some internal endpoints use scoped tokens for service-to-service communication.

**OAuth 2.0 Bearer tokens** from `POST /oauth2/token` use the same `Authorization: Bearer` header. For **`client_credentials`**, machine tokens may encode `userId === client_id` in the JWT; the **Node API gateway** resolves the OAuth **app creator**, sets the authenticated user accordingly, and forwards **`x-oauth-user-id`** to Python services on proxied calls. Do not send **`x-oauth-user-id`** yourself—the gateway removes untrusted values on ingress. See the **OAuth Provider** tag for full behavior.

## Base URLs
All endpoints use the `/api/v1` prefix unless otherwise noted.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [pipeshub-sdk](#pipeshub-sdk)
  * [Authentication](#authentication)
  * [Base URLs](#base-urls)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

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

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from pipeshub_sdk import Pipeshub

async def main():

    async with Pipeshub() as pipeshub:

        res = await pipeshub.o_auth_provider.oauth_token_async(grant_type="client_credentials")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](docs/sdks/agents/README.md)

* [list_agents](docs/sdks/agents/README.md#list_agents) - List agents
* [create_agent](docs/sdks/agents/README.md#create_agent) - Create agent
* [get_agent](docs/sdks/agents/README.md#get_agent) - Get agent
* [update_agent](docs/sdks/agents/README.md#update_agent) - Update agent
* [delete_agent](docs/sdks/agents/README.md#delete_agent) - Delete agent
* [list_agent_archived_conversations_grouped](docs/sdks/agents/README.md#list_agent_archived_conversations_grouped) - List archived agent conversations grouped by agent
* [list_agent_conversation_archives](docs/sdks/agents/README.md#list_agent_conversation_archives) - List archived conversations for an agent
* [upload_agent_conversation_chat_attachments](docs/sdks/agents/README.md#upload_agent_conversation_chat_attachments) - Upload agent chat attachments
* [delete_agent_conversation_chat_attachment](docs/sdks/agents/README.md#delete_agent_conversation_chat_attachment) - Delete an agent chat attachment
* [stream_agent_conversation](docs/sdks/agents/README.md#stream_agent_conversation) - Create agent conversation with streaming response
* [stream_agent_conversation_message](docs/sdks/agents/README.md#stream_agent_conversation_message) - Add message to agent conversation with streaming response
* [regenerate_agent_conversation_message](docs/sdks/agents/README.md#regenerate_agent_conversation_message) - Regenerate agent conversation message
* [update_agent_conversation_message_feedback](docs/sdks/agents/README.md#update_agent_conversation_message_feedback) - Submit feedback for an agent message
* [archive_agent_conversation](docs/sdks/agents/README.md#archive_agent_conversation) - Archive an agent conversation
* [unarchive_agent_conversation](docs/sdks/agents/README.md#unarchive_agent_conversation) - Unarchive an agent conversation
* [update_agent_conversation_title](docs/sdks/agents/README.md#update_agent_conversation_title) - Update agent conversation title
* [delete_agent_conversation_by_id](docs/sdks/agents/README.md#delete_agent_conversation_by_id) - Delete an agent conversation
* [get_agent_conversation_by_id](docs/sdks/agents/README.md#get_agent_conversation_by_id) - Get agent conversation by ID
* [list_agent_conversations](docs/sdks/agents/README.md#list_agent_conversations) - List agent conversations

### [AIModelsProviders](docs/sdks/aimodelsproviders/README.md)

* [get_available_models_by_type](docs/sdks/aimodelsproviders/README.md#get_available_models_by_type) - Get available models by type

### [Conversations](docs/sdks/conversations/README.md)

* [stream_chat](docs/sdks/conversations/README.md#stream_chat) - Create conversation with streaming response
* [get_all_conversations](docs/sdks/conversations/README.md#get_all_conversations) - List all conversations
* [get_archived_conversations](docs/sdks/conversations/README.md#get_archived_conversations) - List archived conversations
* [search_archived_conversations](docs/sdks/conversations/README.md#search_archived_conversations) - Search archived conversations
* [get_conversation_by_id](docs/sdks/conversations/README.md#get_conversation_by_id) - Get conversation by ID
* [delete_conversation_by_id](docs/sdks/conversations/README.md#delete_conversation_by_id) - Delete conversation
* [add_message_stream](docs/sdks/conversations/README.md#add_message_stream) - Add message to a conversation with streaming response
* [update_conversation_title](docs/sdks/conversations/README.md#update_conversation_title) - Update conversation title
* [archive_conversation](docs/sdks/conversations/README.md#archive_conversation) - Archive conversation
* [unarchive_conversation](docs/sdks/conversations/README.md#unarchive_conversation) - Unarchive conversation
* [regenerate_answer](docs/sdks/conversations/README.md#regenerate_answer) - Regenerate AI response
* [update_message_feedback](docs/sdks/conversations/README.md#update_message_feedback) - Submit feedback on AI response

### [KnowledgeHub](docs/sdks/knowledgehub/README.md)

* [get_knowledge_hub_root_nodes](docs/sdks/knowledgehub/README.md#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes
* [get_knowledge_hub_child_nodes](docs/sdks/knowledgehub/README.md#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes

### [OAuthApps](docs/sdks/oauthapps/README.md)

* [list_o_auth_apps](docs/sdks/oauthapps/README.md#list_o_auth_apps) - List OAuth apps
* [create_o_auth_app](docs/sdks/oauthapps/README.md#create_o_auth_app) - Create OAuth app
* [list_o_auth_scopes](docs/sdks/oauthapps/README.md#list_o_auth_scopes) - List available scopes
* [get_o_auth_app](docs/sdks/oauthapps/README.md#get_o_auth_app) - Get OAuth app details
* [update_o_auth_app](docs/sdks/oauthapps/README.md#update_o_auth_app) - Update OAuth app
* [delete_o_auth_app](docs/sdks/oauthapps/README.md#delete_o_auth_app) - Delete OAuth app
* [regenerate_o_auth_app_secret](docs/sdks/oauthapps/README.md#regenerate_o_auth_app_secret) - Regenerate client secret
* [suspend_o_auth_app](docs/sdks/oauthapps/README.md#suspend_o_auth_app) - Suspend OAuth app
* [activate_o_auth_app](docs/sdks/oauthapps/README.md#activate_o_auth_app) - Activate suspended OAuth app
* [list_o_auth_app_tokens](docs/sdks/oauthapps/README.md#list_o_auth_app_tokens) - List app tokens
* [revoke_all_o_auth_app_tokens](docs/sdks/oauthapps/README.md#revoke_all_o_auth_app_tokens) - Revoke all app tokens

### [OAuthProvider](docs/sdks/oauthprovider/README.md)

* [oauth_token](docs/sdks/oauthprovider/README.md#oauth_token) - Exchange authorization code for tokens
* [oauth_revoke](docs/sdks/oauthprovider/README.md#oauth_revoke) - Revoke an access or refresh token
* [oauth_introspect](docs/sdks/oauthprovider/README.md#oauth_introspect) - Introspect a token

### [OpenIDConnect](docs/sdks/openidconnect/README.md)

* [oauth_user_info](docs/sdks/openidconnect/README.md#oauth_user_info) - Get authenticated user information

### [OrganizationAuthConfig](docs/sdks/organizationauthconfig/README.md)

* [get_auth_methods](docs/sdks/organizationauthconfig/README.md#get_auth_methods) - Get organization authentication methods
* [update_auth_method](docs/sdks/organizationauthconfig/README.md#update_auth_method) - Update organization authentication methods
* [set_up_auth_config](docs/sdks/organizationauthconfig/README.md#set_up_auth_config) - Set up auth configuration

### [Organizations](docs/sdks/organizations/README.md)

* [get_current_organization](docs/sdks/organizations/README.md#get_current_organization) - Get current organization

### [SemanticSearch](docs/sdks/semanticsearch/README.md)

* [search](docs/sdks/semanticsearch/README.md#search) - Perform semantic search
* [search_history](docs/sdks/semanticsearch/README.md#search_history) - Get search history
* [delete_search_history](docs/sdks/semanticsearch/README.md#delete_search_history) - Clear all search history
* [get_search_by_id](docs/sdks/semanticsearch/README.md#get_search_by_id) - Get search by ID
* [delete_search_by_id](docs/sdks/semanticsearch/README.md#delete_search_by_id) - Delete search by ID
* [archive_search](docs/sdks/semanticsearch/README.md#archive_search) - Archive a search
* [unarchive_search](docs/sdks/semanticsearch/README.md#unarchive_search) - Unarchive a search

### [UserAccount](docs/sdks/useraccount/README.md)

* [init_auth](docs/sdks/useraccount/README.md#init_auth) - Initialize authentication session
* [authenticate](docs/sdks/useraccount/README.md#authenticate) - Authenticate user with credentials
* [refresh_token](docs/sdks/useraccount/README.md#refresh_token) - Refresh access token
* [reset_password](docs/sdks/useraccount/README.md#reset_password) - Reset password

### [WebSearch](docs/sdks/websearchsdk/README.md)

* [get_web_search_providers](docs/sdks/websearchsdk/README.md#get_web_search_providers) - Get all web search providers

</details>
<!-- End Available Resources and Operations [operations] -->

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
from pipeshub_sdk.utils import parse_datetime


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.conversations.stream_chat(query="What are the key findings from our Q4 financial report?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", model_friendly_name="GPT-4 Turbo", chat_mode="web_search", timezone="America/New_York", current_time=parse_datetime("2026-04-12T16:00:00+05:30"), tools=[
        "jira.create_issue",
        "confluence.search_content",
    ])

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

    res = pipeshub.agents.upload_agent_conversation_chat_attachments(agent_key="<value>", files=[])

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

[`PipeshubError`](./src/pipeshub_sdk/errors/pipeshuberror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

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
**Primary error:**
* [`PipeshubError`](./src/pipeshub_sdk/errors/pipeshuberror.py): The base class for HTTP error responses.

<details><summary>Less common errors (32)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`PipeshubError`](./src/pipeshub_sdk/errors/pipeshuberror.py)**:
* [`ErrorResponse`](./src/pipeshub_sdk/errors/errorresponse.py): Standard error envelope returned by all errors routed through `ErrorMiddleware`. Applies to all `BaseError` subclasses including `HttpError`, `ValidationError`, and others. The `code` field is a machine-readable string identifying the error type (e.g. `HTTP_UNAUTHORIZED`, `HTTP_NOT_FOUND`, `VALIDATION_ERROR`, `INTERNAL_ERROR`). Applicable to 20 of 65 methods.*
* [`OAuthClientManagementRateLimitError`](./src/pipeshub_sdk/errors/oauthclientmanagementratelimiterror.py): JSON body when OAuth client management routes exceed the per-minute rate limit (same limiter as other `/oauth-clients/*` routes). Status code `429`. Applicable to 14 of 65 methods.*
* [`ApplicationJSONErrorResponse`](./src/pipeshub_sdk/errors/applicationjsonerrorresponse.py): Standard JSON error envelope from `ErrorMiddleware` for `BaseError` subclasses (`error.middleware.ts`). Returned for most API 4xx errors (unauthorized, forbidden, not found, validation failures, etc.). Applicable to 11 of 65 methods.*
* [`OAuthErrorResponse`](./src/pipeshub_sdk/errors/oautherrorresponse.py): OAuth 2.0 Error Response (RFC 6749 Section 5.2). Standard error format for OAuth endpoints. Status code `401`. Applicable to 3 of 65 methods.*
* [`GetKnowledgeHubRootNodesBadRequestError`](./src/pipeshub_sdk/errors/getknowledgehubrootnodesbadrequesterror.py): Invalid request parameters. The backend's validation message is returned verbatim in `error.message`. See the examples below for the common triggers. Status code `400`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubChildNodesBadRequestError`](./src/pipeshub_sdk/errors/getknowledgehubchildnodesbadrequesterror.py): Invalid request parameters or path values. The backend's validation message is returned verbatim in `error.message`. See the examples below for the common triggers. Status code `400`. Applicable to 1 of 65 methods.*
* [`SearchHistoryBadRequestError`](./src/pipeshub_sdk/errors/searchhistorybadrequesterror.py): Error envelope for a failed request. Status code `400`. Applicable to 1 of 65 methods.*
* [`GetSearchByIDBadRequestError`](./src/pipeshub_sdk/errors/getsearchbyidbadrequesterror.py): Invalid request — `searchId` failed Zod validation (not a valid ObjectId). Status code `400`. Applicable to 1 of 65 methods.*
* [`DeleteAgentConversationChatAttachmentBadRequestError`](./src/pipeshub_sdk/errors/deleteagentconversationchatattachmentbadrequesterror.py): Invalid or blank path params (`agentKey` or `recordId`). Status code `400`. Applicable to 1 of 65 methods.*
* [`GetAvailableModelsByTypeBadRequestError`](./src/pipeshub_sdk/errors/getavailablemodelsbytypebadrequesterror.py): Invalid `modelType` path parameter.  The `modelType` value was not one of the supported enum categories. This response is produced by the Zod validation middleware **before** the handler runs. The `error.metadata.errors` array contains per-field detail about exactly which constraint failed. Status code `400`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubRootNodesUnauthorizedError`](./src/pipeshub_sdk/errors/getknowledgehubrootnodesunauthorizederror.py): Missing or invalid authentication token.  The bearer token was absent, expired, malformed, or could not be verified by the auth middleware. Status code `401`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubChildNodesUnauthorizedError`](./src/pipeshub_sdk/errors/getknowledgehubchildnodesunauthorizederror.py): Missing or invalid authentication token.  The bearer token was absent, expired, malformed, or could not be verified by the auth middleware. Status code `401`. Applicable to 1 of 65 methods.*
* [`SearchHistoryUnauthorizedError`](./src/pipeshub_sdk/errors/searchhistoryunauthorizederror.py): Error envelope for a failed request. Status code `401`. Applicable to 1 of 65 methods.*
* [`GetSearchByIDUnauthorizedError`](./src/pipeshub_sdk/errors/getsearchbyidunauthorizederror.py): Missing or invalid bearer token. Status code `401`. Applicable to 1 of 65 methods.*
* [`GetAvailableModelsByTypeUnauthorizedError`](./src/pipeshub_sdk/errors/getavailablemodelsbytypeunauthorizederror.py): Missing or invalid authentication token.  The bearer token was absent, expired, malformed, or could not be verified by the auth middleware. Status code `401`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubRootNodesForbiddenError`](./src/pipeshub_sdk/errors/getknowledgehubrootnodesforbiddenerror.py): Insufficient OAuth scope.  Only applies to OAuth tokens. The token did not carry the `kb:read` scope required by this endpoint. Regular (non-OAuth) JWT bearer tokens are not subject to scope enforcement and will not receive this error. Status code `403`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubChildNodesForbiddenError`](./src/pipeshub_sdk/errors/getknowledgehubchildnodesforbiddenerror.py): Insufficient OAuth scope.  Only applies to OAuth tokens. The token did not carry the `kb:read` scope required by this endpoint. Regular (non-OAuth) JWT bearer tokens are not subject to scope enforcement and will not receive this error. Status code `403`. Applicable to 1 of 65 methods.*
* [`SearchHistoryForbiddenError`](./src/pipeshub_sdk/errors/searchhistoryforbiddenerror.py): Error envelope for a failed request. Status code `403`. Applicable to 1 of 65 methods.*
* [`GetSearchByIDForbiddenError`](./src/pipeshub_sdk/errors/getsearchbyidforbiddenerror.py): Bearer token lacks the `semantic:read` scope. Status code `403`. Applicable to 1 of 65 methods.*
* [`GetAvailableModelsByTypeForbiddenError`](./src/pipeshub_sdk/errors/getavailablemodelsbytypeforbiddenerror.py): Insufficient OAuth scope.  Only applies to OAuth tokens. The token did not carry the `config:read` scope required by this endpoint. Regular (non-OAuth) JWT bearer tokens are not subject to scope enforcement and will not receive this error. Status code `403`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubChildNodesNotFoundError`](./src/pipeshub_sdk/errors/getknowledgehubchildnodesnotfounderror.py): Parent node not found.  The `parentId` does not correspond to an existing node of the specified `parentType`, or the node has been deleted. Status code `404`. Applicable to 1 of 65 methods.*
* [`GetSearchByIDNotFoundError`](./src/pipeshub_sdk/errors/getsearchbyidnotfounderror.py): Reserved for parity with sibling routes; this endpoint currently returns `200` with an empty array for an unknown id rather than emitting `404`. Status code `404`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubRootNodesInternalServerError`](./src/pipeshub_sdk/errors/getknowledgehubrootnodesinternalservererror.py): An unexpected error occurred on the server. Status code `500`. Applicable to 1 of 65 methods.*
* [`GetKnowledgeHubChildNodesInternalServerError`](./src/pipeshub_sdk/errors/getknowledgehubchildnodesinternalservererror.py): An unexpected error occurred on the server. Status code `500`. Applicable to 1 of 65 methods.*
* [`SearchHistoryInternalServerError`](./src/pipeshub_sdk/errors/searchhistoryinternalservererror.py): Error envelope for a failed request. Status code `500`. Applicable to 1 of 65 methods.*
* [`GetSearchByIDInternalServerError`](./src/pipeshub_sdk/errors/getsearchbyidinternalservererror.py): Server error. Possible causes:  - Explicit `InternalServerError`   or any other 500 `BaseError` thrown by the handler. - Non-`BaseError` exception caught by the   global error middleware. - Response serializer fallback. Status code `500`. Applicable to 1 of 65 methods.*
* [`GetAvailableModelsByTypeInternalServerError`](./src/pipeshub_sdk/errors/getavailablemodelsbytypeinternalservererror.py): An unexpected error occurred on the server. Status code `500`. Applicable to 1 of 65 methods.*
* [`ResponseValidationError`](./src/pipeshub_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
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

| Variable       | Parameter           | Default                      | Description     |
| -------------- | ------------------- | ---------------------------- | --------------- |
| `instance_url` | `instance_url: str` | `"https://app.pipeshub.com"` | Base server URL |

#### Example

```python
from pipeshub_sdk import Pipeshub


with Pipeshub(
    server_idx=0,
    instance_url="https://app.pipeshub.com",
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
    server_url="https://https://app.pipeshub.com",
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
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Pipeshub` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from pipeshub_sdk import Pipeshub
def main():

    with Pipeshub() as pipeshub:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Pipeshub() as pipeshub:
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

<!-- Placeholder for Future Speakeasy SDK Sections -->
