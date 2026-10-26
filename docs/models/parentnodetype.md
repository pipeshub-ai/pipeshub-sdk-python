# ParentNodeType

Parent node type; opened as `/nodes/{nodeType}/{id}`.

## Example Usage

```python
from pipeshub_sdk.models import ParentNodeType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ParentNodeType = "app"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"app"`
- `"recordGroup"`
- `"folder"`
- `"record"`
