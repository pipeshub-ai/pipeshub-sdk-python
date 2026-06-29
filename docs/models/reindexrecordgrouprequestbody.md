# ReindexRecordGroupRequestBody

Optional body for record-group (folder/KB container) reindex.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `depth`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Depth of records under the record group to include.                     |
| `force`                                                                 | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Force reindex for all matched records in the group.                     |
| `status_filters`                                                        | List[[models.IndexingStatusFilter](../models/indexingstatusfilter.md)]  | :heavy_minus_sign:                                                      | When set, only records matching these indexing statuses are reindexed.<br/> |