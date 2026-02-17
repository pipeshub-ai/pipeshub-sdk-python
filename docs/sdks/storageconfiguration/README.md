# StorageConfiguration

## Overview

### Available Operations

* [create_local](#create_local) - Configure Local Storage
* [create_s3](#create_s3) - Configure AWS S3 Storage
* [create_azure_blob_config](#create_azure_blob_config) - Configure Azure Blob Storage
* [get](#get) - Get current storage configuration

## create_local

Configure local filesystem as the storage backend for file uploads and document storage. Suitable for development or on-premise deployments.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLocalStorageConfig" method="post" path="/configurationManager/storageConfig#local" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.storage_configuration.create_local(storage_type="local", mount_name="PipesHub", base_url="http://localhost:3000/storage")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `storage_type`                                                                                    | [models.CreateLocalStorageConfigStorageType](../../models/createlocalstorageconfigstoragetype.md) | :heavy_check_mark:                                                                                | Storage type identifier                                                                           | local                                                                                             |
| `mount_name`                                                                                      | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Mount point name for local storage directory                                                      | PipesHub                                                                                          |
| `base_url`                                                                                        | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Base URL for accessing locally stored files                                                       | http://localhost:3000/storage                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_s3

Configure AWS S3 as the storage backend for file uploads and document storage. Requires an S3 bucket and IAM credentials with appropriate permissions.

### Example Usage

<!-- UsageSnippet language="python" operationID="createS3StorageConfig" method="post" path="/configurationManager/storageConfig#s3" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.storage_configuration.create_s3(storage_type="s3", s3_access_key_id="AKIAIOSFODNN7EXAMPLE", s3_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", s3_region="us-east-1", s3_bucket_name="my-pipeshub-bucket")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `storage_type`                                                                              | [models.CreateS3StorageConfigStorageType](../../models/creates3storageconfigstoragetype.md) | :heavy_check_mark:                                                                          | Storage type identifier                                                                     | s3                                                                                          |
| `s3_access_key_id`                                                                          | *str*                                                                                       | :heavy_check_mark:                                                                          | AWS IAM access key ID with S3 permissions                                                   | AKIAIOSFODNN7EXAMPLE                                                                        |
| `s3_secret_access_key`                                                                      | *str*                                                                                       | :heavy_check_mark:                                                                          | AWS IAM secret access key                                                                   | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY                                                    |
| `s3_region`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | AWS region where the S3 bucket is located                                                   | us-east-1                                                                                   |
| `s3_bucket_name`                                                                            | *str*                                                                                       | :heavy_check_mark:                                                                          | Name of the S3 bucket for storing files                                                     | my-pipeshub-bucket                                                                          |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_azure_blob_config

Configure Azure Blob Storage as the storage backend. You can provide either:
- A full connection string (azureBlobConnectionString), OR
- Individual credentials (accountName, accountKey, endpointProtocol, endpointSuffix)


### Example Usage

<!-- UsageSnippet language="python" operationID="createAzureBlobStorageConfig" method="post" path="/configurationManager/storageConfig#azureBlob" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    p_client.storage_configuration.create_azure_blob_config(storage_type="azureBlob", container_name="pipeshub-files", azure_blob_connection_string="DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net", account_name="mystorageaccount", account_key="base64encodedaccountkey==", endpoint_protocol="https", endpoint_suffix="core.windows.net")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `storage_type`                                                                                            | [models.CreateAzureBlobStorageConfigStorageType](../../models/createazureblobstorageconfigstoragetype.md) | :heavy_check_mark:                                                                                        | Storage type identifier                                                                                   | azureBlob                                                                                                 |
| `container_name`                                                                                          | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Azure Blob container name for storing files                                                               | pipeshub-files                                                                                            |
| `azure_blob_connection_string`                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Full Azure Blob connection string. If provided, accountName and accountKey are not required.              | DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net     |
| `account_name`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Azure storage account name. Required if not using connection string.                                      | mystorageaccount                                                                                          |
| `account_key`                                                                                             | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Azure storage account access key. Required if not using connection string.                                | base64encodedaccountkey==                                                                                 |
| `endpoint_protocol`                                                                                       | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Protocol for Azure Blob endpoint                                                                          | https                                                                                                     |
| `endpoint_suffix`                                                                                         | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Azure endpoint suffix                                                                                     | core.windows.net                                                                                          |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get

Retrieve the current storage backend configuration. Returns the configuration for whichever storage type is currently active (Local, S3, or Azure Blob).

### Example Usage

<!-- UsageSnippet language="python" operationID="getStorageConfig" method="get" path="/configurationManager/storageConfig" -->
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.storage_configuration.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageConfigResponse](../../models/getstorageconfigresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |