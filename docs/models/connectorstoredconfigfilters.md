# ConnectorStoredConfigFilters

Saved filter selections


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `sync`                                                                               | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | What to fetch from the source. Selections are under `values`, keyed by filter name.  |
| `indexing`                                                                           | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | Which fetched records to index. Selections are under `values`, keyed by filter name. |
| `__pydantic_extra__`                                                                 | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | N/A                                                                                  |