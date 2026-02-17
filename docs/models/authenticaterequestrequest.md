# AuthenticateRequestRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `x_session_token`                                              | *str*                                                          | :heavy_check_mark:                                             | Session token received from `/initAuth` endpoint               |
| `body`                                                         | [models.AuthenticateRequest](../models/authenticaterequest.md) | :heavy_check_mark:                                             | Request payload                                                |