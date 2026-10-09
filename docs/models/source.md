# Source

Origin of the feedback. Always present in responses (server applies the default `user`).

## Example Usage

```python
from pipeshub_sdk.models import Source

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Source = "user"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user"`
- `"system"`
- `"admin"`
- `"auto"`
