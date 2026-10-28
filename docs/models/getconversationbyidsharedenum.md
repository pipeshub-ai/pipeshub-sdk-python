# GetConversationByIDSharedEnum

Filters on the conversation's `isShared`; a conversation that
does not match is answered `404`. Read case-insensitively;
any other value is refused with `400`.


## Example Usage

```python
from pipeshub_sdk.models import GetConversationByIDSharedEnum
value: GetConversationByIDSharedEnum = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
