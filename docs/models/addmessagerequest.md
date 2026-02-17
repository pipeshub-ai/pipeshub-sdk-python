# AddMessageRequest

Request body for adding a message to an existing conversation


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `query`                                          | *str*                                            | :heavy_check_mark:                               | The follow-up question or message content        | Can you elaborate on the revenue trends?         |
| `filters`                                        | [Optional[models.Filters]](../models/filters.md) | :heavy_minus_sign:                               | N/A                                              |                                                  |
| `model_key`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Override the model for this specific message     |                                                  |
| `model_name`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | Display name of the model                        |                                                  |
| `chat_mode`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Chat mode for this message                       |                                                  |