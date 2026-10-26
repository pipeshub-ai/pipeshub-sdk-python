# OptionSourceType

`dynamic` options come from GET /connectors/{connectorId}/filters/{filterKey}/options

## Example Usage

```python
from pipeshub_sdk.models import OptionSourceType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: OptionSourceType = "manual"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"manual"`
- `"static"`
- `"dynamic"`
