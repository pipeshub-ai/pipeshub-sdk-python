# UpdateSlackBotConfigRequestBody

Request payload


## Fields

| Field                                 | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `name`                                | *str*                                 | :heavy_check_mark:                    | Slack Bot display name                | PipesHub Bot                          |
| `bot_token`                           | *str*                                 | :heavy_check_mark:                    | Slack Bot OAuth token                 | xoxb-example-token                    |
| `signing_secret`                      | *str*                                 | :heavy_check_mark:                    | Slack app signing secret              | abc123signingsecret                   |
| `agent_id`                            | *Optional[str]*                       | :heavy_minus_sign:                    | Optional agent ID to link to this bot |                                       |