# QueryParamSource

`owned` — owner list (`userId` filter only).
`shared` — explicit share grant list (`isShared` + `sharedWith`). Includes agent
conversations shared with the caller; those rows carry `agentKey`.
Defaults to `owned` when omitted.


## Example Usage

```python
from pipeshub_sdk.models import QueryParamSource
value: QueryParamSource = "owned"
```


## Values

- `"owned"`
- `"shared"`
