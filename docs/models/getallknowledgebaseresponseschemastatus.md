# GetAllKnowledgeBaseResponseSchemaStatus

The knowledge base's processing state. `DELETING` while it is being deleted (writes are
refused with 409). `IDLE`, `QUEUED`, `SYNCING` or `FULL_SYNCING` otherwise, or null on a
knowledge base that has not been processed yet.


## Example Usage

```python
from pipeshub_sdk.models import GetAllKnowledgeBaseResponseSchemaStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetAllKnowledgeBaseResponseSchemaStatus = "IDLE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"IDLE"`
- `"QUEUED"`
- `"SYNCING"`
- `"FULL_SYNCING"`
- `"DELETING"`
