# AgentConversationDetailPagination

Message pagination returned inside the `conversation` object. The
handler paginates backwards from the end of the stored message array,
then sorts the selected page in memory before serialization.



## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `page`                                                   | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `limit`                                                  | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `total_count`                                            | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `total_pages`                                            | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `has_next_page`                                          | *bool*                                                   | :heavy_check_mark:                                       | True when older messages exist outside the returned page |
| `has_prev_page`                                          | *bool*                                                   | :heavy_check_mark:                                       | True when newer messages exist outside the returned page |
| `message_range`                                          | [models.MessageRange](../models/messagerange.md)         | :heavy_check_mark:                                       | N/A                                                      |