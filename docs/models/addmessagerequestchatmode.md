# AddMessageRequestChatMode

Optional execution mode for non-stream consumers of this shared
request schema. `deep`, `quick`, `verification` and `auto` are
legacy values: still accepted, they run as `internal_search`.
The streaming routes accept only `agent`, `internal_search` and
`web_search`. `agent:<mode>` is refused.


## Example Usage

```python
from pipeshub_sdk.models import AddMessageRequestChatMode
value: AddMessageRequestChatMode = "agent"
```


## Values

- `"agent"`
- `"internal_search"`
- `"web_search"`
- `"deep"`
- `"quick"`
- `"verification"`
- `"auto"`
