# UserGroups

## Overview

User group management operations

### Available Operations

* [create_user_group](#create_user_group) - Create user group
* [get_all_user_groups](#get_all_user_groups) - Get all user groups
* [get_user_group_by_id](#get_user_group_by_id) - Get user group by ID
* [update_user_group](#update_user_group) - Update user group
* [delete_user_group](#delete_user_group) - Delete user group
* [add_users_to_group](#add_users_to_group) - Add users to group
* [remove_users_from_group](#remove_users_from_group) - Remove users from group
* [get_groups_for_user](#get_groups_for_user) - Get groups for a user
* [~~get_users_in_group~~](#get_users_in_group) - Get users in group :warning: **Deprecated**
* [~~get_group_statistics~~](#get_group_statistics) - Get group statistics :warning: **Deprecated**

## create_user_group

Create a new user group within the organization.<br><br>
<b>Group Types:</b><br>
<ul>
<li><code>admin</code> - Administrative group with elevated privileges</li>
<li><code>standard</code> - Regular user group</li>
<li><code>everyone</code> - Automatically includes all organization users</li>
<li><code>custom</code> - Custom group with manual membership management</li>
</ul>
<b>Validation Rules:</b><br>
<ul>
<li>Group name must be unique within the organization</li>
<li>Group name is required and cannot be empty</li>
<li>Type must be one of the allowed values</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Creates a unique slug from the group name</li>
<li>Sets createdBy to the authenticated user</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createUserGroup" method="post" path="/userGroups" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.create_user_group(name="Engineering Team", type_="standard", description="All engineering department members")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Display name for the group                                          | Engineering Team                                                    |
| `type`                                                              | [models.CreateUserGroupType](../../models/createusergrouptype.md)   | :heavy_check_mark:                                                  | Group type determining behavior and privileges                      | standard                                                            |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional description of the group's purpose                         | All engineering department members                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserGroup](../../models/usergroup.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_all_user_groups

Retrieve all user groups in the organization.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Returns all groups including admin, standard, everyone, and custom types</li>
<li>Groups are returned with their member counts</li>
<li>Soft-deleted groups are excluded by default</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Populating group selection dropdowns</li>
<li>Managing group memberships</li>
<li>Access control configuration</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllUserGroups" method="get" path="/userGroups" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.get_all_user_groups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllUserGroupsResponse](../../models/getallusergroupsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_user_group_by_id

Retrieve detailed information about a specific user group.<br><br>
<b>Response Includes:</b><br>
<ul>
<li>Group metadata (name, type, description)</li>
<li>Member count</li>
<li>Creation and modification timestamps</li>
<li>Creator information</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserGroupById" method="get" path="/userGroups/{groupId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.get_user_group_by_id(group_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user group                                 | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserGroup](../../models/usergroup.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_user_group

Update an existing user group's information.<br><br>
<b>Updatable Fields:</b><br>
<ul>
<li><code>name</code> - Display name (must remain unique)</li>
<li><code>description</code> - Group description</li>
</ul>
<b>Note:</b> Group type cannot be changed after creation.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUserGroup" method="put" path="/userGroups/{groupId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.update_user_group(group_id="507f1f77bcf86cd799439011", name="Engineering Team - Updated", description="All engineering and DevOps members")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user group to update                       | 507f1f77bcf86cd799439011                                            |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New display name for the group                                      | Engineering Team - Updated                                          |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Updated description                                                 | All engineering and DevOps members                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserGroup](../../models/usergroup.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_user_group

Soft delete a user group.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Group is marked as deleted (isDeleted: true)</li>
<li>Group members are not affected</li>
<li>Group can be restored by admin if needed</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Cannot delete system groups (admin, everyone)</li>
<li>Requires admin privileges</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteUserGroup" method="delete" path="/userGroups/{groupId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.delete_user_group(group_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user group to delete                       | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteUserGroupResponse](../../models/deleteusergroupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_users_to_group

Add one or more users to a user group.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Users already in the group are silently skipped</li>
<li>Invalid user IDs are reported in the response</li>
<li>Operation is atomic - all valid users are added together</li>
</ul>
<b>Validation:</b><br>
<ul>
<li>All user IDs must be valid MongoDB ObjectIds</li>
<li>Users must belong to the same organization</li>
<li>Group must exist and not be deleted</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="addUsersToGroup" method="post" path="/userGroups/add-users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.add_users_to_group(group_id="507f1f77bcf86cd799439011", user_ids=[
        "507f1f77bcf86cd799439012",
        "507f1f77bcf86cd799439013",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the group to add users to                                     | 507f1f77bcf86cd799439011                                            |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of user IDs to add to the group                               | [<br/>"507f1f77bcf86cd799439012",<br/>"507f1f77bcf86cd799439013"<br/>] |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AddUsersToGroupResponse](../../models/adduserstogroupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_users_from_group

Remove one or more users from a user group.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Users not in the group are silently skipped</li>
<li>Operation is atomic - all specified users are removed together</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Cannot remove users from "everyone" group type</li>
<li>Cannot remove the last admin from admin group</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="removeUsersFromGroup" method="post" path="/userGroups/remove-users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.remove_users_from_group(group_id="507f1f77bcf86cd799439011", user_ids=[
        "507f1f77bcf86cd799439012",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the group to remove users from                                | 507f1f77bcf86cd799439011                                            |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of user IDs to remove from the group                          | [<br/>"507f1f77bcf86cd799439012"<br/>]                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RemoveUsersFromGroupResponse](../../models/removeusersfromgroupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_groups_for_user

Retrieve all user groups that a specific user belongs to.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Includes all group types (admin, standard, everyone, custom)</li>
<li>Returns group metadata for each membership</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Displaying user's group memberships in profile</li>
<li>Access control checks</li>
<li>Permission inheritance calculations</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getGroupsForUser" method="get" path="/userGroups/users/{userId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.get_groups_for_user(user_id="507f1f77bcf86cd799439012")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user                                       | 507f1f77bcf86cd799439012                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetGroupsForUserResponse](../../models/getgroupsforuserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_users_in_group~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve all users that belong to a specific user group.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsersInGroup" method="get" path="/userGroups/{groupId}/users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.get_users_in_group(group_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user group                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUsersInGroupResponse](../../models/getusersingroupresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_group_statistics~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve statistics for all user groups including member counts.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGroupStatistics" method="get" path="/userGroups/stats/list" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.user_groups.get_group_statistics()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGroupStatisticsResponse](../../models/getgroupstatisticsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |