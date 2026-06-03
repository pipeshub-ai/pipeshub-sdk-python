<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.o_auth_provider.oauth_token(grant_type="client_credentials")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from pipeshub_sdk import Pipeshub

async def main():

    async with Pipeshub() as pipeshub:

        res = await pipeshub.o_auth_provider.oauth_token_async(grant_type="client_credentials")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->