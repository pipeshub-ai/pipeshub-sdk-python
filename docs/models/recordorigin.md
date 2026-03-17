# RecordOrigin

Source of the record:
- UPLOAD: Manually uploaded via API/UI
- CONNECTOR: Synced from external connector


## Example Usage

```python
from pipeshub_sdk.models import RecordOrigin

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RecordOrigin = "UPLOAD"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"UPLOAD"`
- `"CONNECTOR"`
