# RestoreRecordResponseSchema

Response returned by POST /knowledgeBase/record/{recordId}/restore.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `success`                                                              | *Literal[True]*                                                        | :heavy_check_mark:                                                     | N/A                                                                    |
| `message`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `batch_id`                                                             | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The delete batch that was restored                                     |
| `restored_records`                                                     | List[[models.RestoredRecordSchema](../models/restoredrecordschema.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `reindex_pending`                                                      | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Some restored files could not be queued for indexing                   |
| `reindex_pending_record_ids`                                           | List[*str*]                                                            | :heavy_minus_sign:                                                     | Files to reindex by hand to make them searchable again                 |
| `reindex_pending_reason`                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `rename_pending_record_ids`                                            | List[*str*]                                                            | :heavy_minus_sign:                                                     | Items restored under a name another item next to them has; rename them |
| `rename_pending_reason`                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |