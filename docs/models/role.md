# Role

Organization role stored on the user document (`admin` or `member`)

## Example Usage

```python
from pipeshub_sdk.models import Role

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Role = "admin"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"admin"`
- `"member"`
