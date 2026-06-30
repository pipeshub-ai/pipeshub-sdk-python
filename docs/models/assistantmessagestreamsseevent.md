# AssistantMessageStreamSSEEvent

Server-Sent Event envelope for non-agent assistant follow-up message
streams (`internal_search` / `web_search` chat modes) on an existing
conversation. `data` is a JSON-encoded string whose shape depends on
`event`.

Same event vocabulary as the conversation-creation stream — only the
`connected` and `complete` payloads differ because the conversation
already exists when this route is called.

Three events are emitted by the API layer with stable, server-defined
shapes:

- `connected` — `{ "message": string }`. Fired once on connection.
  No `conversationId` or `title` is included because the caller
  already passed the conversation ID in the URL.
- `complete` — `{ "conversation": Conversation, "recordsUsed": number,
  "meta": { "requestId": string, "timestamp": string,
  "duration": number, "recordsUsed": number } }`. Fired once after
  the AI backend finishes. `recordsUsed` is the count of citations
  attached to the new assistant message.
- `error` — `{ "error": string, "details"?: string }`. Fired when the
  stream fails; the conversation row is marked FAILED before close.

The remaining events are forwarded from the Python query service.
Their payloads are AI-backend defined and may evolve:

- `status` — progress message describing the current pipeline stage
  (for example `started`, `transforming`, `searching`, `processing`,
  `checking_tools`, `generating_answer`). `transforming` is common on
  this route because follow-up turns always have prior history to
  rewrite the query against.
- `answer_chunk` — incremental token batch with running `accumulated`
  text and any new `citations`.
- `tool_calls` — the assistant requested one or more tool calls.
  Carries the assistant message that triggered the tool round.
- `tool_call` — emitted once per individual tool invocation as it
  starts. Payload includes `tool_name`, `tool_args`, and `call_id`.
- `tool_success` — a tool finished successfully. Payload includes
  `tool_name`, `summary`, `call_id`, and any `record_info`.
- `tool_error` — a tool invocation failed. Payload includes
  `tool_name`, `error`, and `call_id`.
- `restreaming` — the LLM is being restarted with new context, for
  example before a citation-verification pass.

Clients should ignore unknown event names rather than treating them
as errors.



## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `event`                                                                                                  | [Optional[models.AssistantMessageStreamSSEEventEvent]](../models/assistantmessagestreamsseeventevent.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |
| `data`                                                                                                   | *Optional[Any]*                                                                                          | :heavy_minus_sign:                                                                                       | JSON-encoded event payload. Shape depends on `event`.                                                    |