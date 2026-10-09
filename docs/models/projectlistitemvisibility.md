# ProjectListItemVisibility

`org` makes the project (and, per `chatSharing`, its
`project`-visible conversations) readable by every member of the
organization, without adding them to `members[]`. Also grants
the organization's synthetic all-members team `READER` access
on the linked hidden Collection.


## Example Usage

```python
from pipeshub_sdk.models import ProjectListItemVisibility

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProjectListItemVisibility = "private"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"private"`
- `"org"`
