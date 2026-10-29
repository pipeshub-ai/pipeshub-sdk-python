<!-- Start SDK Example Usage [usage] -->
### Retrieve passages with citations

```python
# Synchronous Example
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.semantic_search.retrieve(query="how do we roll back a canary?", limit=8, rewrite_query=False)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os
from pipeshub_sdk import Pipeshub, models

async def main():

    async with Pipeshub(
        security=models.Security(
            bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
        ),
    ) as pipeshub:

        res = await pipeshub.semantic_search.retrieve_async(query="how do we roll back a canary?", limit=8, rewrite_query=False)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->