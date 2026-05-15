# UpdateAuthMethodResponse

Response after updating organization authentication methods


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `message`                                                 | *str*                                                     | :heavy_check_mark:                                        | N/A                                                       | Auth method updated                                       |
| `auth_method`                                             | List[[models.AuthStep](../models/authstep.md)]            | :heavy_check_mark:                                        | Updated authentication steps (same shape as request body) |                                                           |