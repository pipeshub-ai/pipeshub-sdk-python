# InternalServerErrorErrorCode

Machine-readable error code.

- `HTTP_INTERNAL_SERVER_ERROR` — explicit
  `InternalServerError` raised by the handler.
- `INTERNAL_ERROR` — unhandled exception
  caught by the global error middleware.
- `MIDDLEWARE_ERROR` — the error middleware
  itself failed while serializing the
  response.


## Example Usage

```python
from pipeshub_sdk.models import InternalServerErrorErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InternalServerErrorErrorCode = "HTTP_INTERNAL_SERVER_ERROR"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"HTTP_INTERNAL_SERVER_ERROR"`
- `"INTERNAL_ERROR"`
- `"MIDDLEWARE_ERROR"`
