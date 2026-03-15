# UserGroupType

Group type:
- admin: System admin group (cannot be modified)
- standard: Default user group
- everyone: All users group (cannot be modified)
- custom: User-created custom group


## Example Usage

```python
from pipeshub_sdk.models import UserGroupType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UserGroupType = "admin"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"admin"`
- `"standard"`
- `"everyone"`
- `"custom"`
