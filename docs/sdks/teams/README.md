# Teams

## Overview

Team management operations

### Available Operations

* [create](#create) - Create a team
* [list](#list) - List teams
* [get_by_id](#get_by_id) - Get team by ID
* [update](#update) - Update team
* [delete](#delete) - Delete team
* [get_members](#get_members) - Get team members
* [add_users](#add_users) - Add users to team
* [remove_users](#remove_users) - Remove users from team
* [update_user_permissions](#update_user_permissions) - Update user role in team
* [get_user](#get_user) - Get current user's teams
* [list_created](#list_created) - Get teams created by current user

## create

Create a new team within the organization for project collaboration and resource sharing.<br><br>
<b>Overview:</b><br>
Teams are collaborative units that group users together for specific projects, departments, or initiatives. Teams have their own resources, permissions, and member hierarchies.<br><br>
<b>Team Structure:</b><br>
<ul>
<li><b>Owner:</b> Creator of the team, full administrative control</li>
<li><b>Admins:</b> Can manage members and settings</li>
<li><b>Members:</b> Standard access to team resources</li>
<li><b>Viewers:</b> Read-only access</li>
</ul>
<b>What Gets Created:</b><br>
<ul>
<li>Team entity with unique identifier</li>
<li>Owner role automatically assigned to creator</li>
<li>Team workspace for shared resources</li>
<li>Default permission settings</li>
</ul>
<b>Initial Members:</b><br>
You can optionally add initial members with their roles during creation using the <code>userRoles</code> array.<br><br>
<b>Validation:</b><br>
<ul>
<li>Team name is required and must be unique in the org</li>
<li>Name: 1-100 characters</li>
<li>Description: Optional, max 500 characters</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createTeam" method="post" path="/teams" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.create(name="Engineering Team", description="Core engineering team for product development")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Team display name (must be unique in org)                           | Engineering Team                                                    |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Team description and purpose                                        | Core engineering team for product development                       |
| `user_roles`                                                        | List[[models.UserRole](../../models/userrole.md)]                   | :heavy_minus_sign:                                                  | Optional initial members with roles                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateTeamResponse](../../models/createteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list

Retrieve all teams in the organization with optional search and pagination.<br><br>
<b>Overview:</b><br>
This endpoint returns teams the authenticated user can access. Admins see all teams; regular users see teams they're members of.<br><br>
<b>Response Data per Team:</b><br>
<ul>
<li>Team metadata (name, description)</li>
<li>Member count</li>
<li>Owner information</li>
<li>Creation timestamp</li>
</ul>
<b>Search:</b><br>
The search parameter performs fuzzy matching on team names and descriptions.<br><br>
<b>Visibility Rules:</b><br>
<ul>
<li><b>Admins:</b> See all organization teams</li>
<li><b>Users:</b> See only teams they belong to</li>
</ul>
<b>Sorting:</b><br>
Results are sorted by name alphabetically by default.


### Example Usage

<!-- UsageSnippet language="python" operationID="listTeams" method="get" path="/teams" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.list(search="engineering", limit=10, page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search teams by name or description                                 | engineering                                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results per page                                          |                                                                     |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number (1-based)                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListTeamsResponse](../../models/listteamsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_id

Retrieve detailed information about a specific team.<br><br>
<b>Overview:</b><br>
Returns complete team details including metadata, member list with roles, and resource information. Use this for team profile pages and detailed views.<br><br>
<b>Response Includes:</b><br>
<ul>
<li>Team metadata (name, description, slug)</li>
<li>Owner and creator information</li>
<li>Member count and list (with pagination)</li>
<li>Team settings and permissions</li>
<li>Creation and modification timestamps</li>
</ul>
<b>Authorization:</b><br>
<ul>
<li>Team members can view their team</li>
<li>Organization admins can view any team</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamById" method="get" path="/teams/{teamId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.get_by_id(team_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTeamByIDResponse](../../models/getteambyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update team metadata and settings.<br><br>
<b>Overview:</b><br>
This endpoint allows updating team properties like name and description. Member management is handled through separate endpoints.<br><br>
<b>Updatable Fields:</b><br>
<ul>
<li><code>name</code>: Team display name (must remain unique)</li>
<li><code>description</code>: Team description</li>
</ul>
<b>Authorization:</b><br>
<ul>
<li><b>Team Owner:</b> Full update access</li>
<li><b>Team Admin:</b> Can update name and description</li>
<li><b>Org Admin:</b> Can update any team</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Team update event published</li>
<li>Team slug may be regenerated if name changes</li>
<li>Cached team data invalidated</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateTeam" method="put" path="/teams/{teamId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.update(team_id="507f1f77bcf86cd799439011", name="Core Engineering Team", description="Primary engineering team for product development")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New team name                                                       | Core Engineering Team                                               |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New team description                                                | Primary engineering team for product development                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateTeamResponse](../../models/updateteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Delete a team from the organization.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Team is soft-deleted (isDeleted: true)</li>
<li>Team members lose access to team resources</li>
<li>Team can be restored by admin if needed</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Only team owner or organization admin can delete</li>
<li>Team must have no active resources (configurable)</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTeam" method="delete" path="/teams/{teamId}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.delete(team_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the team to delete                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteTeamResponse](../../models/deleteteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_members

Retrieve all users that are members of a specific team.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Returns user profiles with their team role</li>
<li>Supports pagination for large teams</li>
<li>Excludes deleted or inactive users</li>
</ul>
<b>Team Roles:</b><br>
<ul>
<li><code>owner</code> - Full control over team settings and members</li>
<li><code>admin</code> - Can manage members and most settings</li>
<li><code>member</code> - Standard team member</li>
<li><code>viewer</code> - Read-only access to team resources</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamUsers" method="get" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.get_members(team_id="507f1f77bcf86cd799439011", page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the team                                       | 507f1f77bcf86cd799439011                                            |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number for pagination (1-based)                                |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of users per page                                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetTeamUsersResponse](../../models/getteamusersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## add_users

Add one or more users to a team with specified roles.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Users already in the team are skipped</li>
<li>Default role is "member" if not specified</li>
<li>Sends invitation notification to added users</li>
</ul>
<b>Validation:</b><br>
<ul>
<li>All user IDs must be valid and from the same organization</li>
<li>Role must be one of the allowed values</li>
<li>Only team owner/admin can add members</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="addUsersToTeam" method="post" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.add_users(team_id="507f1f77bcf86cd799439011", users=[
        {
            "user_id": "507f1f77bcf86cd799439012",
        },
        {
            "user_id": "507f1f77bcf86cd799439013",
            "role": "admin",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `team_id`                                                                                                                 | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Unique identifier of the team                                                                                             | 507f1f77bcf86cd799439011                                                                                                  |
| `users`                                                                                                                   | List[[models.AddUsersToTeamUser](../../models/adduserstoteamuser.md)]                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       | [<br/>{<br/>"userId": "507f1f77bcf86cd799439012",<br/>"role": "member"<br/>},<br/>{<br/>"userId": "507f1f77bcf86cd799439013",<br/>"role": "admin"<br/>}<br/>] |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[models.AddUsersToTeamResponse](../../models/adduserstoteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_users

Remove one or more users from a team.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Users not in the team are silently skipped</li>
<li>Removed users lose access to team resources immediately</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Cannot remove the team owner</li>
<li>Only team owner/admin can remove members</li>
<li>Admins cannot remove other admins (only owner can)</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="removeUsersFromTeam" method="delete" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.remove_users(team_id="507f1f77bcf86cd799439011", user_ids=[
        "507f1f77bcf86cd799439012",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the team                                       | 507f1f77bcf86cd799439011                                            |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of user IDs to remove from the team                           | [<br/>"507f1f77bcf86cd799439012"<br/>]                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RemoveUsersFromTeamResponse](../../models/removeusersfromteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_user_permissions

Update a user's role/permissions within a team.<br><br>
<b>Available Roles:</b><br>
<ul>
<li><code>owner</code> - Full control (only one per team, transferable)</li>
<li><code>admin</code> - Can manage members and settings</li>
<li><code>member</code> - Standard access</li>
<li><code>viewer</code> - Read-only access</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Only team owner can promote to admin</li>
<li>Only team owner can transfer ownership</li>
<li>Admins can modify member/viewer roles</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateTeamUserPermissions" method="put" path="/teams/{teamId}/users/permissions" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.update_user_permissions(team_id="507f1f77bcf86cd799439011", user_id="507f1f77bcf86cd799439012", role="admin")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `team_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the team                                                         | 507f1f77bcf86cd799439011                                                              |
| `user_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | ID of the user whose role to update                                                   | 507f1f77bcf86cd799439012                                                              |
| `role`                                                                                | [models.UpdateTeamUserPermissionsRole](../../models/updateteamuserpermissionsrole.md) | :heavy_check_mark:                                                                    | New role to assign to the user                                                        | admin                                                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.UpdateTeamUserPermissionsResponse](../../models/updateteamuserpermissionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_user

Retrieve all teams that the authenticated user is a member of.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Includes teams where user is owner, admin, member, or viewer</li>
<li>Returns user's role in each team</li>
<li>Sorted by most recently accessed</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Populating team switcher in UI</li>
<li>Dashboard team list</li>
<li>Access control checks</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserTeams" method="get" path="/teams/user/teams" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.get_user(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number for pagination (1-based)                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of teams per page                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserTeamsResponse](../../models/getuserteamsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_created

Retrieve all teams that were created by the authenticated user.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Only includes teams where user is the original creator</li>
<li>User may or may not still be the owner (ownership can be transferred)</li>
<li>Useful for tracking team creation history</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserCreatedTeams" method="get" path="/teams/user/teams/created" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.teams.list_created(page=1, limit=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number for pagination (1-based)                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of teams per page                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserCreatedTeamsResponse](../../models/getusercreatedteamsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |