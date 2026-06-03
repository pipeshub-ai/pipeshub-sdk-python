# Organizations

## Overview

Organization management operations

### Available Operations

* [get_current_organization](#get_current_organization) - Get current organization

## get_current_organization

Retrieve details about the authenticated user's organization.

**Overview:**

This endpoint returns the organization document for the current user's org, including profile data and configuration.

**Response Includes:**

- Organization profile (registeredName, shortName, contactEmail, domain)
- Account type
- Onboarding status
- Permanent address
- Creation and modification timestamps

**Use Cases:**

- Organization profile pages
- Settings and configuration screens


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
| errors.ErrorResponse        | 401, 404                    | application/json            |
| errors.ErrorResponse        | 500                         | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |