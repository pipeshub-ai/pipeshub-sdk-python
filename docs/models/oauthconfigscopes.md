# OAuthConfigScopes

OAuth scopes copied from the registry when the configuration was created, by use case


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `personal_sync`                           | List[*str*]                               | :heavy_minus_sign:                        | Scopes requested for a personal connector |
| `team_sync`                               | List[*str*]                               | :heavy_minus_sign:                        | Scopes requested for a team connector     |
| `agent`                                   | List[*str*]                               | :heavy_minus_sign:                        | Scopes requested for agent tools          |