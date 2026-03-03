# Organizations

## Overview

Organization management operations

### Available Operations

* [check_org_exists](#check_org_exists) - Check if organization exists
* [create_organization](#create_organization) - Create organization
* [get_current_organization](#get_current_organization) - Get current organization
* [update_organization](#update_organization) - Update organization
* [delete_organization](#delete_organization) - Delete organization
* [upload_organization_logo](#upload_organization_logo) - Upload organization logo
* [get_organization_logo](#get_organization_logo) - Get organization logo
* [delete_organization_logo](#delete_organization_logo) - Delete organization logo
* [get_onboarding_status](#get_onboarding_status) - Get onboarding status
* [update_onboarding_status](#update_onboarding_status) - Update onboarding status

## check_org_exists

Check if any organization has been created in the system. This is typically the first API call made during initial setup.<br><br>
<b>Overview:</b><br>
This public endpoint determines whether the system has been initialized with an organization. Used by the frontend to decide whether to show the setup wizard or the login screen.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>First-time setup detection</li>
<li>Onboarding flow decisions</li>
<li>System initialization checks</li>
</ul>
<b>Response:</b><br>
<ul>
<li><code>exists: true</code> - Organization exists, show login</li>
<li><code>exists: false</code> - No organization, show setup wizard</li>
</ul>
<b>Note:</b> This endpoint requires no authentication and is publicly accessible.


### Example Usage

<!-- UsageSnippet language="python" operationID="checkOrgExists" method="get" path="/org/exists" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.organizations.check_org_exists()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckOrgExistsResponse](../../models/checkorgexistsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_organization

Create a new organization and its first admin user. This is the initial setup endpoint for new PipesHub installations.<br><br>
<b>Overview:</b><br>
This endpoint performs the complete initial setup of a PipesHub instance, including creating the organization entity and its first administrator account. Should only be called once during initial setup.<br><br>
<b>Setup Flow:</b><br>
<ol>
<li>Frontend calls <code>/org/exists</code> to check if setup is needed</li>
<li>If no organization exists, show setup wizard</li>
<li>Collect organization and admin details</li>
<li>Call this endpoint to create organization</li>
<li>User is automatically logged in as admin</li>
</ol>
<b>What Gets Created:</b><br>
<ul>
<li>Organization entity with provided details</li>
<li>Admin user account with provided credentials</li>
<li>Default user groups (admin, everyone)</li>
<li>Default system settings</li>
<li>Initial authentication configuration</li>
</ul>
<b>Account Types:</b><br>
<ul>
<li><code>individual</code>: Single-user account, limited team features</li>
<li><code>business</code>: Multi-user organization with full features</li>
</ul>
<b>Security:</b><br>
<ul>
<li>This endpoint only works if no organization exists</li>
<li>Password must meet security requirements</li>
<li>Email verification may be required based on config</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createOrganization" method="post" path="/org" -->
```python
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.organizations.create_organization(account_type="business", contact_email="admin@acme.com", admin_full_name="John Smith", password="SecurePassword123!", short_name="Acme", registered_name="Acme Corporation Inc.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `account_type`                                                                        | [models.CreateOrganizationAccountType](../../models/createorganizationaccounttype.md) | :heavy_check_mark:                                                                    | Type of organization account                                                          | business                                                                              |
| `contact_email`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | Primary contact email (also used as admin email)                                      | admin@acme.com                                                                        |
| `admin_full_name`                                                                     | *str*                                                                                 | :heavy_check_mark:                                                                    | Full name of the first admin user                                                     | John Smith                                                                            |
| `password`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | Password for the admin account (min 8 chars)                                          | SecurePassword123!                                                                    |
| `short_name`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Short display name for the organization                                               | Acme                                                                                  |
| `registered_name`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Official registered name (for business accounts)                                      | Acme Corporation Inc.                                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.CreateOrganizationResponse](../../models/createorganizationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_current_organization

Retrieve details about the authenticated user's organization.<br><br>
<b>Overview:</b><br>
This endpoint returns complete information about the current user's organization, including profile data, settings, and configuration. Use this for organization profile pages and settings.<br><br>
<b>Response Includes:</b><br>
<ul>
<li>Organization profile (name, email, address)</li>
<li>Account type and billing status</li>
<li>Feature flags and limits</li>
<li>Branding settings (logo, colors)</li>
<li>Creation and modification timestamps</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Organization profile pages</li>
<li>Settings and configuration screens</li>
<li>Billing and subscription displays</li>
<li>White-label branding retrieval</li>
</ul>
<b>Note:</b><br>
All authenticated users can access this endpoint to view their organization's details.


### Example Usage

<!-- UsageSnippet language="python" operationID="getCurrentOrganization" method="get" path="/org" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.get_current_organization()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_organization

Update organization profile and settings information.<br><br>
<b>Overview:</b><br>
This endpoint allows administrators to update the organization's profile information, contact details, and address. Used in the organization settings section of the admin panel.<br><br>
<b>Updatable Fields:</b><br>
<ul>
<li><code>registeredName</code>: Official registered/legal name of the organization</li>
<li><code>shortName</code>: Short display name used in UI</li>
<li><code>phoneNumber</code>: Primary contact phone number</li>
<li><code>permanentAddress</code>: Full address object with street, city, state, country, postal code</li>
</ul>
<b>Restrictions:</b><br>
<ul>
<li>Only organization admins can perform updates</li>
<li>Contact email cannot be changed through this endpoint</li>
<li>Account type cannot be changed after creation</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Organization update event is published</li>
<li>Cached organization data is invalidated</li>
<li>Changes are reflected immediately across all services</li>
</ul>
<b>Validation:</b><br>
<ul>
<li>Phone number must be valid international format</li>
<li>Address fields have maximum length constraints</li>
<li>Names cannot be empty if provided</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateOrganization" method="put" path="/org" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.update_organization(registered_name="Acme Corporation Inc.", short_name="Acme Corp", phone_number="+15551234567")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `registered_name`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Official registered/legal name                                      | Acme Corporation Inc.                                               |
| `short_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Short display name for UI                                           | Acme Corp                                                           |
| `phone_number`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Contact phone number (international format)                         | +15551234567                                                        |
| `permanent_address`                                                 | [Optional[models.Address]](../../models/address.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateOrganizationResponse](../../models/updateorganizationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_organization

Permanently delete an organization and all associated data.<br><br>
<b>WARNING:</b> This action is <b>irreversible</b>.<br><br>
<b>Data Deleted:</b><br>
<ul>
<li>All user accounts in the organization</li>
<li>All teams and user groups</li>
<li>All documents and storage data</li>
<li>All configuration and settings</li>
</ul>
<b>Requirements:</b><br>
<ul>
<li>Must be the organization owner (super admin)</li>
<li>Must provide confirmation parameter</li>
<li>All active subscriptions must be cancelled first</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOrganization" method="delete" path="/org" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.delete_organization(confirm="DELETE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `confirm`                                                           | [models.Confirm](../../models/confirm.md)                           | :heavy_check_mark:                                                  | Must be "DELETE" to confirm deletion                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOrganizationResponse](../../models/deleteorganizationresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## upload_organization_logo

Upload or update the organization's logo image.<br><br>
<b>Supported Formats:</b><br>
<ul>
<li>PNG (recommended for transparency)</li>
<li>JPG/JPEG</li>
<li>SVG</li>
<li>WebP</li>
</ul>
<b>Requirements:</b><br>
<ul>
<li>Maximum file size: 5MB</li>
<li>Recommended dimensions: 256x256 pixels or higher</li>
<li>Square aspect ratio recommended</li>
</ul>
<b>Side Effects:</b><br>
<ul>
<li>Previous logo is replaced</li>
<li>Multiple sizes may be generated for different use cases</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="uploadOrganizationLogo" method="put" path="/org/logo" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.upload_organization_logo(logo={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `logo`                                                              | [models.Logo](../../models/logo.md)                                 | :heavy_check_mark:                                                  | Logo image file                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadOrganizationLogoResponse](../../models/uploadorganizationlogoresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_organization_logo

Retrieve the organization's logo image or URL.<br><br>
<b>Response Formats:</b><br>
<ul>
<li>Returns a signed URL to access the logo</li>
<li>URL is valid for a limited time (typically 1 hour)</li>
</ul>
<b>Use Cases:</b><br>
<ul>
<li>Displaying logo in navigation/header</li>
<li>Email templates</li>
<li>White-label branding</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationLogo" method="get" path="/org/logo" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.get_organization_logo()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOrganizationLogoResponse](../../models/getorganizationlogoresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_organization_logo

Remove the organization's custom logo.<br><br>
<b>Behavior:</b><br>
<ul>
<li>Logo file is permanently deleted from storage</li>
<li>Organization reverts to default/placeholder logo</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOrganizationLogo" method="delete" path="/org/logo" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.delete_organization_logo()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteOrganizationLogoResponse](../../models/deleteorganizationlogoresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_onboarding_status

Retrieve the organization's onboarding progress and status.<br><br>
<b>Response Details:</b><br>
<ul>
<li>Current onboarding step</li>
<li>Completion status of each step</li>
<li>Overall completion percentage</li>
</ul>
<b>Onboarding Steps:</b><br>
<ul>
<li>Organization profile setup</li>
<li>Admin account configuration</li>
<li>Invite team members</li>
<li>Connect integrations</li>
<li>Configure settings</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="getOnboardingStatus" method="get" path="/org/onboarding-status" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.get_onboarding_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOnboardingStatusResponse](../../models/getonboardingstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_onboarding_status

Update the organization's onboarding progress.<br><br>
<b>Use Cases:</b><br>
<ul>
<li>Mark a step as completed</li>
<li>Skip optional steps</li>
<li>Complete entire onboarding</li>
</ul>
<b>Behavior:</b><br>
<ul>
<li>Steps must be completed in order (unless skippable)</li>
<li>Completing all required steps marks onboarding as complete</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="updateOnboardingStatus" method="put" path="/org/onboarding-status" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.organizations.update_onboarding_status(step_id="invite_team", action="complete")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the step to update                                            | invite_team                                                         |
| `action`                                                            | [models.Action](../../models/action.md)                             | :heavy_check_mark:                                                  | Action to perform on the step                                       | complete                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdateOnboardingStatusResponse](../../models/updateonboardingstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |