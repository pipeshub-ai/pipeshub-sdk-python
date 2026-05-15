# ArchiveConversationResponse

Conversation archived successfully


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Conversation identifier                                                              |
| `status`                                                                             | [Optional[models.ArchiveConversationStatus]](../models/archiveconversationstatus.md) | :heavy_minus_sign:                                                                   | New archive status of the conversation                                               |
| `archived_by`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | User who archived the conversation                                                   |
| `archived_at`                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                 | :heavy_minus_sign:                                                                   | Timestamp when the conversation was archived                                         |
| `meta`                                                                               | [Optional[models.ArchiveConversationMeta]](../models/archiveconversationmeta.md)     | :heavy_minus_sign:                                                                   | N/A                                                                                  |