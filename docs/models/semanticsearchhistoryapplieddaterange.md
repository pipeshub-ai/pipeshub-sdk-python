# SemanticSearchHistoryAppliedDateRange

Echoed back only when the caller passed `startDate` and/or `endDate`.
Each bound is an ISO 8601 string when set; the field is absent when
the corresponding query param was omitted (utils.ts:480-486 reads
`appliedFilters.createdAt.$gte?.toISOString()` directly, so missing
bounds become `undefined` and drop out of the JSON).



## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `start`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `end`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |