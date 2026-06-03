# WebSearchProvidersResponse

Response for getWebSearchProviders


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `status`                                                                                 | [models.WebSearchProvidersResponseStatus](../models/websearchprovidersresponsestatus.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `providers`                                                                              | List[[models.WebSearchProviderItem](../models/websearchprovideritem.md)]                 | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `settings`                                                                               | [models.WebSearchSettings](../models/websearchsettings.md)                               | :heavy_check_mark:                                                                       | Normalized web search global settings returned by getWebSearchProviders                  |
| `message`                                                                                | *str*                                                                                    | :heavy_check_mark:                                                                       | Human-readable status (empty list vs populated providers)                                |