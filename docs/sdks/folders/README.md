# Folders

## Overview

Folder organization and management

### Available Operations

* [create_root_folder](#create_root_folder) - Create root folder
* [get_folder_contents](#get_folder_contents) - Get folder contents
* [update_folder](#update_folder) - Update folder
* [delete_folder](#delete_folder) - Delete folder
* [get_folder_children](#get_folder_children) - Get folder children (alias for folder contents)
* [create_subfolder](#create_subfolder) - Create subfolder

## create_root_folder

Create a new folder at the root level of a knowledge base.<br><br>
<b>Required Permission:</b> FILEORGANIZER or higher<br><br>
<b>Folder Features:</b><br>
<ul>
<li>Organize records hierarchically</li>
<li>Support nested subfolders</li>
<li>Inherit parent KB permissions</li>
</ul>
<b>Naming Rules:</b><br>
<ul>
<li>1-255 characters</li>
<li>XSS protection applied</li>
<li>Can contain spaces and special characters</li>
</ul>


### Example Usage

<!-- UsageSnippet language="python" operationID="createRootFolder" method="post" path="/knowledgeBase/{kbId}/folder" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.folders.create_root_folder(kb_id="<id>", folder_name="Project Documents")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Knowledge base ID                                                   |                                                                     |
| `folder_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name of the folder                                                  | Project Documents                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Folder](../../models/folder.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_folder_contents

Retrieve the contents of a folder including subfolders and records.<br><br>
<b>Overview:</b><br>
Returns paginated list of records within the folder, with same filtering options as KB-level record listing.<br><br>
<b>Navigation:</b><br>
Use this endpoint to browse folder hierarchies. Response includes folder metadata and child items.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFolderContents" method="get" path="/knowledgeBase/{kbId}/folder/{folderId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.folders.get_folder_contents(kb_id="<id>", folder_id="<id>", page=1, limit=20, sort_by="createdAtTimestamp", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `kb_id`                                                                                   | *str*                                                                                     | :heavy_check_mark:                                                                        | Knowledge base ID                                                                         |
| `folder_id`                                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | Folder ID                                                                                 |
| `page`                                                                                    | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `search`                                                                                  | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `sort_by`                                                                                 | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `sort_order`                                                                              | [Optional[models.GetFolderContentsSortOrder]](../../models/getfoldercontentssortorder.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.RecordsResponse](../../models/recordsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## update_folder

Rename a folder.<br><br>
<b>Required Permission:</b> FILEORGANIZER or higher


### Example Usage

<!-- UsageSnippet language="python" operationID="updateFolder" method="put" path="/knowledgeBase/{kbId}/folder/{folderId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.folders.update_folder(kb_id="<id>", folder_id="<id>", folder_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Folder](../../models/folder.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## delete_folder

Delete a folder and all its contents.<br><br>
<b>Required Permission:</b> FILEORGANIZER or higher<br><br>
<b>Cascade Delete:</b><br>
All subfolders and records within will be permanently deleted.<br><br>
<b>Warning:</b> This action is irreversible.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteFolder" method="delete" path="/knowledgeBase/{kbId}/folder/{folderId}" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    pipeshub.folders.delete_folder(kb_id="<id>", folder_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## get_folder_children

Retrieve the children (subfolders and records) of a folder.<br><br>
<b>Overview:</b><br>
This is an alias endpoint for <code>/knowledgeBase/{kbId}/folder/{folderId}</code>. Returns paginated list of records within the folder, with same filtering options as KB-level record listing.<br><br>
<b>Navigation:</b><br>
Use this endpoint to browse folder hierarchies. Response includes folder metadata and child items.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFolderChildren" method="get" path="/knowledgeBase/{kbId}/folder/{folderId}/children" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.folders.get_folder_children(kb_id="<id>", folder_id="<id>", page=1, limit=20, sort_by="createdAtTimestamp", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `kb_id`                                                                                   | *str*                                                                                     | :heavy_check_mark:                                                                        | Knowledge base ID                                                                         |
| `folder_id`                                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | Folder ID                                                                                 |
| `page`                                                                                    | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `search`                                                                                  | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `sort_by`                                                                                 | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `sort_order`                                                                              | [Optional[models.GetFolderChildrenSortOrder]](../../models/getfolderchildrensortorder.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.RecordsResponse](../../models/recordsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## create_subfolder

Create a nested folder within an existing folder.<br><br>
<b>Required Permission:</b> FILEORGANIZER or higher<br><br>
<b>Nesting:</b><br>
Supports unlimited folder nesting depth for complex organizational structures.


### Example Usage

<!-- UsageSnippet language="python" operationID="createSubfolder" method="post" path="/knowledgeBase/{kbId}/folder/{folderId}/subfolder" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.folders.create_subfolder(kb_id="<id>", folder_id="<id>", folder_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `kb_id`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Parent folder ID                                                    |
| `folder_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Folder](../../models/folder.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |