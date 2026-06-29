# GetAllKnowledgeBaseResponseSchemaApplied

Active filters. Empty `{}` when defaults. Keys use snake_case for sort
fields (backend convention in kb_service.py).



## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `search`                                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `permissions`                                                      | List[[models.AppliedPermission](../models/appliedpermission.md)]   | :heavy_minus_sign:                                                 | N/A                                                                |
| `sort_by`                                                          | [Optional[models.SortBy]](../models/sortby.md)                     | :heavy_minus_sign:                                                 | N/A                                                                |
| `sort_order`                                                       | [Optional[models.AppliedSortOrder]](../models/appliedsortorder.md) | :heavy_minus_sign:                                                 | N/A                                                                |