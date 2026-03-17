# ConnectorAuthType

Authentication method required by the connector:<br>
<ul>
<li><code>OAUTH</code> - User OAuth consent flow</li>
<li><code>OAUTH_ADMIN_CONSENT</code> - Admin OAuth with org-wide consent</li>
<li><code>API_TOKEN</code> - API key or token authentication</li>
<li><code>USERNAME_PASSWORD</code> - Username/password credentials</li>
<li><code>NONE</code> - No authentication required</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import ConnectorAuthType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConnectorAuthType = "OAUTH"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"OAUTH"`
- `"OAUTH_ADMIN_CONSENT"`
- `"API_TOKEN"`
- `"USERNAME_PASSWORD"`
- `"NONE"`
