# AuthMethodType

Type of authentication method:
- `password`: Email/password authentication
- `otp`: One-time password via email (6-digit, expires in 10 minutes)
- `google`: Google OAuth 2.0
- `microsoft`: Microsoft OAuth 2.0
- `samlSso`: SAML 2.0 Single Sign-On
- `oauth`: Generic OAuth 2.0 provider


## Example Usage

```python
from pipeshub_sdk.models import AuthMethodType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuthMethodType = "samlSso"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"samlSso"`
- `"otp"`
- `"password"`
- `"google"`
- `"microsoft"`
- `"oauth"`
