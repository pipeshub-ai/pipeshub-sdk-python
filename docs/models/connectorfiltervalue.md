# ConnectorFilterValue

A saved filter. Sync parses only entries that carry `operator` and `type`; one without `type` is saved but skipped when the connector syncs.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `operator`                                                               | *str*                                                                    | :heavy_check_mark:                                                       | One of the field's `operators`, for example `in` or `is_after`           |
| `value`                                                                  | *Any*                                                                    | :heavy_check_mark:                                                       | The filter value; its type follows `type`                                |
| `type`                                                                   | [models.ConnectorFilterValueType](../models/connectorfiltervaluetype.md) | :heavy_check_mark:                                                       | The field's `filterType` from the registry schema                        |