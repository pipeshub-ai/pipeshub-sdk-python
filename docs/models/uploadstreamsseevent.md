# UploadStreamSSEEvent

Server-Sent Event envelope for the KB streaming upload endpoint
(`POST /knowledgeBase/{kbId}/upload`, with optional `folderId` query param).

These endpoints respond with `Content-Type: text/event-stream`: the upload
and its per-file progress are a single request. The body streams one
terminal event per file, then a final `done` summary, then closes. `data`
is a JSON-encoded string whose decoded shape depends on `event`:

- `file:succeeded` — see `UploadSucceededFileDetail`. The file was
  uploaded and its record created; content indexing then continues
  asynchronously.
- `file:failed` — see `UploadFailedFileDetail`. Covers files rejected up
  front (oversize / unsupported type — these carry `reason`), files that
  failed the storage upload (`stage: "upload"`), and files the indexing
  service could not create (`stage: "index"`).
- `done` — see `UploadDoneSummary`. Final event; the stream closes after it.
- `error` — `{ "message": string }`. Emitted only on a catastrophic
  mid-stream failure (after the 200 headers were already sent), then the
  stream closes. Clients MUST treat any file without a terminal
  `file:succeeded` / `file:failed` as failed when this is received.

The stream also emits SSE comment heartbeats (`: keepalive`) roughly every
1s during slow work; these carry no `event`/`data` and should be ignored.
Authentication, permission, and request-shape failures occur BEFORE the
stream starts and are returned as ordinary 4xx JSON errors (not stream
events).



## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `event`                                                                              | [Optional[models.UploadStreamSSEEventEvent]](../models/uploadstreamsseeventevent.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `data`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | JSON-encoded event payload. Shape depends on `event`.                                |