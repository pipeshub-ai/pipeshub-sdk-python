# GetSearchByIDInternalServerError

Server error. Possible causes:

- Explicit `InternalServerError`
  or any other 500 `BaseError` thrown by the handler.
- Non-`BaseError` exception caught by the
  global error middleware.
- Response serializer fallback.



## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `error`                                                                                            | [models.GetSearchByIDInternalServerErrorError](../models/getsearchbyidinternalservererrorerror.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |