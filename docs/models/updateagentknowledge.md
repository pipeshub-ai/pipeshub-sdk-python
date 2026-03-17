# UpdateAgentKnowledge


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `connector_id`                                                                   | *str*                                                                            | :heavy_check_mark:                                                               | ID of the connector providing this knowledge                                     |
| `filters`                                                                        | [Optional[models.UpdateAgentFiltersUnion]](../models/updateagentfiltersunion.md) | :heavy_minus_sign:                                                               | Filter criteria (JSON object or JSON string)                                     |