# AgentSkill

A skill linked to the agent, as returned by the agent detail graph
projection. Flat by design — a skill carries no sub-entities analogous
to a toolset's tools. Fields other than `name` are read straight off
the skill document and are null when unset.



## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `name`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Unique skill name, used to reference the skill on agent create/update. |
| `description`                                                          | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `category`                                                             | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `subcategory`                                                          | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `version`                                                              | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `status`                                                               | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | Lifecycle state of the skill — `active` or `deprecated`.               |