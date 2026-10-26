# DeleteRecordResponseSchema

Response returned by DELETE /knowledgeBase/record/{recordId}.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `success`                                                        | *Literal[True]*                                                  | :heavy_check_mark:                                               | N/A                                                              |
| `message`                                                        | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `record_id`                                                      | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `connector`                                                      | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `timestamp`                                                      | *OptionalNullable[int]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `soft_deleted`                                                   | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | True when the record went to the trash instead of being removed  |
| `batch_id`                                                       | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | The delete batch; restoring any record in it restores all of it  |
| `vector_cleanup_pending`                                         | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | The record is deleted, but removing its embeddings is still owed |
| `vector_cleanup_failed_record_ids`                               | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |
| `vector_cleanup_failed_virtual_record_ids`                       | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |