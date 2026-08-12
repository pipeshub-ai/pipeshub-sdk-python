# CreatePatResponse

Response body for `POST /personal-access-tokens` (`pat.controller.ts` `createToken`).


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `message`                                          | *str*                                              | :heavy_check_mark:                                 | N/A                                                | Personal access token created successfully         |
| `token`                                            | [models.PatWithSecret](../models/patwithsecret.md) | :heavy_check_mark:                                 | N/A                                                |                                                    |