# SearchArchivedConversationsSummary


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `total_matches`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | Combined match count across both collections              |
| `assistant_matches`                                       | *Optional[int]*                                           | :heavy_minus_sign:                                        | Match count in the assistant (`Conversation`) collection  |
| `agent_matches`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | Match count in the agent (`AgentConversation`) collection |
| `search_query`                                            | *Optional[str]*                                           | :heavy_minus_sign:                                        | Trimmed search term that was applied                      |