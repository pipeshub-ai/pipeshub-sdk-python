# AgentWebSearch

Web search provider attached to this agent. Null when none is configured.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `provider`                                                         | *str*                                                              | :heavy_check_mark:                                                 | Provider identifier (e.g. "tavily", "serper", "exa", "duckduckgo") |
| `provider_key`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `provider_label`                                                   | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |