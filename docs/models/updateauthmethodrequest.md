# UpdateAuthMethodRequest

Request payload


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `auth_method`                                                                          | List[[models.AuthStep](../models/authstep.md)]                                         | :heavy_check_mark:                                                                     | Authentication steps configuration                                                     | [<br/>{<br/>"order": 1,<br/>"allowedMethods": [<br/>{<br/>"type": "password"<br/>},<br/>{<br/>"type": "google"<br/>}<br/>]<br/>}<br/>] |