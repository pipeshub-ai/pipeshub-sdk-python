# SearchHistoryShared

Filter results by their shared status. Accepted values are
`'true'` / `'1'` (return only shared searches) and
`'false'` / `'0'` (exclude shared searches). Matching is
case-insensitive and surrounding whitespace is trimmed.


## Example Usage

```python
from pipeshub_sdk.models import SearchHistoryShared
value: SearchHistoryShared = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
