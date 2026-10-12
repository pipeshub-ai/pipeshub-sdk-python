# ParentType

Type of the parent node whose children to retrieve.

Must be one of: `app`, `recordGroup`, `folder`, `record`.
Any other value returns a 400 error.


## Example Usage

```python
from pipeshub_sdk.models import ParentType
value: ParentType = "app"
```


## Values

- `"app"`
- `"recordGroup"`
- `"folder"`
- `"record"`
