# ConnectorScope

Scope determines visibility and access control for connectors:<br>
<ul>
<li><code>team</code> - Available to all users in the organization (admin-only creation)</li>
<li><code>personal</code> - Private to the creating user only</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import ConnectorScope

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConnectorScope = "team"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"team"`
- `"personal"`
