# AccessRule

How this record's own permissions combine with its ancestors'.
OPEN: an accessible parent, or a direct grant, is enough.
STRICT: every ancestor up to the connector must be accessible too.
RESTRICTED: strict, and a grant on the record itself is required.
Absent on records written before the field existed; read as OPEN.


## Example Usage

```python
from pipeshub_sdk.models import AccessRule

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AccessRule = "OPEN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"OPEN"`
- `"STRICT"`
- `"RESTRICTED"`
