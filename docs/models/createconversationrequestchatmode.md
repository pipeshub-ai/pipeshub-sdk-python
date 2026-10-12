# CreateConversationRequestChatMode

Optional execution mode for non-stream consumers of this shared
request schema.
`agent` uses the universal agent loop, while `internal_search`
and `web_search` use their corresponding assistant search paths.


## Example Usage

```python
from pipeshub_sdk.models import CreateConversationRequestChatMode
value: CreateConversationRequestChatMode = "agent"
```


## Values

- `"agent"`
- `"internal_search"`
- `"web_search"`
