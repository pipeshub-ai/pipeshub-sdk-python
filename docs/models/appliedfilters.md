# AppliedFilters

Rich filter state selected by the user, used for display and persistence only.
This mirrors the active selection shown in the UI and is distinct from the
machine-readable `filters` field used for retrieval scoping.



## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `apps`                                                                 | List[[models.AppliedFilterNode](../models/appliedfilternode.md)]       | :heavy_minus_sign:                                                     | Applied app/connector filter nodes                                     |
| `kb`                                                                   | List[[models.AppliedFilterNode](../models/appliedfilternode.md)]       | :heavy_minus_sign:                                                     | Applied knowledge-base filter nodes                                    |
| `record_groups`                                                        | List[[models.AppliedFilterNode](../models/appliedfilternode.md)]       | :heavy_minus_sign:                                                     | Applied record-group filter nodes                                      |
| `records`                                                              | List[[models.AppliedFilterNode](../models/appliedfilternode.md)]       | :heavy_minus_sign:                                                     | Applied folder and record filter nodes (each with everything under it) |
| `records_exact`                                                        | List[[models.AppliedFilterNode](../models/appliedfilternode.md)]       | :heavy_minus_sign:                                                     | Applied record filter nodes selected alone                             |