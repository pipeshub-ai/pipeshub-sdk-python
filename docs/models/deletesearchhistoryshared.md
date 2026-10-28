# DeleteSearchHistoryShared

Restrict the deletion to rows with this `isShared` value. `'true'` / `'1'` and
`'false'` / `'0'`, case-insensitive; anything else is refused with `400`.


## Example Usage

```python
from pipeshub_sdk.models import DeleteSearchHistoryShared
value: DeleteSearchHistoryShared = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
