# Permissions

## Overview

Permission management for knowledge bases

### Available Operations

* [grant](#grant) - Grant permissions
* [list](#list) - List permissions
* [update](#update) - Update permissions
* [delete](#delete) - Remove permissions

## grant

Grant access permissions to users or teams for a knowledge base.<br><br>
<b>Required Permission:</b> OWNER or ORGANIZER<br><br>
<b>Permission Roles (highest to lowest):</b><br>
<ol>
<li><b>OWNER:</b> Full control, can delete KB, manage all permissions</li>
<li><b>ORGANIZER:</b> Can manage permissions (except OWNER), edit KB settings</li>
<li><b>FILEORGANIZER:</b> Can create/delete folders, organize content</li>
<li><b>WRITER:</b> Can upload, edit, delete records</li>
<li><b>COMMENTER:</b> Can add comments (if supported)</li>
<li><b>READER:</b> View-only access</li>
</ol>
<b>Grant to Multiple:</b><br>
Provide arrays of userIds and/or teamIds to grant the same role to multiple entities.


### Example Usage

<!-- UsageSnippet language="python" operationID="createKBPermission" method="post" path="/knowledgeBase/{kbId}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.permissions.grant(kb_id="<id>", role="OWNER")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `kb_id`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `role`                                                                  | [models.CreateKBPermissionRole](../../models/createkbpermissionrole.md) | :heavy_check_mark:                                                      | Permission role to grant                                                |
| `user_ids`                                                              | List[*str*]                                                             | :heavy_minus_sign:                                                      | User IDs to grant permission                                            |
| `team_ids`                                                              | List[*str*]                                                             | :heavy_minus_sign:                                                      | Team IDs to grant permission                                            |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CreateKBPermissionResponse](../../models/createkbpermissionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list

Retrieve all permissions granted on a knowledge base.<br><br>
<b>Required Permission:</b> ORGANIZER or higher to see all permissions, others see only their own.


### Example Usage

<!-- UsageSnippet language="python" operationID="listKBPermissions" method="get" path="/knowledgeBase/{kbId}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.permissions.list(kb_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListKBPermissionsResponse](../../models/listkbpermissionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update permission roles for users or teams.<br><br>
<b>Required Permission:</b> OWNER or ORGANIZER


### Example Usage

<!-- UsageSnippet language="python" operationID="updateKBPermissions" method="put" path="/knowledgeBase/{kbId}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.permissions.update(kb_id="<id>", role="WRITER")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `kb_id`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `role`                                                                    | [models.UpdateKBPermissionsRole](../../models/updatekbpermissionsrole.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `user_ids`                                                                | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `team_ids`                                                                | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Remove access permissions from users or teams.<br><br>
<b>Required Permission:</b> OWNER or ORGANIZER<br><br>
<b>Note:</b> Cannot remove the last OWNER from a KB.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteKBPermissions" method="delete" path="/knowledgeBase/{kbId}/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.permissions.delete(kb_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `team_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |