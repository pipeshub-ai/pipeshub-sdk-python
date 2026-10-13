# Changelog

## 1.7.0

Compatible with PipesHub [v0.9.1](https://github.com/pipeshub-ai/pipeshub-ai/releases/tag/v0.9.1).

> **1.7.0 is a minor version, but it contains breaking changes.** Read this list before you upgrade.

### Breaking changes and how to fix them

#### Renaming a conversation no longer returns `messages`

`update_conversation_title` returns only the updated conversation fields. Read the messages with a second call.

```python
# ❌ 1.6.0
# res = sdk.conversations.update_conversation_title(conversation_id=cid, title=title)
# messages = res.conversation.messages

# ✅ 1.7.0
sdk.conversations.update_conversation_title(conversation_id=cid, title=title)
res = sdk.conversations.get_conversation_by_id(conversation_id=cid)
messages = (res.conversation.messages or []) if res.conversation else []
```

#### Deleting an agent conversation: `conversation` can be empty

`conversation` is now a stored conversation, an empty object, or `None`. Your code runs as before, but type checkers need a check before you read a field.

```python
from pipeshub_sdk import models

res = sdk.agents.delete_agent_conversation_by_id(agent_key=agent_key, conversation_id=cid)
c = res.conversation
if isinstance(c, models.StoredAgentConversation):
    print(c.id)
```

#### Some type names changed

Use the new name. The data inside is the same. All names are in `pipeshub_sdk.models`.

| Old name | New name |
|---|---|
| `Meta` | `MessageFeedbackUpdateResponseMeta` |
| `ModelInfo` | `ConversationListItemModelInfo` |
| `IsArchived` | `ListAgentConversationsIsArchived` |
| `MessageMessageType` | `MessageMessageType1` |
| `GetConversationByIDMessageMessageType` | `MessageMessageType2` |

The `UpdateConversationTitle*` message types are removed, because renaming a conversation no longer returns messages.

```python
# ❌ 1.6.0
# from pipeshub_sdk.models import Meta, ModelInfo, IsArchived

# ✅ 1.7.0
from pipeshub_sdk.models import (
    MessageFeedbackUpdateResponseMeta,
    ConversationListItemModelInfo,
    ListAgentConversationsIsArchived,
)
```

#### Two errors have a new error class

A `500` from `knowledge_base.upload_records` is now raised as `ErrorResponse`. A `410` from `user_account.authenticate` is now `PipeshubDefaultError`, not `ErrorResponse`. Both classes extend `PipeshubError`, so catch the parent class and check the status code.

```python
from pipeshub_sdk import errors

try:
    sdk.knowledge_base.upload_records(...)
except errors.PipeshubError as e:
    if e.status_code == 500:
        ...  # handle the server error
    else:
        raise
```

#### A citation can have two shapes

A message citation is now a `CitationReference` or a `PopulatedCitationReference`. Your code runs as before, but type checkers need a check before you read a field.

```python
from pipeshub_sdk import models

for c in msg.citations or []:
    if isinstance(c, models.CitationReference):
        print(c.citation_id)
```

### Behavior notes (not breaking)

- **A user token on 22 endpoints.** OAuth apps, personal access tokens, user info, org auth config and reset password now send only the user token. If you set up only an app token, add a user token:
  ```python
  sdk = Pipeshub(security=models.Security(bearer_auth=user_token))
  ```
- **Conversation streams work.** `data` on `ConversationStreamSSEEvent` and `ConversationMessageStreamSSEEvent` is typed `Any`, as on the other stream models. The SDK decodes each event's JSON before validation, so the old `str` type rejected those events.
