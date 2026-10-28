# GetConversationByIDQueryParamMessageType

Checked against the listed values (`400` otherwise) but not
applied: every message type is returned.


## Example Usage

```python
from pipeshub_sdk.models import GetConversationByIDQueryParamMessageType
value: GetConversationByIDQueryParamMessageType = "user_query"
```


## Values

- `"user_query"`
- `"bot_response"`
- `"error"`
- `"feedback"`
- `"system"`
- `"tool_call"`
