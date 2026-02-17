<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from pipeshub import Pipeshub

async def main():

    async with Pipeshub(
        server_url="https://api.example.com",
    ) as p_client:

        res = await p_client.user_account.init_auth_async(email="user@example.com")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->