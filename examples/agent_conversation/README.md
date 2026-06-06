# Agent conversation examples

Scripts demonstrating agent chat over Server-Sent Events (SSE), conversation management, archives, message feedback, and regeneration.

See [`../README.md`](../README.md) for setup and environment configuration.

## Environment

All scripts take a path to a `.env` file as their first argument. Copy [`../.env.example`](../.env.example) to `examples/.env` and fill in values before running.

Variables used by these examples:

| Variable | Required | Used for |
| --- | --- | --- |
| `PIPESHUB_TEST_USER_EMAIL` | yes | Authentication |
| `PIPESHUB_TEST_USER_PASSWORD` | yes | Authentication |
| `PIPESHUB_BASE_URL` | no | API host (default `http://localhost:3000`) |
| `PIPESHUB_AGENT_KEY` | no | Target agent for conversation calls |
| `CONNECTOR_ID` | no | Default retrieval filter (`apps`) in streaming examples |
| `PIPESHUB_AGENT_MODEL_KEY` | no | Only if calling `create_agent_with_web_search()` |

## Shared helpers

[`helpers.py`](helpers.py) provides reusable utilities:

| Function | Purpose |
| --- | --- |
| `agent_key()` | Resolves agent key from env or default |
| `connector_id()` | Resolves `CONNECTOR_ID` from env or default |
| `default_filters()` | Builds default `FiltersTypedDict` for streaming (`apps`) |
| `first_llm_model_key()` | Resolves `PIPESHUB_AGENT_MODEL_KEY` or picks an available LLM |
| `decode_complete()` | Parses the stream `complete` event payload |
| `stream_create()` | Starts a new conversation and streams the first bot reply |
| `stream_create_async()` | Async version of `stream_create()` |
| `stream_add_message()` | Appends a user message and streams the bot reply |
| `stream_regenerate()` | Regenerates a `bot_response` message via SSE |
| `update_title()` | Updates conversation title |
| `update_title_async()` | Async version of `update_title()` |
| `print_conversation()` | Fetches and prints a conversation by ID |
| `format_activity()` | Formats conversation activity timestamps for display |
| `archive_conversation()` / `delete_conversation()` | Archive or delete a conversation |
| `list_archived()` | Paginated list of archived conversations |
| `create_agent_with_web_search()` | Creates an example web-search-enabled agent |

### `bot_response_message_id`

`stream_create()` and `stream_create_async()` return `(conversation_id, title, answer, bot_response_message_id)`. The fourth value is the `_id` of the latest `bot_response` message in the stream `complete` payload. Pass it to API methods that expect `message_id` (feedback, regeneration). It is a message document ID, not an agent ID.

## Scripts

| Script | SDK operations demonstrated |
| --- | --- |
| `create_conversation_stream_and_add_message.py` | `stream_agent_conversation`, `stream_agent_conversation_message` |
| `get_conversation_by_id.py` | `get_agent_conversation_by_id` |
| `get_all_conversations.py` | `list_agent_conversations` (owned + shared) |
| `update_conversation_title.py` | `update_agent_conversation_title` |
| `archive_unarchive.py` | `archive_agent_conversation`, `unarchive_agent_conversation` |
| `list_all_archived_conversations.py` | create, archive, `list_agent_conversation_archives`, delete |
| `list_archives_grouped.py` | `list_agent_archived_conversations_grouped` |
| `add_message_feedback.py` | `update_agent_conversation_message_feedback` |
| `regenerate_message_stream.py` | `regenerate_agent_conversation_message` |

## Run examples

From the repository root (using `examples/.env`):

```bash
uv run python examples/agent_conversation/create_conversation_stream_and_add_message.py examples/.env
uv run python examples/agent_conversation/get_conversation_by_id.py examples/.env
uv run python examples/agent_conversation/get_all_conversations.py examples/.env
uv run python examples/agent_conversation/update_conversation_title.py examples/.env
uv run python examples/agent_conversation/archive_unarchive.py examples/.env
uv run python examples/agent_conversation/list_all_archived_conversations.py examples/.env
uv run python examples/agent_conversation/list_archives_grouped.py examples/.env
uv run python examples/agent_conversation/add_message_feedback.py examples/.env
uv run python examples/agent_conversation/regenerate_message_stream.py examples/.env
```

## Notes

- Streaming examples print bot output live. Some scripts pass `print_bot=False` to reduce console noise.
- Scripts that archive or delete conversations create their own test data. `list_all_archived_conversations.py` cleans up conversations it creates.
- Feedback and regeneration require a `bot_response` message ID. Examples obtain this from `stream_create()` rather than hard-coding IDs.
