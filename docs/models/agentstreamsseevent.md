# AgentStreamSSEEvent

SSE event envelope for `POST /agents/{agentKey}/conversations/stream`.
Event names are listed in `event`; payload JSON is carried in `data`.



## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `event`                                                                            | [Optional[models.AgentStreamSSEEventEvent]](../models/agentstreamsseeventevent.md) | :heavy_minus_sign:                                                                 | SSE event name.<br/>See the enum for possible values.<br/>                         |
| `data`                                                                             | *Optional[Any]*                                                                    | :heavy_minus_sign:                                                                 | JSON-encoded event payload.<br/>Shape depends on `event`.<br/>                     |