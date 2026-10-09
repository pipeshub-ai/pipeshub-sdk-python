# AllowedMethod

## Example Usage

```python
from pipeshub_sdk.models import AllowedMethod

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AllowedMethod = "samlSso"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"samlSso"`
- `"otp"`
- `"password"`
- `"google"`
- `"microsoft"`
- `"azureAd"`
- `"oauth"`
