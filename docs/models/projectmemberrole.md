# ProjectMemberRole

`viewer` can read the project and its `project`-visible
conversations. `editor` can additionally update project
metadata, instructions, scope, tools, and files. Only the owner
can manage members or change `visibility`/`chatSharing`.


## Example Usage

```python
from pipeshub_sdk.models import ProjectMemberRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProjectMemberRole = "viewer"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"viewer"`
- `"editor"`
