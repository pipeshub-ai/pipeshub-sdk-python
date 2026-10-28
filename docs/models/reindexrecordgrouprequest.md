# ReindexRecordGroupRequest


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `record_group_id`                                                                            | *str*                                                                                        | :heavy_check_mark:                                                                           | Record group ID (from a connector sync; not a knowledge base or folder id)                   |
| `body`                                                                                       | [Optional[models.ReindexRecordGroupRequestBody]](../models/reindexrecordgrouprequestbody.md) | :heavy_minus_sign:                                                                           | Request payload                                                                              |