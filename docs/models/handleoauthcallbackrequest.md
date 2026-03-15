# HandleOAuthCallbackRequest


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `code`                                  | *Optional[str]*                         | :heavy_minus_sign:                      | Authorization code from provider        |
| `state`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | State parameter (contains connector ID) |
| `error`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | Error code if authorization failed      |
| `base_url`                              | *Optional[str]*                         | :heavy_minus_sign:                      | Base URL for redirect                   |