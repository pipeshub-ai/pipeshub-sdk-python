# Changelog

## 1.7.0

Compatible with PipesHub [v0.9.1](https://github.com/pipeshub-ai/pipeshub-ai/releases/tag/v0.9.1). This version is generated from the PipesHub v0.9.1 API spec. The changes for all three SDKs are also in the [PipesHub changelog](https://github.com/pipeshub-ai/pipeshub-ai/blob/main/changelog/0.9.0.md#sdks--170-typescript-python-go).

> **1.7.0 is a minor version, but it contains breaking changes.** Read the list below before you upgrade.

### What's new

- **Projects:** a new `projects` namespace. You can create, list, get, update, delete, archive, unarchive, pin and unpin projects. You can also manage project members, the project knowledge base, and a project's conversations. `conversations.set_conversation_project`, `conversations.set_conversation_project_visibility`, `projects.set_agent_conversation_project` and `projects.set_agent_conversation_project_visibility` move a conversation into a project and set its visibility.
- **Non-streaming chat:** `conversations.create_conversation`, `conversations.add_message`, `agents.create_agent_conversation` and `agents.add_agent_conversation_message` return the finished answer as JSON.
- **Stop a running answer:** `conversations.cancel_conversation_stream` and `agents.cancel_agent_conversation_stream`.
- **Examples:** `examples/` has updated agent conversation and conversation samples.

### Fixes

- **Conversation streams:** `data` on `ConversationStreamSSEEvent` and `ConversationMessageStreamSSEEvent` is typed `Any`, as on the other stream models. The SDK decodes each event's JSON before validation, so the old `str` type rejected those events.

### Breaking changes and how to fix them

#### Renaming a conversation no longer returns `messages`

Get the messages with a second call.

```python
sdk.conversations.update_conversation_title(conversation_id=cid, title=title)
msgs = sdk.conversations.get_conversation_by_id(conversation_id=cid).conversation.messages
```

#### Delete agent conversation: `conversation` can be empty

This matters only for type checkers. Check the type before you read the conversation.

```python
c = res.conversation
if isinstance(c, models.StoredAgentConversation): print(c.id)
```

#### Some type names changed

Use the new name. The data inside is the same.

| Old name | New name |
|---|---|
| `Meta` | `MessageFeedbackUpdateResponseMeta` |
| `ModelInfo` | `ConversationListItemModelInfo` |
| `IsArchived` | `ListAgentConversationsIsArchived` |
| `MessageMessageType` | `MessageMessageType1` |
| `GetConversationByIDMessageMessageType` | `MessageMessageType2` |

```python
# ❌ from pipeshub_sdk.models import ModelInfo
# ✅
from pipeshub_sdk.models import ConversationListItemModelInfo
```

The `UpdateConversationTitle*` message types are removed, because renaming a conversation no longer returns messages.

#### Two errors have a new error class

A `500` from `knowledge_base.upload_records` is now an `ErrorResponse`. A `410` from `user_account.authenticate` is now the default `PipeshubError` instead of an `ErrorResponse`. Catch the parent error class, and check the status code.

```python
from pipeshub_sdk import errors

try: ...
except errors.PipeshubError as e:
    if e.status_code == 500: ...
```

#### A citation can have two shapes

This matters only for type checkers. A message citation is now a `CitationReference` or a `PopulatedCitationReference`. Check with `isinstance(c, models.CitationReference)`.

### Behavior notes (not breaking)

- **Login on 22 endpoints** (OAuth apps, access tokens, user info, org auth config, reset password): these calls send only the user token. If you set up only an app token, add a user token.
  ```python
  sdk = Pipeshub(security=models.Security(bearer_auth=user_token))
  ```
