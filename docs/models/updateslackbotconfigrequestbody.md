# UpdateSlackBotConfigRequestBody

Request payload


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `name`                  | *str*                   | :heavy_check_mark:      | Bot display name        |
| `bot_token`             | *str*                   | :heavy_check_mark:      | Slack bot token         |
| `signing_secret`        | *str*                   | :heavy_check_mark:      | Slack signing secret    |
| `agent_id`              | *OptionalNullable[str]* | :heavy_minus_sign:      | Associated agent ID     |