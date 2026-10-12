# Kind

Whether this account is a person who signs in (`human`) or a
machine identity that automation authenticates as (`service`).
Absent on records written before service accounts existed, which
are all human.


## Example Usage

```python
from pipeshub_sdk.models import Kind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Kind = "human"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"human"`
- `"service"`
