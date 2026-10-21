# GrantType

OAuth grant type:
- `authorization_code`: Exchange auth code for tokens
- `client_credentials`: Machine-to-machine auth
- `refresh_token`: Get new access token using refresh token
- `urn:ietf:params:oauth:grant-type:token-exchange`: Service-account
  delegation (RFC 8693). Exchanges a service token for a
  short-lived token that acts as one named person. Enterprise
  edition; kept in this enum because the request shape is the same
  wherever the grant is offered.


## Example Usage

```python
from pipeshub_sdk.models import GrantType
value: GrantType = "authorization_code"
```


## Values

- `"authorization_code"`
- `"client_credentials"`
- `"refresh_token"`
- `"urn:ietf:params:oauth:grant-type:token-exchange"`
