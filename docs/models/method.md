# Method

Authentication method to use. It must be one the session's current step allows;
any other value, known or not, is answered `400`.


## Example Usage

```python
from pipeshub_sdk.models import Method
value: Method = "otp"
```


## Values

- `"otp"`
- `"password"`
- `"google"`
- `"microsoft"`
