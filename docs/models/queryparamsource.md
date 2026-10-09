# QueryParamSource

`owned` — owner list (`userId` filter only).
`shared` — explicit share grant list (`isShared` + `sharedWith`).
Defaults to `owned` when omitted.


## Example Usage

```python
from pipeshub_sdk.models import QueryParamSource
value: QueryParamSource = "owned"
```


## Values

- `"owned"`
- `"shared"`
