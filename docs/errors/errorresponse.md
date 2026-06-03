# ErrorResponse

Standard error envelope returned by all errors routed through `ErrorMiddleware`.
Applies to all `BaseError` subclasses including `HttpError`, `ValidationError`, and others.
The `code` field is a machine-readable string identifying the error type (e.g.
`HTTP_UNAUTHORIZED`, `HTTP_NOT_FOUND`, `VALIDATION_ERROR`, `INTERNAL_ERROR`).



## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `error`                                                      | [models.ErrorResponseError](../models/errorresponseerror.md) | :heavy_check_mark:                                           | N/A                                                          |