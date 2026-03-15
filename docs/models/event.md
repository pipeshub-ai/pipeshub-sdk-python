# Event

## Example Usage

```python
from pipeshub_sdk.models import Event

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Event = "connected"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"connected"`
- `"status"`
- `"answer_chunk"`
- `"citation"`
- `"complete"`
- `"error"`
