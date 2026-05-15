# Metrics

Optional telemetry captured alongside the feedback


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `time_to_feedback`                                 | *Optional[float]*                                  | :heavy_minus_sign:                                 | Time from response delivery to feedback submission |
| `user_interaction_time`                            | *Optional[float]*                                  | :heavy_minus_sign:                                 | Total time the user spent reviewing the response   |
| `feedback_session_id`                              | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `user_agent`                                       | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `platform`                                         | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |