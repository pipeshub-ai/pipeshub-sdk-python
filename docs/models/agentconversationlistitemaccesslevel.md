# AgentConversationListItemAccessLevel

Computed per request from `sharedWith`; defaults to `read` when no
explicit share grant is attached to the serialized row.


## Example Usage

```python
from pipeshub_sdk.models import AgentConversationListItemAccessLevel

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentConversationListItemAccessLevel = "read"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"read"`
- `"write"`
