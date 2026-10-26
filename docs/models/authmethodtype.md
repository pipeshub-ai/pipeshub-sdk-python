# AuthMethodType

Type of authentication method:
- `password`: Email/password authentication
- `otp`: One-time password via email (6-digit, expires in 10 minutes)
- `google`: Google OAuth 2.0
- `microsoft`: Microsoft OAuth 2.0


## Example Usage

```python
from pipeshub_sdk.models import AuthMethodType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuthMethodType = "otp"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"otp"`
- `"password"`
- `"google"`
- `"microsoft"`
