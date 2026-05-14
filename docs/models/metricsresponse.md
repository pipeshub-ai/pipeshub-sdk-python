# MetricsResponse

Telemetry recorded server-side alongside the feedback.
Always present.



## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `time_to_feedback`                                                              | *float*                                                                         | :heavy_check_mark:                                                              | Milliseconds between message creation and feedback<br/>submission. Always present.<br/> |
| `user_interaction_time`                                                         | *Optional[float]*                                                               | :heavy_minus_sign:                                                              | Echoed from `metrics.userInteractionTime` in the request when supplied.         |
| `feedback_session_id`                                                           | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Echoed from `metrics.feedbackSessionId` in the request when supplied.           |
| `user_agent`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Value of the `User-Agent` request header captured server-side.                  |