# FilterOption

A single filter option for knowledge hub filters.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Filter ID value to send in requests.                                |
| `label`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Display label for the filter.                                       |
| `type`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Additional type information (currently unused, may be null).        |
| `connector_type`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Connector type/name. Set only for entries in the `connectors` list. |