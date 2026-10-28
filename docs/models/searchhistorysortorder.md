# SearchHistorySortOrder

Sort direction applied to `sortBy`. Only the exact, case-sensitive value `asc` sorts
ascending; any other value (`ASC`, `sideways`, ...) is accepted and sorts descending.
The raw value is echoed in `filters.applied.values.sortOrder`.


## Example Usage

```python
from pipeshub_sdk.models import SearchHistorySortOrder
value: SearchHistorySortOrder = "asc"
```


## Values

- `"asc"`
- `"desc"`
