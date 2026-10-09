# ConversationProjectVisibility

Only meaningful when `projectId` is set. `private` (default)
keeps the conversation visible to its owner only; `project`
exposes it to every member of the linked project. See
`PATCH /conversations/{conversationId}/project-visibility`.


## Example Usage

```python
from pipeshub_sdk.models import ConversationProjectVisibility

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConversationProjectVisibility = "private"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"private"`
- `"project"`
