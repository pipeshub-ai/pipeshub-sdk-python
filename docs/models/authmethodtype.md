# AuthMethodType

Type of authentication method:
- `password`: Email/password authentication
- `otp`: One-time password via email (6-digit, expires in 10 minutes)
- `google`: Google OAuth 2.0
- `microsoft`: Microsoft OAuth 2.0
- `github`: accepted and stored, but no sign-in flow implements it:
  `/userAccount/initAuth` never lists it and `/userAccount/authenticate` answers `400`

`samlSso`, `oauth` (removed in 1.0) and `azureAd` (now `microsoft`) are refused when a
policy is saved. A stored policy that still names one is read without it (`azureAd`
reads as `microsoft`), with `password` added to the first step.


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
- `"github"`
