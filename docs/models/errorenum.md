# ErrorEnum

Error code. Common values:
- `invalid_request` - Missing or invalid parameter
- `invalid_client` - Client authentication failed
- `invalid_grant` - Invalid authorization code or refresh token
- `unauthorized_client` - Client not authorized for this grant type
- `unsupported_grant_type` - Grant type not supported
- `invalid_scope` - Requested scope is invalid or exceeds allowed
- `access_denied` - User denied authorization


## Example Usage

```python
from pipeshub_sdk.models import ErrorEnum

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ErrorEnum = "invalid_request"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_request"`
- `"invalid_client"`
- `"invalid_grant"`
- `"unauthorized_client"`
- `"unsupported_grant_type"`
- `"invalid_scope"`
- `"access_denied"`
- `"server_error"`
