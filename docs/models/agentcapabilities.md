# AgentCapabilities

Per-request agent capability toggles. Only meaningful when `chatMode`
selects an agent mode; ignored otherwise. Each field falls back to its
own `default` below when omitted — a missing flag is not uniformly
`true`. Omitting the whole object applies every default.



## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `internal_search`                                                         | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Whether the agent may search internal knowledge bases for this turn.      |
| `web_search`                                                              | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Whether the agent may perform web search for this turn.                   |
| `deep_search`                                                             | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Whether the agent may use deeper, higher-latency retrieval for this turn. |