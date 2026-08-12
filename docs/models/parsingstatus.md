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



## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `NOT_STARTED`             | NOT_STARTED               |
| `IN_PROGRESS`             | IN_PROGRESS               |
| `FAILED`                  | FAILED                    |
| `COMPLETED`               | COMPLETED                 |
| `FILE_TYPE_NOT_SUPPORTED` | FILE_TYPE_NOT_SUPPORTED   |
| `AUTO_INDEX_OFF`          | AUTO_INDEX_OFF            |
| `EMPTY`                   | EMPTY                     |
| `QUEUED`                  | QUEUED                    |