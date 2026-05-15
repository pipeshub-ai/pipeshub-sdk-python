# KnowledgeHubNodesResponseFilters


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `applied`                                                    | [models.Applied](../models/applied.md)                       | :heavy_check_mark:                                           | Echo of applied filters; unused slots are JSON `null`.       |
| `available`                                                  | [Nullable[models.Available]](../models/available.md)         | :heavy_check_mark:                                           | Populated when `include=availableFilters`; otherwise `null`. |