# ReindexRecordRequestBody

Optional body for single-record reindex. Only `depth` and `statusFilters` are read;
any other field is dropped by the validator before the handler runs (there is no
`force` option: the handler always sends `force: false`). No body, an empty object
or an empty `statusFilters` list mean depth `0` and no status filter.



## Fields

| Field                                                                                                                                                | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `depth`                                                                                                                                              | *Optional[int]*                                                                                                                                      | :heavy_minus_sign:                                                                                                                                   | Child traversal depth (`0` = record only; higher values include<br/>descendants; `-1` = all of them; `100` is used by clients for folder-like reindex).<br/> |
| `status_filters`                                                                                                                                     | List[*str*]                                                                                                                                          | :heavy_minus_sign:                                                                                                                                   | When set, only records whose indexing status matches one of these<br/>values are reindexed (applies to the record and its descendants per `depth`).<br/> |