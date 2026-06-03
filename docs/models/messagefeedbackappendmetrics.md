# MessageFeedbackAppendMetrics

Telemetry recorded server-side alongside the feedback. Always present
on append responses.



## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `time_to_feedback`                                                              | *float*                                                                         | :heavy_check_mark:                                                              | Milliseconds between message creation and feedback submission.<br/>Always present.<br/> |
| `user_agent`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Value of the `User-Agent` request header captured server-side.                  |