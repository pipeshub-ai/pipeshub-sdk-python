# Order

Budgeted record reads only. `relevance` when `query` chose which blocks to show; the blocks are then not contiguous.

## Example Usage

```python
from pipeshub_sdk.models import Order

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Order = "in_order"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"in_order"`
- `"relevance"`
