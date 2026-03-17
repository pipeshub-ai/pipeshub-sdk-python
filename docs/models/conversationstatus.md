# ConversationStatus

Current status of the conversation:
<ul>
<li><code>INPROGRESS</code> - AI is processing</li>
<li><code>COMPLETED</code> - Response ready</li>
<li><code>FAILED</code> - Error occurred</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import ConversationStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConversationStatus = "INPROGRESS"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"INPROGRESS"`
- `"COMPLETED"`
- `"FAILED"`
