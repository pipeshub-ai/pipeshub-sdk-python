# MessageFeedbackSubmitRequest

Gateway request body for submitting message feedback (Zod
`feedbackBodySchema`). All fields are optional; an empty object is
accepted. Matches the first-party chat UI payload shape.



## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `is_helpful`                                                                                               | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | Overall helpfulness signal (thumbs up/down).                                                               |
| `categories`                                                                                               | List[[models.MessageFeedbackSubmitRequestCategory](../models/messagefeedbacksubmitrequestcategory.md)]     | :heavy_minus_sign:                                                                                         | Issue or positive categories that apply to the response.                                                   |
| `comments`                                                                                                 | [Optional[models.MessageFeedbackSubmitRequestComments]](../models/messagefeedbacksubmitrequestcomments.md) | :heavy_minus_sign:                                                                                         | Free-text comments grouped by sentiment.                                                                   |