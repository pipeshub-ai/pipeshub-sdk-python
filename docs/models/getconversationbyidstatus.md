# GetConversationByIDStatus

Current status of the conversation:
<ul>
<li><code>INPROGRESS</code> - AI is processing</li>
<li><code>COMPLETED</code> - Response ready</li>
<li><code>FAILED</code> - Error occurred</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import GetConversationByIDStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetConversationByIDStatus = "INPROGRESS"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"INPROGRESS"`
- `"COMPLETED"`
- `"FAILED"`
