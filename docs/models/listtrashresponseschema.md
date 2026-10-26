# ListTrashResponseSchema

Response returned by GET /knowledgeBase/{kbId}/trash.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `success`                                                                                  | *Literal[True]*                                                                            | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `items`                                                                                    | List[[models.TrashItemSchema](../models/trashitemschema.md)]                               | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `pagination`                                                                               | [models.ListTrashResponseSchemaPagination](../models/listtrashresponseschemapagination.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `retention`                                                                                | [OptionalNullable[models.Retention]](../models/retention.md)                               | :heavy_minus_sign:                                                                         | N/A                                                                                        |