# MessageFeedback

Comprehensive feedback on an AI response. Feedback helps improve
the AI's performance and response quality over time.



## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `is_helpful`                                                   | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Overall helpfulness rating                                     |
| `ratings`                                                      | [Optional[models.Ratings]](../models/ratings.md)               | :heavy_minus_sign:                                             | N/A                                                            |
| `categories`                                                   | List[[models.Category](../models/category.md)]                 | :heavy_minus_sign:                                             | Categories of issues identified                                |
| `comments`                                                     | [Optional[models.Comments]](../models/comments.md)             | :heavy_minus_sign:                                             | N/A                                                            |
| `citation_feedback`                                            | List[[models.CitationFeedback](../models/citationfeedback.md)] | :heavy_minus_sign:                                             | Feedback on individual citations                               |
| `follow_up_questions_helpful`                                  | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Were the suggested follow-up questions helpful                 |