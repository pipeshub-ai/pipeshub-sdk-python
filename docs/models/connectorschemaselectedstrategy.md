# ConnectorSchemaSelectedStrategy

Strategy preselected in the form

## Example Usage

```python
from pipeshub_sdk.models import ConnectorSchemaSelectedStrategy

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConnectorSchemaSelectedStrategy = "MANUAL"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"MANUAL"`
- `"SCHEDULED"`
- `"WEBHOOK"`
