# Auth

Authentication configuration


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `oauth_instance_name`                                  | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `auth_type`                                            | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `oauth_config_id`                                      | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `connector_type`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `authorize_url`                                        | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `token_url`                                            | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `scopes`                                               | List[*str*]                                            | :heavy_minus_sign:                                     | N/A                                                    |
| `redirect_uri`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `connector_scope`                                      | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `values`                                               | [Optional[models.AuthValues]](../models/authvalues.md) | :heavy_minus_sign:                                     | Auth field values                                      |