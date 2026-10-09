# ConversationMessageStreamRequestProtocol

AG-UI is the only supported wire protocol. When present must be
`"agui"`. Omitting the field is equivalent — the server always
uses the AG-UI vocabulary (see `ConversationMessageStreamSSEEvent`).
Kept in the schema for backward compatibility with callers that
already send it.


## Example Usage

```python
from pipeshub_sdk.models import ConversationMessageStreamRequestProtocol
value: ConversationMessageStreamRequestProtocol = "agui"
```


## Values

- `"agui"`
