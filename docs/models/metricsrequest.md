# MetricsRequest

Optional client-supplied telemetry.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `user_interaction_time`                                                        | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Total time the user spent reviewing the response, in milliseconds.             |
| `feedback_session_id`                                                          | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Opaque session identifier used by the client to group related feedback events. |