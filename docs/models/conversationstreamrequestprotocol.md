# ConversationStreamRequestProtocol

AG-UI is the only supported wire protocol. When present must be
`"agui"`. Omitting the field is equivalent — the server always
uses the AG-UI vocabulary (`RUN_STARTED`, `TEXT_MESSAGE_CONTENT`,
etc.). Kept in the schema for backward compatibility with callers
that already send it.



## Values

| Name   | Value  |
| ------ | ------ |
| `AGUI` | agui   |