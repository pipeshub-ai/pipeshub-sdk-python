# SearchArchivedConversationsProjectVisibility

Only meaningful when `projectId` is set. `private` (default)
keeps the conversation visible to its owner only; `project`
exposes it to every member of the linked project. See
`PATCH /conversations/{conversationId}/project-visibility`.



## Values

| Name      | Value     |
| --------- | --------- |
| `PRIVATE` | private   |
| `PROJECT` | project   |