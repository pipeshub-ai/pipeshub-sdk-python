## Setup

Install the dependencies, then run any example script with `python`.

```bash
pip install "pipeshub-sdk>=1.8.0" python-dotenv
```

Copy `.env.example` to `.env` in this directory and fill it in. Each script loads
`examples/.env`. Variables that are already set in the environment take precedence
over the file.

```bash
cp .env.example .env
python conversation/create_conversation.py
```

## Authentication

The scripts listed in the tables below authenticate with **OAuth2 client
credentials**. Create an OAuth app with
the `client_credentials` grant and set `PIPESHUB_CLIENT_ID` and
`PIPESHUB_CLIENT_SECRET`. The SDK fetches the access token itself, from
`PIPESHUB_TOKEN_URL` or `${PIPESHUB_BASE_URL}/api/v1/oauth2/token` when that is
unset, and fetches a new one when it expires.

```python
security = models.Security(oauth2=models.SchemeOauth2(
    client_id=os.environ["PIPESHUB_CLIENT_ID"],
    client_secret=os.environ["PIPESHUB_CLIENT_SECRET"],
    token_url=f'{os.environ["PIPESHUB_BASE_URL"]}/api/v1/oauth2/token',
))
```

The older scripts in `agent/`, `agent_conversation/`, `semantic_search/` and the
rest of `conversation/` and `KB/` read a JWT access token from
`PIPESHUB_BEARER_AUTH` instead.

Requests that wait for an AI answer can take a minute or more, so those examples set
a 300 second timeout.

## Examples

The examples listed below show one SDK call each. IDs they need come from
environment variables (see the table at the end); create those resources first.

### conversation

| Example | What it does |
| --- | --- |
| `create_conversation.py` | Creates a conversation and waits for the full answer (non-streaming). Needs nothing. |
| `add_message.py` | Adds a follow-up message and waits for the answer (non-streaming). Needs `PIPESHUB_CONVERSATION_ID`. |
| `get_archived_conversations.py` | Lists archived conversations. |
| `search_archived_conversations.py` | Searches archived conversations by title. |
| `cancel_conversation_stream.py` | Cancels a streaming chat. Needs `PIPESHUB_CONVERSATION_ID` and `PIPESHUB_RUN_ID` (the `run_id` the stream was started with). |

The other scripts in `conversation/` cover streaming chat, get, list, rename,
archive, unarchive, delete, regenerate and feedback.

### KB

| Example | What it does |
| --- | --- |
| `kb/get_upload_limits.py` | Gets the maximum files per upload and the maximum file size. |
| `records/get_record_by_id.py` | Gets a record. Needs `PIPESHUB_RECORD_ID`. |
| `record_groups/reindex_record_group.py` | Reindexes a connector record group. Needs `PIPESHUB_RECORD_GROUP_ID`. |
| `trash/list_trash.py` | Lists a knowledge base's trash. Needs `PIPESHUB_KB_ID`. |
| `trash/restore_record.py` | Restores a record from the trash. Needs `PIPESHUB_RECORD_ID`. |
| `trash/restore_records.py` | Restores records from the trash in one call. Needs `PIPESHUB_RECORD_ID`. |

The `trash` examples need the workspace Labs setting **Move Deleted Records to the
Trash** (`ENABLE_SOFT_DELETE`). Without it, deleting a record removes it permanently
and there is nothing to list or restore.

`reindex_record_group.py` needs a connector record group. A knowledge base or a
knowledge base folder is not a record group.

### connectors

One file per operation in `connectors/`. They take the connector from
`PIPESHUB_CONNECTOR_ID` unless noted.

| Example | What it does |
| --- | --- |
| `get_connector_registry.py`, `get_connector_schema.py` | List connector types; get one type's schema (`PIPESHUB_CONNECTOR_TYPE`). |
| `test_connector_connection.py` | Tries auth settings for `PIPESHUB_CONNECTOR_TYPE` (a type that supports connection checks, e.g. PostgreSQL). |
| `get_connector_egress_ips.py` | Gets the IP addresses PipesHub connects from. |
| `list_connector_instances.py`, `create_connector_instance.py` | List instances; create a team RSS connector. |
| `get_connector_instance.py`, `delete_connector_instance.py`, `get_connector_stats.py` | Get, delete, or get stats of an instance. |
| `resync_connector.py`, `stop_connector_sync.py`, `toggle_connector.py` | Resync, stop a sync, flip sync on or off. |
| `get_connector_config.py`, `update_connector_config.py`, `update_connector_auth_config.py`, `update_connector_filters_sync_config.py` | Read or update a connector's configuration. |
| `get_connector_filters.py`, `save_connector_filters.py`, `get_filter_field_options.py` | Filters; the last one also needs `PIPESHUB_FILTER_KEY`. |
| `get_o_auth_authorization_url.py`, `handle_o_auth_callback.py` | OAuth sign-in for a connector; the callback needs `PIPESHUB_OAUTH_CODE` and `PIPESHUB_OAUTH_STATE`. |
| `get_o_auth_registry.py`, `get_o_auth_connector_type.py`, `list_o_auth_configs.py`, `list_o_auth_configs_by_type.py` | OAuth app registry and configurations. |
| `create_o_auth_config.py`, `get_o_auth_config.py`, `update_o_auth_config.py`, `delete_o_auth_config.py` | OAuth app configurations; all use `PIPESHUB_CONNECTOR_TYPE`, the last three also `PIPESHUB_OAUTH_CONFIG_ID`. |

## Environment variables

See `.env.example` for the full list.

| Variable | Used by |
| --- | --- |
| `PIPESHUB_BASE_URL` | All examples. API root without `/api/v1`. |
| `PIPESHUB_CLIENT_ID`, `PIPESHUB_CLIENT_SECRET`, `PIPESHUB_TOKEN_URL` | OAuth2 client credentials for the examples in the tables above. `PIPESHUB_TOKEN_URL` is optional. |
| `PIPESHUB_BEARER_AUTH` | The older examples only: a JWT access token. |
| `PIPESHUB_UPLOAD_PATH` | KB examples that upload a file. |
| `PIPESHUB_MODEL_KEY`, `PIPESHUB_MODEL_NAME`, `PIPESHUB_MODEL_PROVIDER` | Examples that create an agent. |
| `PIPESHUB_CONVERSATION_ID`, `PIPESHUB_MESSAGE_ID`, `PIPESHUB_RUN_ID` | IDs of an existing conversation, message and streaming run. |
| `PIPESHUB_AGENT_KEY` | Key of an existing agent. |
| `PIPESHUB_KB_ID`, `PIPESHUB_RECORD_ID`, `PIPESHUB_RECORD_GROUP_ID` | IDs of an existing knowledge base, record and connector record group. |
| `PIPESHUB_CONNECTOR_ID`, `PIPESHUB_CONNECTOR_TYPE` | A connector instance id; a connector type such as `RSS`. |
| `PIPESHUB_FILTER_KEY` | A filter key from the connector's filter schema. |
| `PIPESHUB_OAUTH_CONFIG_ID`, `PIPESHUB_OAUTH_CODE`, `PIPESHUB_OAUTH_STATE` | An OAuth app configuration id; the code and state from the provider's redirect. |
| `AGENT_KEY`, `CONNECTOR_APP_KEY` | `agent_conversation` examples. |
