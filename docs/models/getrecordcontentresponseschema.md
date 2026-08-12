# GetRecordContentResponseSchema

Response returned by GET /connectors/record/{recordId}/content.

`content` is the record's full parsed content flattened into a single
plain-text string: a metadata header (title, source, key fields, and a
short summary), then the record's block/table text in reading order, and
finally a foreign-key related-tables footer for `SQL_TABLE` records.

For `TICKET` records (e.g. Jira) the metadata header is refreshed with
live ticket fields (status, assignee, comments) at request time rather
than the last-indexed snapshot. `content` may be empty for records with
no extractable text (e.g. image-only or not-yet-parsed records).



## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `content`                                                       | *str*                                                           | :heavy_check_mark:                                              | The record's full parsed content as a single plain-text string. |