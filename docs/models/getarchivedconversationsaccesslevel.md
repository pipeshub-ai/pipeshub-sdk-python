# GetArchivedConversationsAccessLevel

Computed per request. The requester's effective access level:
their entry in `sharedWith`, or `read` by default.


## Example Usage

```python
from pipeshub_sdk.models import GetArchivedConversationsAccessLevel

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetArchivedConversationsAccessLevel = "read"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"read"`
- `"write"`
