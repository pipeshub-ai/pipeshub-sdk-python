# AgentConversationStatus

Same values as `Conversation.status`.

## Example Usage

```python
from pipeshub_sdk.models import AgentConversationStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentConversationStatus = "None"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"None"`
- `"Inprogress"`
- `"Complete"`
- `"Failed"`
- `"Stopped"`
