# IsVersioned

Enable version tracking. `true`/`1` and `false`/`0`/empty are read as
booleans; any other text is answered `500` (the validator throws a plain
error).


## Example Usage

```python
from pipeshub_sdk.models import IsVersioned
value: IsVersioned = "true"
```


## Values

- `"true"`
- `"false"`
- `"1"`
- `"0"`
- `""`
