# GetKnowledgeHubChildNodesUnprocessableEntityError

Either of:
- A typed query parameter could not be read: `page` or `limit` is not an
  integer or is out of range (`page` below 1, `limit` outside 1-200), or
  `onlyContainers` or `flattened` is not a boolean. `error.message` is the
  connector service's own validation text.
- A listing that spans a whole connector (a flattened listing, a search or a filter) was too large for the
  database to hold in memory, so it was refused instead of cut short. No page is returned. Open a folder
  (`GET /knowledgeBase/knowledge-hub/nodes/{parentType}/{parentId}`) to see its records, or add a search (`q`),
  which keeps only matching records in memory. Choosing a connector, or a filter that keeps most records (such as
  `nodeTypes`), does not help. Sorting by name with no filters is served from stored visibility where the
  connector allows it and is not affected.



## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `error`                                                                                                                    | [models.GetKnowledgeHubChildNodesUnprocessableEntityError](../models/getknowledgehubchildnodesunprocessableentityerror.md) | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |