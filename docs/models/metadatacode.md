# MetadataCode

Machine-readable error code mapped from the Zod issue code.

## Example Usage

```python
from pipeshub_sdk.models import MetadataCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MetadataCode = "INVALID_TYPE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"INVALID_TYPE"`
- `"INVALID_LITERAL"`
- `"INVALID_ENUM"`
- `"INVALID_UNION"`
- `"INVALID_DISCRIMINATOR"`
- `"INVALID_ARGUMENTS"`
- `"TOO_SMALL"`
- `"TOO_BIG"`
