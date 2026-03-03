# Teams

## Overview

Team management operations

### Available Operations

* [create_team](#create_team) - Create a team
* [list_teams](#list_teams) - List teams
* [get_team_by_id](#get_team_by_id) - Get team by ID
* [update_team](#update_team) - Update team
* [delete_team](#delete_team) - Delete team
* [get_user_teams](#get_user_teams) - Get current user's teams
* [~~get_team_users~~](#get_team_users) - Get users in team :warning: **Deprecated**
* [~~add_users_to_team~~](#add_users_to_team) - Add users to team :warning: **Deprecated**
* [~~remove_user_from_team~~](#remove_user_from_team) - Remove user from team :warning: **Deprecated**
* [~~update_team_users_permissions~~](#update_team_users_permissions) - Update team users permissions :warning: **Deprecated**
* [~~get_user_created_teams~~](#get_user_created_teams) - Get user created teams :warning: **Deprecated**

## create_team

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.create_team(name="Engineering Team", description="Core engineering team for product development")

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

## list_teams

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.list_teams(search="engineering", limit=10, page=1)

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

## get_team_by_id

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.get_team_by_id(team_id="507f1f77bcf86cd799439011")

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

## update_team

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.update_team(team_id="507f1f77bcf86cd799439011", name="Core Engineering Team", description="Primary engineering team for product development")

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

## delete_team

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.delete_team(team_id="507f1f77bcf86cd799439011")

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

## get_user_teams

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.get_user_teams(page=1, limit=20)

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

## ~~get_team_users~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve all users that belong to a specific team.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamUsers" method="get" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.get_team_users(team_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTeamUsersResponse](../../models/getteamusersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~add_users_to_team~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Add one or more users to a team.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="addUsersToTeam" method="post" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.add_users_to_team(team_id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddUsersToTeamResponse](../../models/adduserstoteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~remove_user_from_team~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Remove a user from a team.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUserFromTeam" method="delete" path="/teams/{teamId}/users" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.remove_user_from_team(team_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoveUserFromTeamResponse](../../models/removeuserfromteamresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~update_team_users_permissions~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update permissions for users within a team.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTeamUsersPermissions" method="put" path="/teams/{teamId}/users/permissions" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.update_team_users_permissions(team_id="<id>", body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `team_id`                                                                                             | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `body`                                                                                                | [models.UpdateTeamUsersPermissionsRequestBody](../../models/updateteamuserspermissionsrequestbody.md) | :heavy_check_mark:                                                                                    | Request payload                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.UpdateTeamUsersPermissionsResponse](../../models/updateteamuserspermissionsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_user_created_teams~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve teams created by the authenticated user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserCreatedTeams" method="get" path="/teams/user/teams/created" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.teams.get_user_created_teams()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserCreatedTeamsResponse](../../models/getusercreatedteamsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |