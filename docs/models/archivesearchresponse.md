# ArchiveSearchResponse

Search archived successfully


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique identifier of the archived search.                            | 65f1c0a4e2b9c4d8f3a1b2c3                                             |
| `status`                                                             | [models.ArchiveSearchStatus](../models/archivesearchstatus.md)       | :heavy_check_mark:                                                   | Resulting status of the search after the operation.                  | archived                                                             |
| `archived_by`                                                        | *str*                                                                | :heavy_check_mark:                                                   | User ID of the user who archived the search.                         | 65f1c0a4e2b9c4d8f3a1b2c4                                             |
| `archived_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp when the search was archived.                              | 2026-05-10 12:34:56.789 +0000 UTC                                    |
| `meta`                                                               | [models.ArchiveSearchMeta](../models/archivesearchmeta.md)           | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |