# ProjectListItemRole

Caller's effective role on this project (owner, explicit
member role, or `viewer` via `visibility: org`).


## Example Usage

```python
from pipeshub_sdk.models import ProjectListItemRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProjectListItemRole = "owner"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"owner"`
- `"editor"`
- `"viewer"`
