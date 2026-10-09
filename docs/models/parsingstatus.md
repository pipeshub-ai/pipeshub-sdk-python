# ParsingStatus

Parse-phase status (ahead of indexing/extraction):
- NOT_STARTED: Awaiting parsing
- QUEUED: In parsing queue
- IN_PROGRESS: Currently being parsed
- COMPLETED: Successfully parsed
- FAILED: Parsing failed
- FILE_TYPE_NOT_SUPPORTED: Unsupported file format
- AUTO_INDEX_OFF: Auto-indexing disabled for this record
- EMPTY: File has no extractable content


## Example Usage

```python
from pipeshub_sdk.models import ParsingStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ParsingStatus = "NOT_STARTED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"NOT_STARTED"`
- `"IN_PROGRESS"`
- `"FAILED"`
- `"COMPLETED"`
- `"FILE_TYPE_NOT_SUPPORTED"`
- `"AUTO_INDEX_OFF"`
- `"EMPTY"`
- `"QUEUED"`
