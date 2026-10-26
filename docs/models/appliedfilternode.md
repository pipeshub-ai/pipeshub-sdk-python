# AppliedFilterNode

A single filter node selected by the user (used for display/persistence of active filters)


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | Unique identifier of the filter node                           |
| `name`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Display name of the filter node                                |
| `node_type`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Type of the node (e.g. app, recordGroup, folder, record)       |
| `connector`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Connector identifier associated with this node                 |
| `extension`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | File extension of a record node, for its icon                  |
| `mime_type`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | MIME type of a record node, for its icon                       |
| `mentioned`                                                    | *Optional[bool]*                                               | :heavy_minus_sign:                                             | True when the node was picked with an @ mention in the message |