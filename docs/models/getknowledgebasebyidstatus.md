# GetKnowledgeBaseByIDStatus

`DELETING` while the knowledge base is being deleted: reads work, every write is refused with 409
(`error.code` `HTTP_KB_BEING_DELETED`), and deleting it again finishes the job. Otherwise its
processing state (`IDLE`, `QUEUED`, `SYNCING`, `FULL_SYNCING`), or null before it is first processed.


## Example Usage

```python
from pipeshub_sdk.models import GetKnowledgeBaseByIDStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GetKnowledgeBaseByIDStatus = "IDLE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"IDLE"`
- `"QUEUED"`
- `"SYNCING"`
- `"FULL_SYNCING"`
- `"DELETING"`
