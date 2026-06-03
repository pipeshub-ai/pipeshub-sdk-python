# ApplicationJSONErrorResponse

Standard JSON error envelope from `ErrorMiddleware` for `BaseError` subclasses (`error.middleware.ts`).
Returned for most API 4xx errors (unauthorized, forbidden, not found, validation failures, etc.).



## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `error`                                                                                    | [models.ApplicationJSONErrorResponseError](../models/applicationjsonerrorresponseerror.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |