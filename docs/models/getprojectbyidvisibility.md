# GetProjectByIDVisibility

`org` makes the project (and, per `chatSharing`, its
`project`-visible conversations) readable by every member of the
organization, without adding them to `members[]`. Also grants
the organization's synthetic all-members team `READER` access
on the linked hidden Collection.


## Example Usage

```python
from pipeshub_sdk.models import GetProjectByIDVisibility

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetProjectByIDVisibility = "private"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"private"`
- `"org"`
