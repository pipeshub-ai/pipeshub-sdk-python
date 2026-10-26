# ErrorEnum

Error code. Common values:
- `invalid_request` - Missing or invalid parameter
- `invalid_client` - Client authentication failed
- `invalid_grant` - Invalid authorization code or refresh token
- `unauthorized_client` - Client not authorized for this grant type
- `unsupported_grant_type` - Grant type not supported
- `invalid_scope` - Requested scope is invalid or exceeds allowed
- `access_denied` - User denied authorization
- `invalid_target` - The requested subject cannot be acted as
  (RFC 8693). Returned by the token-exchange grant for every
  refusal about the person asked for, with one wording, so a
  service token cannot tell "no such person" from "not on your
  list". The real cause is in the delegation log.


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
- `"invalid_target"`
- `"unauthorized_client"`
- `"unsupported_grant_type"`
- `"invalid_scope"`
- `"access_denied"`
- `"server_error"`
