# ListOAuthAppsStatus

Filter by status. `revoked` always yields an empty page, because an app only becomes revoked by being deleted and deleted apps are never listed.

## Example Usage

```python
from pipeshub_sdk.models import ListOAuthAppsStatus
value: ListOAuthAppsStatus = "active"
```


## Values

- `"active"`
- `"suspended"`
- `"revoked"`
