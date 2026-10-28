# KnowledgeBaseMoveRecordRequestBody

Request body for PUT /knowledgeBase/{kbId}/record/{recordId}/move (moveRecord). Fields other than `newParentId` are dropped by the validator, not refused.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `new_parent_id`                                                         | *Nullable[str]*                                                         | :heavy_check_mark:                                                      | Target folder ID, or null to move the record to the knowledge base root |