# ApplicationJSONErrorResponseError


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Machine-readable code (e.g. `HTTP_UNAUTHORIZED`, `HTTP_FORBIDDEN`). |
| `message`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metadata`                                                          | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | Optional; may appear in non-production for some errors.             |