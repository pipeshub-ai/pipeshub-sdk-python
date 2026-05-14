# GetAvailableModelsByTypeBadRequestError

Invalid `modelType` path parameter.

The `modelType` value was not one of the supported enum categories.
This response is produced by the Zod validation middleware **before**
the handler runs. The `error.metadata.errors` array contains
per-field detail about exactly which constraint failed.



## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `error`                                                                                                          | [models.GetAvailableModelsByTypeErrorValidationError](../models/getavailablemodelsbytypeerrorvalidationerror.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |