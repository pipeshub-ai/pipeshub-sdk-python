# AppliedFilterNode

A single filter node selected by the user (used for display/persistence of active
filters). The gateway refuses a node that lacks any of the four fields.



## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | Unique identifier of the filter node                           |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | Display name of the filter node                                |
| `node_type`                                                    | *str*                                                          | :heavy_check_mark:                                             | Type of the node (e.g. app, recordGroup, folder, record)       |
| `connector`                                                    | *str*                                                          | :heavy_check_mark:                                             | Connector identifier associated with this node                 |
| `extension`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | File extension of a record node, for its icon                  |
| `mime_type`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | MIME type of a record node, for its icon                       |
| `mentioned`                                                    | *Optional[bool]*                                               | :heavy_minus_sign:                                             | True when the node was picked with an @ mention in the message |