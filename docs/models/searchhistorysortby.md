# SearchHistorySortBy

Field used to sort results. Any value other than `createdAt`,
`lastActivityAt`, or `title` is treated as `lastActivityAt`.


## Example Usage

```python
from pipeshub_sdk.models import SearchHistorySortBy
value: SearchHistorySortBy = "createdAt"
```


## Values

- `"createdAt"`
- `"lastActivityAt"`
- `"title"`
