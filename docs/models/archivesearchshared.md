# ArchiveSearchShared

Additional `isShared` filter. `'true'` / `'1'` and `'false'` / `'0'`,
case-insensitive; anything else is refused with `400`. The search is only archived
if it matches, otherwise `404`.


## Example Usage

```python
from pipeshub_sdk.models import ArchiveSearchShared
value: ArchiveSearchShared = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
