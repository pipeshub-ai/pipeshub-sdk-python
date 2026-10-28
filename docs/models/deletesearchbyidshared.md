# DeleteSearchByIDShared

Additional `isShared` filter. `'true'` / `'1'` and `'false'` / `'0'`,
case-insensitive; anything else is refused with `400`. The row is only deleted if
it matches.


## Example Usage

```python
from pipeshub_sdk.models import DeleteSearchByIDShared
value: DeleteSearchByIDShared = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
