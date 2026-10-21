# HandleOAuthCallbackRequest


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `code`                                  | *str*                                   | :heavy_check_mark:                      | Authorization code from provider        |
| `state`                                 | *str*                                   | :heavy_check_mark:                      | State parameter (contains connector ID) |
| `error`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | Error code if authorization failed      |
| `base_url`                              | *Optional[str]*                         | :heavy_minus_sign:                      | Base URL for redirect                   |