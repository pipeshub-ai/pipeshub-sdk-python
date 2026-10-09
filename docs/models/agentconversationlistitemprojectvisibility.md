# AgentConversationListItemProjectVisibility

Only meaningful when `projectId` is set. `project` exposes the
conversation to every member of the linked project.


## Example Usage

```python
from pipeshub_sdk.models import AgentConversationListItemProjectVisibility

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentConversationListItemProjectVisibility = "private"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"private"`
- `"project"`
