# ConversationStreamRequestChatMode

Optional execution mode for non-stream consumers of this shared
request schema.
`agent` uses the universal agent loop, while `internal_search`
and `web_search` use their corresponding assistant search paths.


## Example Usage

```python
from pipeshub_sdk.models import ConversationStreamRequestChatMode
value: ConversationStreamRequestChatMode = "agent"
```


## Values

- `"agent"`
- `"internal_search"`
- `"web_search"`
