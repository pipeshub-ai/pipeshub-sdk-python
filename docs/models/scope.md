# Scope

`mine` — owned only. `shared` — projects the caller is a member
of. `all` — owned, member, and `visibility: org` projects.
Defaults to `mine`.


## Example Usage

```python
from pipeshub_sdk.models import Scope
value: Scope = "mine"
```


## Values

- `"mine"`
- `"shared"`
- `"all"`
