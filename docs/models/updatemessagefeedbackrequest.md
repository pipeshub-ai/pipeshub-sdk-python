# UpdateMessageFeedbackRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `conversation_id`                                                                | *str*                                                                            | :heavy_check_mark:                                                               | Unique conversation identifier.                                                  |
| `message_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Identifier of the bot-response message being rated.                              |
| `body`                                                                           | [models.MessageFeedbackSubmitRequest](../models/messagefeedbacksubmitrequest.md) | :heavy_check_mark:                                                               | Request payload                                                                  |