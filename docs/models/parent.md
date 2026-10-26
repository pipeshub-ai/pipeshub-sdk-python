# Parent

The parent this node is listed under, with what a client needs to
open it and name it; `null` exactly when `parentId` is. It is the
node's placement parent: an ancestor the user cannot open is
replaced, never named.



## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `id`                                                  | *str*                                                 | :heavy_check_mark:                                    | Parent node ID.                                       |
| `node_type`                                           | [models.ParentNodeType](../models/parentnodetype.md)  | :heavy_check_mark:                                    | Parent node type; opened as `/nodes/{nodeType}/{id}`. |
| `name`                                                | *OptionalNullable[str]*                               | :heavy_minus_sign:                                    | Parent display name.                                  |