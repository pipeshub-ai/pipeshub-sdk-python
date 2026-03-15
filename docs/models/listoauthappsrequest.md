# ListOAuthAppsRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `page`                                                                   | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Page number                                                              |
| `limit`                                                                  | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Items per page                                                           |
| `status`                                                                 | [Optional[models.ListOAuthAppsStatus]](../models/listoauthappsstatus.md) | :heavy_minus_sign:                                                       | Filter by status                                                         |
| `search`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Search by app name                                                       |