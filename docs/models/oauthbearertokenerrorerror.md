# OAuthBearerTokenErrorError

- `invalid_request` - no `Authorization: Bearer` header was sent
- `invalid_token` - the token is malformed, expired, revoked, or its user no longer exists
- `insufficient_scope` - the token is valid but lacks a required scope
- `server_error` - the scope check itself failed


## Example Usage

```python
from pipeshub_sdk.models import OAuthBearerTokenErrorError

# Open enum: unrecognized values are captured as UnrecognizedStr
value: OAuthBearerTokenErrorError = "invalid_request"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_request"`
- `"invalid_token"`
- `"insufficient_scope"`
- `"server_error"`
