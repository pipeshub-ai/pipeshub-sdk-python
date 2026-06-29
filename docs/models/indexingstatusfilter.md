# IndexingStatusFilter

Indexing status used to filter which records are included in a scoped
reindex (record or record-group). Omit `statusFilters` to reindex all
descendants regardless of status.



## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `NOT_STARTED`             | NOT_STARTED               |
| `QUEUED`                  | QUEUED                    |
| `IN_PROGRESS`             | IN_PROGRESS               |
| `COMPLETED`               | COMPLETED                 |
| `FAILED`                  | FAILED                    |
| `FILE_TYPE_NOT_SUPPORTED` | FILE_TYPE_NOT_SUPPORTED   |
| `AUTO_INDEX_OFF`          | AUTO_INDEX_OFF            |
| `EMPTY`                   | EMPTY                     |