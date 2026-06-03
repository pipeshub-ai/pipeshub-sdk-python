# UnarchiveSearchResponse

Search unarchived successfully


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique identifier of the unarchived search.                          | 65f1c0a4e2b9c4d8f3a1b2c3                                             |
| `status`                                                             | [models.UnarchiveSearchStatus](../models/unarchivesearchstatus.md)   | :heavy_check_mark:                                                   | Resulting status of the search after the operation.                  | unarchived                                                           |
| `unarchived_by`                                                      | *str*                                                                | :heavy_check_mark:                                                   | User ID of the user who unarchived the search.                       | 65f1c0a4e2b9c4d8f3a1b2c4                                             |
| `unarchived_at`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp when the search was unarchived.                            | 2026-05-10T12:34:56.789Z                                             |
| `meta`                                                               | [models.UnarchiveSearchMeta](../models/unarchivesearchmeta.md)       | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |