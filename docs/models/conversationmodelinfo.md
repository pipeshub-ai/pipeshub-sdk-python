# ConversationModelInfo

AI model configuration recorded against a conversation or message.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `model_key`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Stable identifier of the configured model record               |
| `model_name`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Provider-facing model name (e.g. `gpt-4o-mini`)                |
| `model_provider`                                               | *Optional[str]*                                                | :heavy_minus_sign:                                             | Provider key (e.g. `openai`, `anthropic`)                      |
| `model_friendly_name`                                          | *Optional[str]*                                                | :heavy_minus_sign:                                             | Human-readable display name                                    |
| `chat_mode`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Chat mode used for this turn (e.g. `quick`, `internal_search`) |