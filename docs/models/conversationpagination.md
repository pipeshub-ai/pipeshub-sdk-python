# ConversationPagination

Pagination over the conversation's messages. Messages are paginated backwards
(newest first), so `messageRange.start`/`messageRange.end` refer to 1-based
positions within the full message list.



## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `page`                                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `limit`                                                    | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `total_count`                                              | *Optional[int]*                                            | :heavy_minus_sign:                                         | Total number of messages in the conversation               |
| `total_pages`                                              | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `has_next_page`                                            | *Optional[bool]*                                           | :heavy_minus_sign:                                         | True if there are older messages available                 |
| `has_prev_page`                                            | *Optional[bool]*                                           | :heavy_minus_sign:                                         | True if there are newer messages available                 |
| `message_range`                                            | [Optional[models.MessageRange]](../models/messagerange.md) | :heavy_minus_sign:                                         | N/A                                                        |