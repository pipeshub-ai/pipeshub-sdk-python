# ToolApprovalAnswer

The person's answer to a tool approval card. The web app sends it with the query
`Tool approval: allow` or `Tool approval: deny`, and the request carries on the turn that
stopped on the card: the saved call runs (when allowed) and its result answers the call
the model made, in the same reply. The call is the one saved server-side when the card was
shown (answerable for 15 minutes, settled once, bound to the asking user and
conversation); only its id and the answer travel here. A reply that answered a card
can't be regenerated.



## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `approval_id`                                                                                                                    | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | N/A                                                                                                                              |
| `decision`                                                                                                                       | [models.Decision](../models/decision.md)                                                                                         | :heavy_check_mark:                                                                                                               | N/A                                                                                                                              |
| `remember`                                                                                                                       | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | "Don't ask again for this tool": the answer becomes the person's own rule for the<br/>tool (Pre-approved for allow, Deny for deny).<br/> |