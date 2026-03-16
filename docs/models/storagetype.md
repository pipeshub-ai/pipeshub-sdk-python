# StorageType

Currently configured storage type

## Example Usage

```python
from pipeshub_sdk.models import StorageType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: StorageType = "local"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"local"`
- `"s3"`
- `"azureBlob"`
