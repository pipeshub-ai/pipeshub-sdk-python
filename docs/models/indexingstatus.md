# IndexingStatus

Current indexing/processing status:
- NOT_STARTED: Awaiting indexing
- QUEUED: In indexing queue
- IN_PROGRESS: Currently being indexed
- COMPLETED: Successfully indexed and searchable
- FAILED: Indexing failed (check error details)
- PAUSED: Indexing paused by user
- FILE_TYPE_NOT_SUPPORTED: Unsupported file format
- AUTO_INDEX_OFF: Auto-indexing disabled for this record
- EMPTY: File has no extractable content
- ENABLE_MULTIMODAL_MODELS: Requires multimodal AI models



## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `NOT_STARTED`              | NOT_STARTED                |
| `PAUSED`                   | PAUSED                     |
| `IN_PROGRESS`              | IN_PROGRESS                |
| `COMPLETED`                | COMPLETED                  |
| `FAILED`                   | FAILED                     |
| `FILE_TYPE_NOT_SUPPORTED`  | FILE_TYPE_NOT_SUPPORTED    |
| `AUTO_INDEX_OFF`           | AUTO_INDEX_OFF             |
| `EMPTY`                    | EMPTY                      |
| `ENABLE_MULTIMODAL_MODELS` | ENABLE_MULTIMODAL_MODELS   |
| `QUEUED`                   | QUEUED                     |