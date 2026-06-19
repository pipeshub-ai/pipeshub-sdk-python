# Agent conversation examples

Scripts demonstrating agent chat over Server-Sent Events (SSE), conversation management, archives, message feedback, and regeneration.

See [`../README.md`](../README.md) for setup and environment configuration.

## Environment

Copy [`../.env.example`](../.env.example) to `examples/.env` and set `PIPESHUB_BEARER_AUTH`, `PIPESHUB_BASE_URL`, `AGENT_KEY`, and `CONNECTOR_APP_KEY` before running.

## Shared helpers

[`helpers.py`](helpers.py) provides `stream_bot_reply()` — pass the SDK stream object, print the bot reply, and read the `complete` event from raw SSE lines.

### `bot_response_message_id`

The feedback and regeneration examples read the latest `bot_response` message from the stream `complete` payload. The `_id` on that message is the value to pass to API methods that expect `message_id`. It is a message document ID, not an agent ID.

## Scripts

| Script | SDK operations demonstrated |
| --- | --- |
| `create_conversation_stream_and_add_message.py` | `stream_agent_conversation`, `stream_agent_conversation_message` |
| `get_conversation_by_id.py` | `get_agent_conversation_by_id` |
| `get_all_conversations.py` | `list_agent_conversations` |
| `update_conversation_title.py` | `update_agent_conversation_title` |
| `archive_unarchive.py` | `archive_agent_conversation`, `unarchive_agent_conversation` |
| `list_all_archived_conversations.py` | create, archive, `list_agent_conversation_archives` |
| `list_archives_grouped.py` | `list_agent_archived_conversations_grouped` |
| `add_message_feedback.py` | `update_agent_conversation_message_feedback` |
| `regenerate_message_stream.py` | `regenerate_agent_conversation_message` |

## Run examples

From `examples/`:

```bash
uv run python agent_conversation/create_conversation_stream_and_add_message.py
uv run python agent_conversation/get_conversation_by_id.py
uv run python agent_conversation/get_all_conversations.py
uv run python agent_conversation/update_conversation_title.py
uv run python agent_conversation/archive_unarchive.py
uv run python agent_conversation/list_all_archived_conversations.py
uv run python agent_conversation/list_archives_grouped.py
uv run python agent_conversation/add_message_feedback.py
uv run python agent_conversation/regenerate_message_stream.py
```

From the repository root:

```bash
uv run --project examples python examples/agent_conversation/create_conversation_stream_and_add_message.py
```

## Notes

- Streaming examples print bot output live. Pass `print_output=False` to `stream_bot_reply()` to wait silently.
- Scripts that create or archive conversations create their own test data.
- Feedback and regeneration require a `bot_response` message ID. Examples read it from the stream `complete` payload rather than hard-coding IDs.
