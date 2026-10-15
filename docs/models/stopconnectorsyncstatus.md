# StopConnectorSyncStatus

The status the connector is actually left in.

## Example Usage

```python
from pipeshub_sdk.models import StopConnectorSyncStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: StopConnectorSyncStatus = "IDLE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"IDLE"`
- `"SYNCING"`
- `"FULL_SYNCING"`
- `"QUEUED"`
- `"DELETING"`
