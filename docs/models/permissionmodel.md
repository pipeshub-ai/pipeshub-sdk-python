# PermissionModel

How records of this connector get their per-user visibility:
`RECORD_LEVEL` (per-record permissions from the source) or
`APP_LEVEL` (everyone who can reach the connector sees every record).


## Example Usage

```python
from pipeshub_sdk.models import PermissionModel

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PermissionModel = "RECORD_LEVEL"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RECORD_LEVEL"`
- `"APP_LEVEL"`
