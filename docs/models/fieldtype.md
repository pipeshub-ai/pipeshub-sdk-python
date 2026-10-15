# FieldType

## Example Usage

```python
from pipeshub_sdk.models import FieldType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FieldType = "TEXT"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"TEXT"`
- `"PASSWORD"`
- `"URL"`
- `"SELECT"`
