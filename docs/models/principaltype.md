# PrincipalType

Whether `principalId` names a user or a team. Both grant the same `role`, mirroring Collection sharing.

## Example Usage

```python
from pipeshub_sdk.models import PrincipalType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PrincipalType = "user"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user"`
- `"team"`
