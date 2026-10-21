# ConnectorRegistryScope

Scope determines visibility and access control for connectors:<br>
<ul>
<li><code>team</code> - Available to all users in the organization (admin-only creation)</li>
<li><code>personal</code> - Private to the creating user only</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import ConnectorRegistryScope
value: ConnectorRegistryScope = "team"
```


## Values

- `"team"`
- `"personal"`
