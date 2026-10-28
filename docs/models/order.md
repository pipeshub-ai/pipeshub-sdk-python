# Order

Budgeted record reads only. `relevance` when `query` chose which blocks to show; the blocks are then not contiguous. `extract` when `extract=true` was asked and the reader model answered: `content` is the passages it copied out (told to copy word for word; see `extract.unverifiedLines`), not a page of the record. An extract is one response, so `complete` is true and `nextStartBlock` null; whether the reader saw the whole record is `extract.sourceComplete`.

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
- `"extract"`
