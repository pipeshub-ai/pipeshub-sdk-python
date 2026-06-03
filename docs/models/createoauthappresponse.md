# CreateOAuthAppResponse

Response body for `POST /oauth-clients` (`oauth.app.controller.ts` `createApp`).
The new app (including one-time `clientSecret`) is nested under `app`.



## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `message`                                                    | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          | OAuth app created successfully                               |
| `app`                                                        | [models.OAuthAppWithSecret](../models/oauthappwithsecret.md) | :heavy_check_mark:                                           | N/A                                                          |                                                              |