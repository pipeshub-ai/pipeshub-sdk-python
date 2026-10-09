# GrantType

OAuth grant type:
- `authorization_code`: Exchange auth code for tokens
- `client_credentials`: Machine-to-machine auth
- `refresh_token`: Get new access token using refresh token


## Example Usage

```python
from pipeshub_sdk.models import GrantType
value: GrantType = "authorization_code"
```


## Values

- `"authorization_code"`
- `"client_credentials"`
- `"refresh_token"`
