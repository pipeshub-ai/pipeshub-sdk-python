<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from pipeshub_sdk import Pipeshub


with Pipeshub() as pipeshub:

    res = pipeshub.user_account.init_auth(email="user@example.com")

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

        res = await pipeshub.user_account.init_auth_async(email="user@example.com")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->