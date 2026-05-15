# Feedback

The feedback entry just appended to the message. Echoes
the fields supplied in the request plus server-stamped
`feedbackProvider`, `timestamp`, and `metrics`.



## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `is_helpful`                                                                       | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Echoed from the request when supplied.                                             |
| `ratings`                                                                          | Dict[str, *float*]                                                                 | :heavy_minus_sign:                                                                 | Echoed per-aspect ratings (values 1–5).                                            |
| `categories`                                                                       | List[[models.CategoryResponse](../models/categoryresponse.md)]                     | :heavy_minus_sign:                                                                 | Echoed categories from the request.                                                |
| `comments`                                                                         | [Optional[models.CommentsResponse]](../models/commentsresponse.md)                 | :heavy_minus_sign:                                                                 | Echoed free-text comments from the request.                                        |
| `feedback_provider`                                                                | *str*                                                                              | :heavy_check_mark:                                                                 | User who submitted the feedback. Always present.                                   |
| `timestamp`                                                                        | *int*                                                                              | :heavy_check_mark:                                                                 | Submission time as epoch milliseconds (not an ISO 8601<br/>datetime). Always present.<br/> |
| `metrics`                                                                          | [models.MetricsResponse](../models/metricsresponse.md)                             | :heavy_check_mark:                                                                 | Telemetry recorded server-side alongside the feedback.<br/>Always present.<br/>    |