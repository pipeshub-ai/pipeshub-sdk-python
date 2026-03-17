# MessageTypeEnum

Type of message:
<ul>
<li><code>user_query</code> - User's question or input</li>
<li><code>bot_response</code> - AI-generated response</li>
<li><code>error</code> - Error message from the system</li>
<li><code>feedback</code> - User feedback on a response</li>
<li><code>system</code> - System notification or status</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import MessageTypeEnum

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MessageTypeEnum = "user_query"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user_query"`
- `"bot_response"`
- `"error"`
- `"feedback"`
- `"system"`
