# UpdateConversationTitleStatus

Current status of the conversation:
- `None` — no activity yet
- `Inprogress` — AI is processing
- `Complete` — response ready
- `Failed` — error occurred
- `Stopped` — cancelled, or the client disconnected mid-answer


## Example Usage

```python
from pipeshub_sdk.models import UpdateConversationTitleStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UpdateConversationTitleStatus = "None"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"None"`
- `"Inprogress"`
- `"Complete"`
- `"Failed"`
- `"Stopped"`
