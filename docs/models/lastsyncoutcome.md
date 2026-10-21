# LastSyncOutcome

How the last sync run ended

## Example Usage

```python
from pipeshub_sdk.models import LastSyncOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: LastSyncOutcome = "succeeded"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"succeeded"`
- `"failed"`
- `"stopped"`
- `"skipped"`
