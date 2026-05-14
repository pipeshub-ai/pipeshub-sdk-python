# AppliedFilterNode

A single filter node selected by the user (used for display/persistence of active filters)


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `id`                                           | *Optional[str]*                                | :heavy_minus_sign:                             | Unique identifier of the filter node           |
| `name`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | Display name of the filter node                |
| `node_type`                                    | *Optional[str]*                                | :heavy_minus_sign:                             | Type of the node (e.g. app, kb)                |
| `connector`                                    | *Optional[str]*                                | :heavy_minus_sign:                             | Connector identifier associated with this node |