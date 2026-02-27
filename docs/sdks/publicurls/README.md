# PublicURLs

## Overview

Configure public URLs for frontend application and connector callbacks.

### Available Operations

* [set_frontend_public_url](#set_frontend_public_url) - Set frontend public URL
* [get_frontend_public_url](#get_frontend_public_url) - Get frontend public URL
* [set_connector_public_url](#set_connector_public_url) - Set connector public URL
* [get_connector_public_url](#get_connector_public_url) - Get connector public URL

## set_frontend_public_url

Configure the public URL where the frontend application is accessible. Used for OAuth redirects and email links.

### Example Usage

<!-- UsageSnippet language="python" operationID="setFrontendPublicUrl" method="post" path="/configurationManager/frontendPublicUrl" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.public_ur_ls.set_frontend_public_url(security=models.SetFrontendPublicURLSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), url="https://app.example.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.SetFrontendPublicURLSecurity](../../models/setfrontendpublicurlsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `url`                                                                               | *str*                                                                               | :heavy_check_mark:                                                                  | Public URL                                                                          | https://app.example.com                                                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_frontend_public_url

Get frontend public URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFrontendPublicUrl" method="get" path="/configurationManager/frontendPublicUrl" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.public_ur_ls.get_frontend_public_url(security=models.GetFrontendPublicURLSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [models.GetFrontendPublicURLSecurity](../../getfrontendpublicurlsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.URLConfig](../../models/urlconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## set_connector_public_url

Configure the public URL for connector OAuth callbacks.

### Example Usage

<!-- UsageSnippet language="python" operationID="setConnectorPublicUrl" method="post" path="/configurationManager/connectorPublicUrl" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    p_client.public_ur_ls.set_connector_public_url(security=models.SetConnectorPublicURLSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), url="https://app.example.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.SetConnectorPublicURLSecurity](../../models/setconnectorpublicurlsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |                                                                                       |
| `url`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | Public URL                                                                            | https://app.example.com                                                               |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_connector_public_url

Get connector public URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnectorPublicUrl" method="get" path="/configurationManager/connectorPublicUrl" -->
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.public_ur_ls.get_connector_public_url(security=models.GetConnectorPublicURLSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [models.GetConnectorPublicURLSecurity](../../getconnectorpublicurlsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.URLConfig](../../models/urlconfig.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |