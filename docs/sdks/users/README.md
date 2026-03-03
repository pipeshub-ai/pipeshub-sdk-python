# Users

## Overview

User management operations

### Available Operations

* [get_all_users](#get_all_users) - Get all users
* [create_user](#create_user) - Create a new user
* [get_user_by_id](#get_user_by_id) - Get user by ID
* [update_user](#update_user) - Update user
* [delete_user](#delete_user) - Delete user
* [get_user_email_by_id](#get_user_email_by_id) - Get user email by ID
* [~~update_email~~](#update_email) - Update user email :warning: **Deprecated**
* [upload_user_display_picture](#upload_user_display_picture) - Upload display picture
* [get_user_display_picture](#get_user_display_picture) - Get display picture
* [remove_user_display_picture](#remove_user_display_picture) - Remove display picture
* [bulk_invite_users](#bulk_invite_users) - Bulk invite users
* [resend_user_invite](#resend_user_invite) - Resend user invite
* [list_users_graph](#list_users_graph) - List users (paginated with graph data)
* [unblock_user](#unblock_user) - Unblock a user in organization
* [get_all_users_with_groups](#get_all_users_with_groups) - Get all users with groups
* [~~get_users_by_ids~~](#get_users_by_ids) - Get users by IDs :warning: **Deprecated**
* [~~update_full_name~~](#update_full_name) - Update user full name :warning: **Deprecated**
* [~~update_first_name~~](#update_first_name) - Update user first name :warning: **Deprecated**
* [~~update_last_name~~](#update_last_name) - Update user last name :warning: **Deprecated**
* [~~update_designation~~](#update_designation) - Update user designation :warning: **Deprecated**
* [~~admin_check~~](#admin_check) - Check if user is admin :warning: **Deprecated**
* [~~get_user_teams_via_users~~](#get_user_teams_via_users) - Get user teams :warning: **Deprecated**

## get_all_users

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_all_users(page=1, limit=50)

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

**[List[models.User]](../../models/.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_user

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.create_user(full_name="John Smith", email="john.smith@company.com", mobile="+15551234567", designation="Software Engineer", send_invite=True)

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

## get_user_by_id

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_user_by_id(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID (24-character MongoDB ObjectId)                             | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.User](../../models/user.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_user

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.update_user(id="507f1f77bcf86cd799439011", full_name="John Smith", first_name="John", last_name="Smith", email="john.smith@company.com", mobile="+15551234567", designation="Senior Software Engineer")

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

## delete_user

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.delete_user(id="507f1f77bcf86cd799439011")

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

## get_user_email_by_id

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_user_email_by_id(id="507f1f77bcf86cd799439011")

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

## ~~update_email~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update the email address of a user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateEmail" method="patch" path="/users/{id}/email" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.users.update_email(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `email`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upload_user_display_picture

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.upload_user_display_picture(file={
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

## get_user_display_picture

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_user_display_picture()

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

## remove_user_display_picture

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.remove_user_display_picture()

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

## bulk_invite_users

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.bulk_invite_users(emails=[
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

## resend_user_invite

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.resend_user_invite(id="507f1f77bcf86cd799439011")

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

## list_users_graph

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
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.list_users_graph(page=1, limit=10, search="john", sort_by="fullName", sort_order="asc")

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

## unblock_user

Unblock a previously blocked user within the authenticated administrator's organization.<br><br>

<b>Overview:</b><br>
This endpoint updates the user's credential record by setting <code>isBlocked</code> to <code>false</code> 
and resetting <code>wrongCredentialCount</code> to <code>0</code>.<br><br>

<b>Authorization:</b><br>
<ul>
<li><b>Admin only:</b> Only organization administrators can unblock users</li>
<li>Requires a valid Bearer token</li>
</ul>

<b>Validation & Conditions:</b><br>
<ul>
<li>User must belong to the same <code>orgId</code> as the authenticated admin</li>
<li>User must currently be blocked (<code>isBlocked: true</code>)</li>
<li>User must not be deleted (<code>isDeleted: false</code>)</li>
</ul>

<b>Note:</b> If the user is not blocked or does not exist in the organization, a 404 response is returned.


### Example Usage

<!-- UsageSnippet language="python" operationID="unblockUser" method="put" path="/users/{id}/unblock" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.unblock_user(id="507f1f77bcf86cd799439011")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | User ID to unblock                                                  | 507f1f77bcf86cd799439011                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnblockUserResponse](../../models/unblockuserresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_all_users_with_groups

Retrieve all users in the organization along with their group memberships.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllUsersWithGroups" method="get" path="/users/fetch/with-groups" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_all_users_with_groups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAllUsersWithGroupsResponse](../../models/getalluserswithgroupsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_users_by_ids~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve multiple users by their IDs in a single request.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsersByIds" method="post" path="/users/by-ids" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_users_by_ids()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUsersByIdsResponse](../../models/getusersbyidsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~update_full_name~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update the full name of a user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateFullName" method="patch" path="/users/{id}/fullname" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.update_full_name(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `full_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateFullNameResponse](../../models/updatefullnameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~update_first_name~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update the first name of a user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateFirstName" method="patch" path="/users/{id}/firstName" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.update_first_name(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `first_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateFirstNameResponse](../../models/updatefirstnameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~update_last_name~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update the last name of a user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLastName" method="patch" path="/users/{id}/lastName" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.update_last_name(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `last_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateLastNameResponse](../../models/updatelastnameresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~update_designation~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Update the designation/title of a user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDesignation" method="patch" path="/users/{id}/designation" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.update_designation(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `designation`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateDesignationResponse](../../models/updatedesignationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~admin_check~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Check whether the specified user has admin privileges. Returns 200 OK if the user is an admin.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="adminCheck" method="get" path="/users/{id}/adminCheck" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.admin_check(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AdminCheckResponse](../../models/admincheckresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## ~~get_user_teams_via_users~~

<b>⚠️ Deprecated:</b> This endpoint is deprecated and will be removed in a future release.<br><br>
Retrieve teams associated with the authenticated user.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserTeamsViaUsers" method="get" path="/users/teams/list" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.users.get_user_teams_via_users()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserTeamsViaUsersResponse](../../models/getuserteamsviausersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |