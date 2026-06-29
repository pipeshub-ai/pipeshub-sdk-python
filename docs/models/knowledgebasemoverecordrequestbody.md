# KnowledgeBaseMoveRecordRequestBody

Request body for PUT /knowledgeBase/{kbId}/record/{recordId}/move (moveRecord).


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `new_parent_id`                                                         | *Nullable[str]*                                                         | :heavy_check_mark:                                                      | Target folder ID, or null to move the record to the knowledge base root |