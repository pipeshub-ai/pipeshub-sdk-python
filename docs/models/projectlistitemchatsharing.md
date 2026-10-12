# ProjectListItemChatSharing

Owner-controlled default for new conversations created in this
project. `private` keeps new chats visible to their own owner
only; `members` exposes them to every project member
(`projectVisibility: project`). A conversation's own
`projectVisibility` can override this default per-chat.


## Example Usage

```python
from pipeshub_sdk.models import ProjectListItemChatSharing

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProjectListItemChatSharing = "private"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"private"`
- `"members"`
