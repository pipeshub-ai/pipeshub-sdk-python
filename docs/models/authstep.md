# AuthStep

A single step in multi-factor authentication flow


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `order`                                                                                              | *int*                                                                                                | :heavy_check_mark:                                                                                   | Order of the authentication step (1-3, must be unique across steps)                                  |
| `allowed_methods`                                                                                    | List[[models.AuthMethod](../models/authmethod.md)]                                                   | :heavy_check_mark:                                                                                   | List of allowed authentication methods for this step. User can choose any one method from this list. |