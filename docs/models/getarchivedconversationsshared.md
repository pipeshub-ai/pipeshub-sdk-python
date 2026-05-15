# GetArchivedConversationsShared


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `values`                                       | List[*str*]                                    | :heavy_minus_sign:                             | Allowed values for the `shared` filter         |
| `description`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `current`                                      | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | Current value supplied by the caller, or null  |
| `applied`                                      | *Optional[bool]*                               | :heavy_minus_sign:                             | Whether this filter was applied on the request |