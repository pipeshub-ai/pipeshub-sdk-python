# MessageMessageType1

Type of message:
- `user_query` - User's question or input
- `bot_response` - AI-generated response
- `error` - Error message from the system
- `feedback` - User feedback on a response
- `system` - System notification or status
- `tool_call` - Tool invocation turn; details are on `tools`


## Example Usage

```python
from pipeshub_sdk.models import MessageMessageType1

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MessageMessageType1 = "user_query"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user_query"`
- `"bot_response"`
- `"error"`
- `"feedback"`
- `"system"`
- `"tool_call"`
