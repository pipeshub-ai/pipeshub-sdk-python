# Users

## Overview

User management operations

### Available Operations

* [get_all](#get_all) - Get all users
* [create](#create) - Create a new user
* [get_by_id](#get_by_id) - Get user by ID
* [update](#update) - Update user
* [delete](#delete) - Delete user
* [get_all_with_groups](#get_all_with_groups) - Get all users with their groups
* [get_email](#get_email) - Get user email by ID
* [get_by_ids](#get_by_ids) - Get users by IDs (bulk)
* [exists_by_email](#exists_by_email) - Check if user exists by email
* [get_internal](#get_internal) - Get user (internal service-to-service)
* [update_full_name](#update_full_name) - Update user full name
* [update_first_name](#update_first_name) - Update user first name
* [update_last_name](#update_last_name) - Update user last name
* [update_designation](#update_designation) - Update user designation
* [check_admin_status](#check_admin_status) - Check if user is admin
* [upload_display_picture](#upload_display_picture) - Upload display picture
* [get_display_picture](#get_display_picture) - Get display picture
* [remove_display_picture](#remove_display_picture) - Remove display picture
* [bulk_invite](#bulk_invite) - Bulk invite users
* [resend_invite](#resend_invite) - Resend user invite
* [list_with_graph](#list_with_graph) - List users (paginated with graph data)
* [get_teams](#get_teams) - Get current user's teams

## get_all

Retrieve a paginated list of all users in the organization.<br><br>
<b>Overview:</b><br>
This endpoint returns all active users in your organization. It's the primary endpoint for listing and displaying users in admin dashboards, user directories, and selection interfaces.<br><br>
<b>Response Data:</b><br>
<ul>
<li>User profile information (name, email, designation)</li>
<li>Account status (active, pending invitation, disabled)</li>
<li>Login history (hasLoggedIn flag)</li>
<li>Timestamps (createdAt, updatedAt)</li>
</ul>
<b>Privacy Controls:</b><br>
<ul>
<li>Email addresses may be masked based on organization settings</li>
<li>Sensitive fields (password, tokens) are never exposed</li>
<li>Deleted users are excluded from results</li>
</ul>
<b>Performance Notes:</b><br>
<ul>
<li>Results are cached for improved performance</li>
<li>For large organizations, consider using pagination</li>
<li>Use <code>/users/by-ids</code> for fetching specific users</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllUsers" method="get" path="/users" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_all(page=1, limit=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number for pagination (1-based)                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of users per page                                            |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search users by name or email                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllUsersResponse](../../models/getallusersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create

Create a new user account in the organization and optionally send an invitation email.<br><br>
<b>Overview:</b><br>
This endpoint creates a new user account. The user will be added to the organization but won't have a password set until they complete the invitation flow or are assigned one by an admin.<br><br>
<b>Invitation Flow:</b><br>
<ol>
<li>Admin creates user with this endpoint</li>
<li>System generates invitation token</li>
<li>User receives invitation email (if sendInvite is true)</li>
<li>User clicks link and sets their password</li>
<li>User can now log in normally</li>
</ol>
<b>Validation Rules:</b><br>
<ul>
<li><code>fullName</code>: Required, 1-100 characters</li>
<li><code>email</code>: Required, valid email format, must be unique in org</li>
<li><code>mobile</code>: Optional, format: +[country][number] (10-15 digits)</li>
<li><code>designation</code>: Optional, job title or role</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>User is automatically added to the "everyone" group</li>
<li>Invitation email sent if <code>sendInvite: true</code></li>
<li>User creation event published to event bus</li>
<li>Audit log entry created</li>
</ul>
<b>Authorization:</b><br>
Only organization administrators can create new users.


### Example Usage

<!-- UsageSnippet language="python" operationID="createUser" method="post" path="/users" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.create(full_name="John Smith", email="john.smith@company.com", mobile="+15551234567", designation="Software Engineer", send_invite=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `full_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | User's full display name                                            | John Smith                                                          |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | User's email address (must be unique)                               | john.smith@company.com                                              |
| `mobile`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Mobile phone number with country code                               | +15551234567                                                        |
| `designation`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Job title or designation                                            | Software Engineer                                                   |
| `send_invite`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether to send invitation email immediately                        |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateUserResponse](../../models/createuserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_id

Retrieve detailed information about a specific user by their unique identifier.<br><br>
<b>Overview:</b><br>
This endpoint returns the complete user profile for the specified user ID. Use this to display user details in profiles, settings pages, or when you need full user information.<br><br>
<b>Response Data:</b><br>
<ul>
<li>Basic info: fullName, firstName, lastName, email</li>
<li>Contact: mobile, address</li>
<li>Professional: designation</li>
<li>Status: hasLoggedIn, isDeleted, accountStatus</li>
<li>Metadata: createdAt, updatedAt, createdBy</li>
</ul>
<b>Privacy Notes:</b><br>
<ul>
<li>Email may be masked for non-admin users based on org settings</li>
<li>Password and sensitive tokens are never returned</li>
<li>Display picture URL returned if set</li>
</ul>
<b>Related Endpoints:</b><br>
<ul>
<li><code>GET /users/{id}/email</code> - Get just the email (admin only)</li>
<li><code>GET /users/fetch/with-groups</code> - Get user with group memberships</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserById" method="get" path="/users/{id}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_by_id(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetUserByIDResponse](../../models/getuserbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update

Update user profile information. Users can update their own profile, admins can update any user.<br><br>
<b>Overview:</b><br>
This endpoint allows updating user profile fields. The scope of allowed updates depends on the requester's role and relationship to the user being updated.<br><br>
<b>Authorization Matrix:</b><br>
<ul>
<li><b>Self-update:</b> Users can update their own fullName, mobile, designation, address</li>
<li><b>Admin-update:</b> Admins can update any field for any user</li>
<li><b>Email changes:</b> Require admin privileges and trigger re-verification</li>
</ul>
<b>Updatable Fields:</b><br>
<ul>
<li><code>fullName</code>: Display name (also updates firstName/lastName if parsed)</li>
<li><code>firstName</code>: First name only</li>
<li><code>lastName</code>: Last name only</li>
<li><code>email</code>: Email address (admin only, triggers verification)</li>
<li><code>mobile</code>: Phone number with country code</li>
<li><code>designation</code>: Job title</li>
<li><code>address</code>: Full address object</li>
</ul>
<b>Validation Rules:</b><br>
<ul>
<li>Email must be unique within the organization</li>
<li>Mobile must match pattern: +[country][number]</li>
<li>Name fields: 1-100 characters</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>User update event published to event bus</li>
<li>Audit log entry created for admin updates</li>
<li>Email change triggers verification email</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUser" method="put" path="/users/{id}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.update(id="507f1f77bcf86cd799439011", full_name="John Smith", first_name="John", last_name="Smith", email="john.smith@company.com", mobile="+15551234567", designation="Senior Software Engineer")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `full_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Full display name                                                   | John Smith                                                          |
| `first_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | First name only                                                     | John                                                                |
| `last_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Last name only                                                      | Smith                                                               |
| `email`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Email address (admin only)                                          | john.smith@company.com                                              |
| `mobile`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Mobile phone with country code                                      | +15551234567                                                        |
| `designation`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Job title or role                                                   | Senior Software Engineer                                            |
| `address`                                                           | [Optional[models.Address]](../../models/address.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateUserResponse](../../models/updateuserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete

Soft delete a user from the organization. The user account is deactivated but data is retained for audit purposes.<br><br>
<b>Overview:</b><br>
This endpoint performs a soft delete on a user account. The user is marked as deleted and can no longer access the system, but their data is retained for compliance and audit purposes.<br><br>
<b>What Happens on Delete:</b><br>
<ol>
<li>User's <code>isDeleted</code> flag is set to true</li>
<li>User's password is cleared</li>
<li>User is removed from all user groups</li>
<li>User's active sessions are invalidated</li>
<li>User deletion event is published</li>
</ol>
<b>Restrictions:</b><br>
<ul>
<li>Cannot delete organization admins (demote first)</li>
<li>Cannot delete the organization owner</li>
<li>Cannot delete yourself through this endpoint</li>
<li>Cannot delete already-deleted users</li>
</ul>
<b>Data Retention:</b><br>
<ul>
<li>User profile data is retained (soft delete)</li>
<li>User's documents and content remain with updated ownership</li>
<li>Audit logs are preserved</li>
<li>Data can be permanently purged by super admin if required</li>
</ul>
<b>Recovery:</b><br>
Deleted users can be restored by organization admins within a configurable retention period.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteUser" method="delete" path="/users/{id}" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.delete(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteUserResponse](../../models/deleteuserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_all_with_groups

Retrieve all users along with their group memberships in a single optimized query.<br><br>
<b>Overview:</b><br>
This endpoint returns users with their associated groups pre-loaded, eliminating the need for separate group lookup calls. Ideal for admin dashboards that need to display user permissions at a glance.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Admin dashboards showing user-group matrix</li>
<li>Permission auditing and compliance checks</li>
<li>Bulk user management interfaces</li>
<li>Access control visualization</li>
</ul>
<b>Response Data per User:</b><br>
<ul>
<li><code>_id</code>: User's unique identifier</li>
<li><code>userId</code>: User's public-facing ID</li>
<li><code>orgId</code>: Organization identifier</li>
<li><code>fullName</code>: User's display name</li>
<li><code>hasLoggedIn</code>: Whether user has ever logged in</li>
<li><code>groups</code>: Array of group objects with name and type</li>
</ul>
<b>Group Types Returned:</b><br>
<ul>
<li><code>admin</code>: Administrative groups with elevated permissions</li>
<li><code>standard</code>: Regular user groups</li>
<li><code>everyone</code>: Default group containing all org users</li>
<li><code>custom</code>: Custom groups created by admins</li>
</ul>
<b>Performance Notes:</b><br>
Uses aggregation pipeline for efficient single-query retrieval. Cached results for improved performance on large organizations.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllUsersWithGroups" method="get" path="/users/fetch/with-groups" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_all_with_groups(include_deleted=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `include_deleted`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include soft-deleted users (admin only)                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllUsersWithGroupsResponse](../../models/getalluserswithgroupsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_email

Retrieve the email address for a specific user. This is a dedicated endpoint for email lookup with proper access controls.<br><br>
<b>Overview:</b><br>
This endpoint provides direct access to a user's email address. It exists separately from the main user endpoint to allow granular permission control over email visibility.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Admin communication workflows</li>
<li>Invitation and notification systems</li>
<li>Email-based user lookup</li>
<li>Contact information export</li>
</ul>
<b>Privacy Considerations:</b><br>
<ul>
<li>Only organization admins can access this endpoint</li>
<li>Access is logged for audit purposes</li>
<li>Consider GDPR/privacy regulations when exposing emails</li>
</ul>
<b>Authorization:</b><br>
Requires admin privileges. Regular users should use the main user endpoint which may mask emails based on organization settings.


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserEmailById" method="get" path="/users/{id}/email" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_email(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetUserEmailByIDResponse](../../models/getuseremailbyidresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_by_ids

Retrieve multiple users by their IDs in a single optimized request. Ideal for efficiently fetching a specific set of users.<br><br>
<b>Overview:</b><br>
This bulk endpoint allows fetching multiple users in a single API call, reducing network overhead when you need to display information about several known users.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Fetching user details for a list of team members</li>
<li>Populating user cards in a dashboard</li>
<li>Loading participants in a document or conversation</li>
<li>Building user mention/autocomplete features</li>
</ul>
<b>Request Format:</b><br>
<ul>
<li>Send array of user IDs in request body</li>
<li>Each ID must be valid 24-character MongoDB ObjectId</li>
<li>Maximum 100 IDs per request (for performance)</li>
<li>Duplicate IDs are automatically deduplicated</li>
</ul>
<b>Response Behavior:</b><br>
<ul>
<li>Returns array of found users</li>
<li>Order matches order of requested IDs</li>
<li>Non-existent or deleted users are silently omitted</li>
<li>Partial results returned if some IDs are invalid</li>
</ul>
<b>Performance Notes:</b><br>
Uses single database query with $in operator for optimal performance. Preferable to multiple individual user fetches.


### Example Usage

<!-- UsageSnippet language="python" operationID="getUsersByIds" method="post" path="/users/by-ids" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_by_ids(user_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_ids`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of user IDs to retrieve                                       | [<br/>"507f1f77bcf86cd799439011",<br/>"507f1f77bcf86cd799439012"<br/>] |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetUsersByIdsResponse](../../models/getusersbyidsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## exists_by_email

Check if a user account exists with the given email address. Used for pre-validation in registration and invitation flows.<br><br>
<b>Overview:</b><br>
This internal service endpoint validates email existence before creating accounts or sending invitations. It helps prevent duplicate accounts and validates recovery email addresses.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Pre-flight check before user invitation</li>
<li>Email validation during registration</li>
<li>Account recovery flow validation</li>
<li>Duplicate prevention checks</li>
</ul>
<b>Security Model:</b><br>
<ul>
<li>Requires scoped token with USER_LOOKUP privilege</li>
<li>Not accessible with regular bearer tokens</li>
<li>Typically called from internal services only</li>
</ul>
<b>Response Behavior:</b><br>
<ul>
<li>Returns matching users (including soft-deleted for recovery)</li>
<li>Empty array if no match found</li>
<li>Does not expose whether email exists to prevent enumeration</li>
</ul>
<b>Note:</b> May return soft-deleted users to support account recovery workflows.


### Example Usage

<!-- UsageSnippet language="python" operationID="checkUserExistsByEmail" method="get" path="/users/email/exists" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.users.exists_by_email(security=models.CheckUserExistsByEmailSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), email="john.smith@company.com", include_deleted=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.CheckUserExistsByEmailSecurity](../../models/checkuserexistsbyemailsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `email`                                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | Email address to check                                                                  | john.smith@company.com                                                                  |
| `include_deleted`                                                                       | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | Whether to include soft-deleted users                                                   |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.CheckUserExistsByEmailResponse](../../models/checkuserexistsbyemailresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_internal

Internal endpoint for service-to-service user lookup. Returns complete user data without privacy masking.<br><br>
<b>Overview:</b><br>
This internal endpoint provides full user data access for trusted backend services. Unlike public endpoints, it bypasses privacy controls and returns complete user information.<br><br>
<b>Security Model:</b><br>
<ul>
<li>Requires scoped token with USER_LOOKUP privilege</li>
<li>Not accessible via regular bearer tokens</li>
<li>Intended for trusted internal services only</li>
<li>All access is logged for audit purposes</li>
</ul>
<b>Intended Consumers:</b><br>
<ul>
<li>Email notification service</li>
<li>Analytics and reporting services</li>
<li>Audit logging service</li>
<li>Integration sync services</li>
</ul>
<b>Data Returned:</b><br>
Complete user object including fields that may be masked in public endpoints (email, phone, etc.).<br><br>
<b>Warning:</b><br>
This endpoint returns sensitive data. Ensure consuming services handle data according to privacy policies.


### Example Usage

<!-- UsageSnippet language="python" operationID="getInternalUser" method="get" path="/users/internal/{id}" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.users.get_internal(security=models.GetInternalUserSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.GetInternalUserSecurity](../../models/getinternalusersecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | User ID (24-character MongoDB ObjectId)                                   | 507f1f77bcf86cd799439011                                                  |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.GetInternalUserResponse](../../models/getinternaluserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_full_name

Update the full name of a user. This is a targeted update endpoint for changing only the display name without affecting other profile fields.<br><br>
<b>Overview:</b><br>
This endpoint updates a user's fullName field, which is their primary display name throughout the application. The firstName and lastName fields may also be updated based on name parsing logic.<br><br>
<b>Authorization:</b><br>
<ul>
<li><b>Self-update:</b> Users can update their own full name</li>
<li><b>Admin-update:</b> Admins can update any user's name</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Updates fullName field</li>
<li>May parse and update firstName/lastName</li>
<li>User update event published</li>
<li>Cached user data invalidated</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>User profile name change</li>
<li>Name correction by admin</li>
<li>Legal name update</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUserFullName" method="patch" path="/users/{id}/fullname" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.update_full_name(id="<id>", full_name="Jim Denesik")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `full_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.User](../../models/user.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_first_name

Update only the first name of a user without affecting other profile fields.<br><br>
<b>Overview:</b><br>
This targeted endpoint updates just the firstName field. Useful when you need fine-grained control over name components rather than updating the full name.<br><br>
<b>Authorization:</b><br>
<ul>
<li><b>Self-update:</b> Users can update their own first name</li>
<li><b>Admin-update:</b> Admins can update any user's first name</li>
</ul>
<b>Note:</b> This does NOT automatically update the fullName field. Use <code>/users/{id}/fullname</code> if you need to update the complete display name.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUserFirstName" method="patch" path="/users/{id}/firstName" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.update_first_name(id="507f1f77bcf86cd799439011", first_name="John")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `first_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | New first name                                                      | John                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateUserFirstNameResponse](../../models/updateuserfirstnameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_last_name

Update only the last name of a user without affecting other profile fields.<br><br>
<b>Overview:</b><br>
This targeted endpoint updates just the lastName field. Useful for fine-grained control over name components.<br><br>
<b>Authorization:</b><br>
<ul>
<li><b>Self-update:</b> Users can update their own last name</li>
<li><b>Admin-update:</b> Admins can update any user's last name</li>
</ul>
<b>Note:</b> This does NOT automatically update the fullName field. Use <code>/users/{id}/fullname</code> if you need to update the complete display name.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUserLastName" method="patch" path="/users/{id}/lastName" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.update_last_name(id="507f1f77bcf86cd799439011", last_name="Smith")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `last_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | New last name                                                       | Smith                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateUserLastNameResponse](../../models/updateuserlastnameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_designation

Update the job title or designation of a user.<br><br>
<b>Overview:</b><br>
This endpoint updates the user's designation field, which typically represents their job title, role, or position within the organization.<br><br>
<b>Authorization:</b><br>
<ul>
<li><b>Self-update:</b> Users can update their own designation</li>
<li><b>Admin-update:</b> Admins can update any user's designation</li>
</ul>
<b>Common Values:</b><br>
<ul>
<li>Software Engineer</li>
<li>Product Manager</li>
<li>Team Lead</li>
<li>Director of Engineering</li>
</ul>
<b>Display:</b><br>
Designation is shown in user profiles, team views, and organizational charts.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateUserDesignation" method="patch" path="/users/{id}/designation" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.update_designation(id="507f1f77bcf86cd799439011", designation="Senior Software Engineer")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `designation`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Job title or designation                                            | Senior Software Engineer                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateUserDesignationResponse](../../models/updateuserdesignationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## check_admin_status

Verify whether a specific user has administrative privileges in the organization.<br><br>
<b>Overview:</b><br>
This endpoint checks if the specified user belongs to an admin group and has elevated permissions. It's useful for authorization checks before performing admin-only operations.<br><br>
<b>What Makes a User an Admin:</b><br>
<ul>
<li>Member of a group with type "admin"</li>
<li>Has explicit admin role assignment</li>
<li>Organization owner (always admin)</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>UI permission checks before showing admin features</li>
<li>Pre-flight authorization validation</li>
<li>Access control for sensitive operations</li>
</ul>
<b>Response Codes:</b><br>
<ul>
<li><code>200</code>: User IS an admin</li>
<li><code>403</code>: User is NOT an admin</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="checkUserIsAdmin" method="get" path="/users/{id}/adminCheck" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.check_admin_status(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID to check for admin privileges                               | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CheckUserIsAdminResponse](../../models/checkuserisadminresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upload_display_picture

Upload or update the display picture (avatar) for the authenticated user.<br><br>
<b>Overview:</b><br>
This endpoint allows users to upload their profile picture. The image is processed, resized, and stored for use throughout the application.<br><br>
<b>File Requirements:</b><br>
<ul>
<li><b>Allowed types:</b> PNG, JPEG, JPG, WebP, GIF</li>
<li><b>Maximum size:</b> 1MB (1,048,576 bytes)</li>
<li><b>Recommended dimensions:</b> 256x256 pixels or larger</li>
<li><b>Aspect ratio:</b> Square recommended (will be cropped to square)</li>
</ul>
<b>Image Processing:</b><br>
<ul>
<li>Images are automatically resized to standard dimensions</li>
<li>Converted to JPEG for consistency and smaller file size</li>
<li>Multiple sizes may be generated (thumbnail, standard, large)</li>
<li>Original is not preserved</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Previous display picture is replaced</li>
<li>Cached images are invalidated</li>
<li>CDN cache may take time to update</li>
</ul>
<b>Authorization:</b><br>
Users can only upload their own display picture. Admins cannot upload on behalf of other users.


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadUserDisplayPicture" method="put" path="/users/dp" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.upload_display_picture(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `file`                                                                              | [models.UploadUserDisplayPictureFile](../../models/uploaduserdisplaypicturefile.md) | :heavy_check_mark:                                                                  | Image file (PNG, JPEG, WebP, or GIF, max 1MB)                                       |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_display_picture

Retrieve the current user's display picture image.<br><br>
<b>Overview:</b><br>
This endpoint returns the user's profile picture as binary image data. Use this for displaying the user's avatar in the application.<br><br>
<b>Response Format:</b><br>
<ul>
<li>Returns raw image data (not JSON)</li>
<li>Content-Type header indicates image format (typically image/jpeg)</li>
<li>Suitable for use directly in &lt;img&gt; src or CSS background</li>
</ul>
<b>Caching:</b><br>
<ul>
<li>Response includes cache headers for browser caching</li>
<li>Use ETag for conditional requests</li>
<li>Cache invalidated when picture is updated</li>
</ul>
<b>Alternative:</b><br>
For signed URL access, use the user profile endpoint which returns a <code>displayPictureUrl</code> field.


### Example Usage

<!-- UsageSnippet language="python" operationID="getUserDisplayPicture" method="get" path="/users/dp" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_display_picture()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserDisplayPictureResponse](../../models/getuserdisplaypictureresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## remove_display_picture

Remove the current user's display picture and revert to default avatar.<br><br>
<b>Overview:</b><br>
This endpoint permanently removes the user's uploaded profile picture. After removal, the user will display a default avatar (typically initials or generic icon).<br><br>
<b>What Happens:</b><br>
<ul>
<li>Profile picture file is deleted from storage</li>
<li>User profile updated to remove picture reference</li>
<li>Cached images invalidated</li>
<li>Default avatar will be shown in UI</li>
</ul>
<b>Note:</b><br>
This action is immediate and irreversible. To restore a picture, user must upload a new one.


### Example Usage

<!-- UsageSnippet language="python" operationID="removeUserDisplayPicture" method="delete" path="/users/dp" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.remove_display_picture()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoveUserDisplayPictureResponse](../../models/removeuserdisplaypictureresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## bulk_invite

Invite multiple users to the organization in a single operation. Ideal for onboarding entire teams at once.<br><br>
<b>Overview:</b><br>
This endpoint creates user accounts for multiple email addresses and sends invitation emails to all of them. It's the most efficient way to add multiple users to your organization.<br><br>
<b>Invitation Flow:</b><br>
<ol>
<li>Validate all email addresses</li>
<li>Check for existing accounts (skip duplicates)</li>
<li>Create user accounts for new emails</li>
<li>Restore any previously deleted accounts</li>
<li>Add users to specified groups (optional)</li>
<li>Send invitation emails to all new users</li>
</ol>
<b>Requirements:</b><br>
<ul>
<li><b>Account Type:</b> Business accounts only (not individual)</li>
<li><b>SMTP:</b> Email configuration must be set up</li>
<li><b>Authorization:</b> Admin privileges required</li>
</ul>
<b>Email Processing:</b><br>
<ul>
<li>Duplicate emails are automatically skipped</li>
<li>Invalid email formats are rejected</li>
<li>Existing users are not re-invited (use resend-invite)</li>
<li>Previously deleted users are restored</li>
</ul>
<b>Response Details:</b><br>
Response includes count of successful invites and any failures with reasons.


### Example Usage

<!-- UsageSnippet language="python" operationID="bulkInviteUsers" method="post" path="/users/bulk/invite" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.bulk_invite(emails=[
        "user1@company.com",
        "user2@company.com",
    ], group_ids=[
        "507f1f77bcf86cd799439011",
    ], send_email=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `emails`                                                            | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of email addresses to invite (max 100)                        | [<br/>"user1@company.com",<br/>"user2@company.com"<br/>]            |
| `group_ids`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | Optional group IDs to add all invited users to                      | [<br/>"507f1f77bcf86cd799439011"<br/>]                              |
| `send_email`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether to send invitation emails immediately                       |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.BulkInviteUsersResponse](../../models/bulkinviteusersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## resend_invite

Resend the invitation email to a user who hasn't completed their account setup.<br><br>
<b>Overview:</b><br>
This endpoint resends the invitation email to a user who was previously invited but hasn't logged in yet. Useful when the original invitation email was lost, expired, or ended up in spam.<br><br>
<b>When to Use:</b><br>
<ul>
<li>User didn't receive original invitation</li>
<li>Invitation link expired</li>
<li>User forgot to complete setup</li>
<li>Email went to spam folder</li>
</ul>
<b>Requirements:</b><br>
<ul>
<li>User must exist in the system</li>
<li>User must NOT have logged in yet (hasLoggedIn: false)</li>
<li>SMTP configuration must be active</li>
<li>Admin privileges required</li>
</ul>
<b>What Happens:</b><br>
<ul>
<li>Generates a new invitation token</li>
<li>Invalidates any previous invitation links</li>
<li>Sends new invitation email</li>
<li>Resets invitation expiry timer</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="resendUserInvite" method="post" path="/users/{id}/resend-invite" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.resend_invite(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID of the user to resend invitation to                         | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ResendUserInviteResponse](../../models/resenduserinviteresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## list_with_graph

Retrieve a paginated list of users with enhanced search capabilities using the graph service.<br><br>
<b>Overview:</b><br>
This endpoint provides advanced user listing with full-text search, pagination, and optional relationship data from the knowledge graph. It's optimized for large organizations with thousands of users.<br><br>
<b>Search Capabilities:</b><br>
<ul>
<li>Full-text search across name and email</li>
<li>Fuzzy matching for typo tolerance</li>
<li>Results ranked by relevance</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>User directory with search</li>
<li>Autocomplete user selection</li>
<li>Admin user management lists</li>
<li>User analytics dashboards</li>
</ul>
<b>Performance:</b><br>
<ul>
<li>Powered by graph database for fast queries</li>
<li>Supports pagination for large datasets</li>
<li>Results cached for repeated queries</li>
</ul>
<b>vs /users endpoint:</b><br>
Use this endpoint when you need advanced search or are dealing with large user bases. Use <code>/users</code> for simple full-list retrieval.


### Example Usage

<!-- UsageSnippet language="python" operationID="listUsersGraph" method="get" path="/users/graph/list" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.list_with_graph(page=1, limit=10, search="john", sort_by="fullName", sort_order="asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `page`                                                                              | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | Page number (1-based)                                                               |                                                                                     |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | Number of results per page                                                          |                                                                                     |
| `search`                                                                            | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Search query (searches name and email)                                              | john                                                                                |
| `sort_by`                                                                           | [Optional[models.ListUsersGraphSortBy]](../../models/listusersgraphsortby.md)       | :heavy_minus_sign:                                                                  | Field to sort by                                                                    |                                                                                     |
| `sort_order`                                                                        | [Optional[models.ListUsersGraphSortOrder]](../../models/listusersgraphsortorder.md) | :heavy_minus_sign:                                                                  | Sort direction                                                                      |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.ListUsersGraphResponse](../../models/listusersgraphresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_teams

Get teams that the current user belongs to

### Example Usage

<!-- UsageSnippet language="python" operationID="getCurrentUserTeams" method="get" path="/users/teams/list" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.get_teams()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Team]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |