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
credentials**, except the `personal_access_tokens` ones. Create an OAuth app with
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

The `personal_access_tokens` examples are different: those endpoints need an
interactive user session and reject OAuth tokens. These examples sign in
with `PIPESHUB_TEST_USER_EMAIL` and `PIPESHUB_TEST_USER_PASSWORD` (password sign-in,
no MFA) and use the session's access token.

Requests that wait for an AI answer can take a minute or more, so those examples set
a 300 second timeout.

## Examples

Every example creates what it needs (a conversation, agent, knowledge base
or token) and deletes it again at the end, unless noted.

### conversation

| Example | What it does |
| --- | --- |
| `create_conversation.py` | Creates a conversation and waits for the full answer (non-streaming). |
| `add_message.py` | Adds a follow-up message and waits for the full answer (non-streaming). |
| `get_archived_conversations.py` | Archives a conversation and lists archived conversations. |
| `search_archived_conversations.py` | Archives a conversation and searches archived conversations by title. |
| `cancel_conversation_stream.py` | Starts a streaming chat with a `run_id` and cancels it after the first chunk of text. |

The other scripts in `conversation/` cover streaming chat, get, list, rename,
archive, unarchive, delete, regenerate and feedback.

### KB

| Example | What it does |
| --- | --- |
| `kb/get_upload_limits.py` | Gets the maximum files per upload and the maximum file size. |
| `records/get_record_by_id.py` | Uploads `PIPESHUB_UPLOAD_PATH` into a new knowledge base and gets the record. |
| `record_groups/reindex_record_group.py` | Finds the connector `PIPESHUB_CONNECTOR_NAME` in the knowledge hub and reindexes its first record group. |
| `trash/list_trash.py` | Deletes an uploaded record and lists the knowledge base's trash. |
| `trash/restore_record.py` | Deletes an uploaded record and restores it. |
| `trash/restore_records.py` | Deletes two uploaded records and restores both in one call. |

The `trash` examples need the workspace Labs setting **Move Deleted Records to the
Trash** (`ENABLE_SOFT_DELETE`). Without it, deleting a record removes it permanently
and there is nothing to list or restore.

`reindex_record_group.py` needs a connector record group. A knowledge base or a
knowledge base folder is not a record group. The example browses with the knowledge
hub methods, which are deprecated but are still the way to list a connector's
record groups. It doesn't create or delete anything.

### personal_access_tokens

| Example | What it does |
| --- | --- |
| `list_personal_access_token_scopes.py` | Lists the scopes a token can be granted. |
| `create_personal_access_token.py` | Creates a token with two scopes and a 30-day expiry. |
| `list_personal_access_tokens.py` | Lists your tokens. |
| `revoke_personal_access_token.py` | Revokes one of your tokens. |
| `admin_list_personal_access_tokens.py` | Lists every token in the organization (admin only). |
| `admin_revoke_personal_access_token.py` | Revokes any user's token (admin only). |

All of them sign in with email and password (see Authentication). `expiry_days`
accepts 30, 90, 365 or `"never"`. The examples revoke every token they create.

### connectors

| Example | What it does |
| --- | --- |
| `rss_connector.py` | Finds RSS in the connector registry, creates a team RSS connector for `PIPESHUB_RSS_FEED_URL`, turns its sync on, waits until every record is indexed, searches the connector, then turns the sync off and deletes it. |
| `gmail_workspace_connector.py` | Creates a team Gmail Workspace connector with a Google service account with domain-wide delegation (`PIPESHUB_GOOGLE_SERVICE_ACCOUNT_FILE`, `PIPESHUB_GOOGLE_ADMIN_EMAIL`), mail received in the last 7 days, syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `drive_workspace_connector.py` | Creates a team Drive Workspace connector with the same Google service account, files modified in the last 30 days, one drive when `PIPESHUB_GOOGLE_DRIVE_ID` is set or the connector lists any, syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `confluence_connector.py` | Creates a team Confluence connector with an Atlassian API token (`PIPESHUB_ATLASSIAN_BASE_URL`, `PIPESHUB_ATLASSIAN_EMAIL`, `PIPESHUB_ATLASSIAN_API_TOKEN`), one space (`PIPESHUB_CONFLUENCE_SPACE_KEY`, or the first), syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `jira_connector.py` | Creates a team Jira connector with the same Atlassian API token, one project (`PIPESHUB_JIRA_PROJECT_KEY`, or the first) and issues modified in the last 30 days, syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `s3_connector.py` | Creates a team S3 connector with an access key (`PIPESHUB_S3_ACCESS_KEY`, `PIPESHUB_S3_SECRET_KEY`), one bucket (`PIPESHUB_S3_BUCKET`, or the first), syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `azure_files_connector.py` | Creates a team Azure Files connector with the storage account connection string (`PIPESHUB_AZURE_FILES_CONNECTION_STRING`), limits its sync to one file share (`PIPESHUB_AZURE_FILES_SHARE`, or the first it can see), syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. |
| `slack_workspace_connector.py` | Creates a team "Slack Workspace" connector with a bot token (`PIPESHUB_SLACK_BOT_TOKEN`), limits its sync to one channel (`PIPESHUB_SLACK_CHANNEL_ID`, or the first the bot can see) and the last 7 days with `update_connector_filters_sync_config`, syncs, waits until indexing finishes, searches it, then turns the sync off and deletes it. Slack records keep Slack's permissions, so search only finds them for PipesHub users whose email matches a member of the channel; the example says so instead of failing when the caller sees none. |

Gmail, Drive, Confluence, Jira and Slack keep the source's permissions, so search only finds their records for PipesHub users whose email has access in the source; the examples report that instead of failing.
Jira and Confluence use an Atlassian API token rather than the OAuth sign-in, so
they run without a browser.

The OAuth app needs `connector:read`, `connector:write`, `connector:sync`,
`connector:delete` and `semantic:write`. The feed defaults to Hacker News, whose
server currently refuses the RSS connector's requests (HTTP 419), so the sync
fails its connection test; any other public feed works.

## Environment variables

See `.env.example` for the full list.

| Variable | Used by |
| --- | --- |
| `PIPESHUB_BASE_URL` | All examples. API root without `/api/v1`. |
| `PIPESHUB_CLIENT_ID`, `PIPESHUB_CLIENT_SECRET`, `PIPESHUB_TOKEN_URL` | OAuth2 client credentials for the examples in the tables above. `PIPESHUB_TOKEN_URL` is optional. |
| `PIPESHUB_BEARER_AUTH` | The older examples only: a JWT access token. |
| `PIPESHUB_TEST_USER_EMAIL`, `PIPESHUB_TEST_USER_PASSWORD` | `personal_access_tokens` examples. |
| `PIPESHUB_UPLOAD_PATH` | KB examples that upload a file. |
| `PIPESHUB_MODEL_KEY`, `PIPESHUB_MODEL_NAME`, `PIPESHUB_MODEL_PROVIDER` | Examples that create an agent. |
| `PIPESHUB_CONNECTOR_NAME` | `KB/record_groups/reindex_record_group.py`. |
| `PIPESHUB_GOOGLE_SERVICE_ACCOUNT_FILE`, `PIPESHUB_GOOGLE_ADMIN_EMAIL` | Gmail and Drive Workspace examples. |
| `PIPESHUB_ATLASSIAN_BASE_URL`, `PIPESHUB_ATLASSIAN_EMAIL`, `PIPESHUB_ATLASSIAN_API_TOKEN` | Confluence and Jira examples. |
| `PIPESHUB_S3_ACCESS_KEY`, `PIPESHUB_S3_SECRET_KEY` | S3 example. Every connector example also takes an optional item to sync and a `*_SEARCH_QUERY`; see `.env.example`. |
| `PIPESHUB_AZURE_FILES_CONNECTION_STRING`, `PIPESHUB_AZURE_FILES_SHARE`, `PIPESHUB_AZURE_FILES_SEARCH_QUERY` | `connectors/azure_files_connector.py`: the connection string (required), the share and the search query (optional). |
| `PIPESHUB_SLACK_BOT_TOKEN`, `PIPESHUB_SLACK_CHANNEL_ID`, `PIPESHUB_SLACK_SEARCH_QUERY` | `connectors/slack_workspace_connector.py`: the bot token (required), the channel id and the search query (optional). |
| `PIPESHUB_RSS_FEED_URL` | Optional, for `connectors/rss_connector.py` (default Hacker News). |
| `AGENT_KEY`, `CONNECTOR_APP_KEY` | `agent_conversation` examples. |
