# SSEEvent

Server-Sent Event envelope for streaming chat responses.

`data` is a JSON-encoded string whose shape depends on `event`.
Three events are emitted by the API layer and have stable shapes
documented on the streaming routes:

- `connected` — fired once on connection. Carries the newly created
  `conversationId` and `title` so the client can link the stream to
  a row before any tokens arrive.
- `complete` — fired once after the AI backend finishes. Carries the
  full persisted `conversation` and a `meta` block with `requestId`,
  `timestamp` and `duration`.
- `error` — fired when the stream fails. Carries an `error` message
  and optional `details`. The conversation row is marked FAILED
  before the stream closes.

All other events are forwarded verbatim from the AI backend; their
payloads are AI-backend defined and may evolve. Currently observed
names include `status`, `answer_chunk`, `tool_call`, `tool_calls`,
`tool_result`, `tool_success`, `tool_error`,
`tool_execution_complete`, `restreaming`, and `metadata`.



## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `event`                                                      | [Optional[models.SSEEventEvent]](../models/sseeventevent.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `data`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | JSON-encoded event payload. Shape depends on `event`.        |