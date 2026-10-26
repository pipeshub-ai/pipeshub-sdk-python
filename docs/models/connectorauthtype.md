# ConnectorAuthType

How a connector instance signs in to its source. Each connector type supports a subset; see `supportedAuthTypes` in the registry.

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
- `"BEARER_TOKEN"`
- `"BASIC_AUTH"`
- `"ACCESS_KEY"`
- `"IAM_ROLE"`
- `"ACCOUNT_KEY"`
- `"CONNECTION_STRING"`
- `"ENTRA_ID"`
- `"CUSTOM"`
- `"NONE"`
