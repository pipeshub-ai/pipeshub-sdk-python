# GetSearchByIDShared

Return the search only if its `isShared` matches. `'true'` / `'1'` and `'false'` /
`'0'`, case-insensitive; anything else is refused with `400`.


## Example Usage

```python
from pipeshub_sdk.models import GetSearchByIDShared
value: GetSearchByIDShared = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
