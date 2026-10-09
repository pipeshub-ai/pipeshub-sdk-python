# Projects

## Overview

Workspaces that group related assistant and agent conversations under a
shared name, custom instructions, a knowledge scope, and reference
files. Projects can be shared with teammates; project membership only
grants read access to conversations explicitly marked
`projectVisibility: project` — a member never gets access to another
member's private chats. See `Conversations` for the two fields
(`projectId`, `projectVisibility`) that link a conversation to a
project.


### Available Operations

* [set_conversation_project](#set_conversation_project) - Link or unlink a conversation to a project
* [set_conversation_project_visibility](#set_conversation_project_visibility) - Override a conversation's project visibility
* [create_project](#create_project) - Create a project
* [list_projects](#list_projects) - List projects
* [get_project_by_id](#get_project_by_id) - Get a project
* [update_project](#update_project) - Update a project
* [delete_project](#delete_project) - Delete a project
* [archive_project](#archive_project) - Archive a project
* [unarchive_project](#unarchive_project) - Unarchive a project
* [pin_project](#pin_project) - Pin a project
* [unpin_project](#unpin_project) - Unpin a project
* [get_project_conversations](#get_project_conversations) - List a project's conversations
* [ensure_project_knowledge_base](#ensure_project_knowledge_base) - Ensure (create-if-absent) the project's hidden file Collection
* [list_project_members](#list_project_members) - List project members
* [upsert_project_members](#upsert_project_members) - Add or update project members
* [remove_project_member](#remove_project_member) - Remove a project member
* [set_agent_conversation_project](#set_agent_conversation_project) - Link or unlink an agent conversation to a project
* [set_agent_conversation_project_visibility](#set_agent_conversation_project_visibility) - Override an agent conversation's project visibility

## set_conversation_project

Set (`projectId: <id>`) or clear (`projectId: null`) the project this
conversation belongs to. Initiator-only.

**Access:**

The caller must be the conversation's initiator. Linking to a
non-null `projectId` also requires at least viewer access to that
project (`404` if not visible to the caller — never `403`, to avoid
leaking project existence across an org boundary).

**Visibility on link:**

When linking, `projectVisibility` defaults from the project's
`chatSharing` setting (`members` → `project`, otherwise `private`)
unless the conversation was already `project`-visible, in which case
that is preserved. Use
`PATCH /conversations/{conversationId}/project-visibility` to
override it explicitly. Unlinking (`projectId: null`) always clears
both `projectId` and `projectVisibility`.


### Example Usage

<!-- UsageSnippet language="python" operationID="setConversationProject" method="put" path="/conversations/{conversationId}/project" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.set_conversation_project(conversation_id="<value>", project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Unique conversation identifier                                      |
| `project_id`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | Target project id, or `null` to unlink.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetConversationProjectResponse](../../models/setconversationprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_conversation_project_visibility

Explicitly set whether a project-linked conversation is visible to
other members of that project (`project`) or only to its owner
(`private`). Initiator-only. Requires the conversation to already be
linked to a project via
`PUT /conversations/{conversationId}/project`.


### Example Usage

<!-- UsageSnippet language="python" operationID="setConversationProjectVisibility" method="patch" path="/conversations/{conversationId}/project-visibility" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.set_conversation_project_visibility(conversation_id="<value>", visibility="project")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                               | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Unique conversation identifier                                                                                  |
| `visibility`                                                                                                    | [models.SetConversationProjectVisibilityVisibility](../../models/setconversationprojectvisibilityvisibility.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.SetConversationProjectVisibilityResponse](../../models/setconversationprojectvisibilityresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_project

Create a new project workspace owned by the caller.


### Example Usage

<!-- UsageSnippet language="python" operationID="createProject" method="post" path="/projects" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.create_project(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                       | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                          | *str*                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `description`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `icon`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `color`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `instructions`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `knowledge_scope`                                                                                                                                                               | [Optional[models.ProjectKnowledgeScope]](../../models/projectknowledgescope.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | Retrieval scope (app connector / knowledge-base ids) inherited by<br/>every conversation in the project when the request itself carries no<br/>`filters`. Same id shapes as `Filters`.<br/> |
| `applied_filters`                                                                                                                                                               | [Optional[models.ProjectAppliedFilters]](../../models/projectappliedfilters.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | Display-friendly mirror of `knowledgeScope`, for rendering scope chips without a round trip.                                                                                    |
| `tools`                                                                                                                                                                         | List[*str*]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `retries`                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                             |

### Response

**[models.CreateProjectResponse](../../models/createprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_projects

Paginated, non-deleted projects visible to the caller, sorted pinned
first then by `lastActivityAt` descending.


### Example Usage

<!-- UsageSnippet language="python" operationID="listProjects" method="get" path="/projects" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.list_projects(page=1, limit=20, scope="mine", include_archived="false")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                          | *Optional[int]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | N/A                                                                                                                                             |
| `limit`                                                                                                                                         | *Optional[int]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | N/A                                                                                                                                             |
| `search`                                                                                                                                        | *Optional[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | Case-insensitive match on project name.                                                                                                         |
| `scope`                                                                                                                                         | [Optional[models.Scope]](../../models/scope.md)                                                                                                 | :heavy_minus_sign:                                                                                                                              | `mine` — owned only. `shared` — projects the caller is a member<br/>of. `all` — owned, member, and `visibility: org` projects.<br/>Defaults to `mine`.<br/> |
| `include_archived`                                                                                                                              | [Optional[models.IncludeArchived]](../../models/includearchived.md)                                                                             | :heavy_minus_sign:                                                                                                                              | Include archived projects alongside active projects.                                                                                            |
| `is_archived`                                                                                                                                   | [Optional[models.ListProjectsIsArchived]](../../models/listprojectsisarchived.md)                                                               | :heavy_minus_sign:                                                                                                                              | Filter by exact archive status. When provided, this takes<br/>precedence over `includeArchived`.<br/>                                           |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.ListProjectsResponse](../../models/listprojectsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_project_by_id

Requires at least viewer access. Cross-org ids and ids the caller
cannot see both return `404` — never `403` — to avoid leaking
project existence across an org boundary.


### Example Usage

<!-- UsageSnippet language="python" operationID="getProjectById" method="get" path="/projects/{projectId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.get_project_by_id(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectByIDResponse](../../models/getprojectbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_project

Requires editor access. `visibility` and `chatSharing` are
owner-only fields — including either as a non-owner editor
returns `403`.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateProject" method="patch" path="/projects/{projectId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.update_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                       | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                                                                                    | *str*                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `name`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `description`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `icon`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `color`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `instructions`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `knowledge_scope`                                                                                                                                                               | [Optional[models.ProjectKnowledgeScope]](../../models/projectknowledgescope.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | Retrieval scope (app connector / knowledge-base ids) inherited by<br/>every conversation in the project when the request itself carries no<br/>`filters`. Same id shapes as `Filters`.<br/> |
| `applied_filters`                                                                                                                                                               | [Optional[models.ProjectAppliedFilters]](../../models/projectappliedfilters.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | Display-friendly mirror of `knowledgeScope`, for rendering scope chips without a round trip.                                                                                    |
| `tools`                                                                                                                                                                         | List[*str*]                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `visibility`                                                                                                                                                                    | [Optional[models.UpdateProjectRequestVisibility]](../../models/updateprojectrequestvisibility.md)                                                                               | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `chat_sharing`                                                                                                                                                                  | [Optional[models.UpdateProjectRequestChatSharing]](../../models/updateprojectrequestchatsharing.md)                                                                             | :heavy_minus_sign:                                                                                                                                                              | N/A                                                                                                                                                                             |
| `retries`                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                             |

### Response

**[models.UpdateProjectResponse](../../models/updateprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_project

Owner-only soft delete. Unlinks every `chatSessions` row pointing at
this project (clearing `projectId`/`projectVisibility`) before
marking the project deleted, so no conversation is left pointing at
a deleted project; wrapped in a transaction when the deployment's
replica set supports it. Idempotent — deleting an already-deleted
project returns `200` without re-running the unlink step.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteProject" method="delete" path="/projects/{projectId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.delete_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteProjectResponse](../../models/deleteprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## archive_project

Requires editor access. Archived projects are hidden from the
default sidebar but their conversations remain reachable directly.


### Example Usage

<!-- UsageSnippet language="python" operationID="archiveProject" method="post" path="/projects/{projectId}/archive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.archive_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ArchiveProjectResponse](../../models/archiveprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unarchive_project

Unarchive a project

### Example Usage

<!-- UsageSnippet language="python" operationID="unarchiveProject" method="post" path="/projects/{projectId}/unarchive" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.unarchive_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnarchiveProjectResponse](../../models/unarchiveprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## pin_project

Requires viewer access. Pin state is owner-scoped on the document in
V1 — pinning affects the project for every viewer, not just the
caller (per-user pins are deferred).


### Example Usage

<!-- UsageSnippet language="python" operationID="pinProject" method="post" path="/projects/{projectId}/pin" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.pin_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PinProjectResponse](../../models/pinprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## unpin_project

Unpin a project

### Example Usage

<!-- UsageSnippet language="python" operationID="unpinProject" method="post" path="/projects/{projectId}/unpin" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.unpin_project(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnpinProjectResponse](../../models/unpinprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_project_conversations

Requires viewer access to the project. Returns both chat and agent
sessions (`chatSessions`, discriminated by `sessionType`/`agentKey`)
that the caller may see: rows they own, plus rows with
`projectVisibility: project`. Access to the project is asserted
first, so a private conversation belonging to a *different* project
member never leaks through this endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="getProjectConversations" method="get" path="/projects/{projectId}/conversations" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.get_project_conversations(project_id="<value>", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectConversationsResponse](../../models/getprojectconversationsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ensure_project_knowledge_base

Requires editor access. Lazily creates the project's own hidden
Knowledge Base (`isHidden: true` in Python `POST /api/v1/kb`) the
first time a caller needs to upload a file, and returns its id
either way. Race-safe: concurrent callers converge on one KB —
the losing request's KB is deleted. The hidden KB is excluded from
the Collections sidebar, Knowledge Hub, and unscoped search, but is
always included in this project's own chat scope
(`filters.kb`) and file uploads go through the normal
`POST /knowledgeBase/{kbId}/upload` SSE pipeline afterward.


### Example Usage

<!-- UsageSnippet language="python" operationID="ensureProjectKnowledgeBase" method="post" path="/projects/{projectId}/knowledge-base" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.ensure_project_knowledge_base(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnsureProjectKnowledgeBaseResponse](../../models/ensureprojectknowledgebaseresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_project_members

Requires viewer access.

### Example Usage

<!-- UsageSnippet language="python" operationID="listProjectMembers" method="get" path="/projects/{projectId}/members" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.list_project_members(project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListProjectMembersResponse](../../models/listprojectmembersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upsert_project_members

Owner-only. Each `principalId` is validated against this org's IAM
service the same way as
`POST /conversations/{conversationId}/share` — a `principalId` with
no matching user returns `400`. Upserts by `principalId`; the owner
is silently skipped if included.


### Example Usage

<!-- UsageSnippet language="python" operationID="upsertProjectMembers" method="put" path="/projects/{projectId}/members" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.upsert_project_members(project_id="<value>", members=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                                                                         | *str*                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                   | N/A                                                                                                                                                                  |
| `members`                                                                                                                                                            | List[[models.Member](../../models/member.md)]                                                                                                                        | :heavy_check_mark:                                                                                                                                                   | Upserted by `principalId`: existing members get their `role`<br/>updated, new ids are added. The project owner is silently<br/>skipped if included (ownership is implicit).<br/> |
| `retries`                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                  |

### Response

**[models.UpsertProjectMembersResponse](../../models/upsertprojectmembersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_project_member

Owner-only.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeProjectMember" method="delete" path="/projects/{projectId}/members/{memberUserId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.remove_project_member(project_id="<value>", member_user_id="<value>", principal_type="user")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `member_user_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `principal_type`                                                                                      | [Optional[models.RemoveProjectMemberPrincipalType]](../../models/removeprojectmemberprincipaltype.md) | :heavy_minus_sign:                                                                                    | Whether `memberUserId` identifies a user or a team.<br/>Defaults to `user` when omitted.<br/>         |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.RemoveProjectMemberResponse](../../models/removeprojectmemberresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_agent_conversation_project

Agent-conversation equivalent of
`PUT /conversations/{conversationId}/project`. Set
(`projectId: <id>`) or clear (`projectId: null`) the project this
agent conversation belongs to. Initiator-only; linking requires at
least viewer access to the target project.


### Example Usage

<!-- UsageSnippet language="python" operationID="setAgentConversationProject" method="put" path="/agents/{agentKey}/conversations/{conversationId}/project" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.set_agent_conversation_project(agent_key="<value>", conversation_id="<value>", project_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | Target project id, or `null` to unlink.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetAgentConversationProjectResponse](../../models/setagentconversationprojectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_agent_conversation_project_visibility

Agent-conversation equivalent of
`PATCH /conversations/{conversationId}/project-visibility`.
Initiator-only; requires the conversation to already be linked to a
project.


### Example Usage

<!-- UsageSnippet language="python" operationID="setAgentConversationProjectVisibility" method="patch" path="/agents/{agentKey}/conversations/{conversationId}/project-visibility" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.projects.set_agent_conversation_project_visibility(agent_key="<value>", conversation_id="<value>", visibility="private")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                               | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `conversation_id`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `visibility`                                                                                                              | [models.SetAgentConversationProjectVisibilityVisibility](../../models/setagentconversationprojectvisibilityvisibility.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.SetAgentConversationProjectVisibilityResponse](../../models/setagentconversationprojectvisibilityresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |