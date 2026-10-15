# Stats


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `total`                                                                            | *int*                                                                              | :heavy_check_mark:                                                                 | Records synced from the connector                                                  |
| `indexing_status`                                                                  | [models.ConnectorIndexingStatusCounts](../models/connectorindexingstatuscounts.md) | :heavy_check_mark:                                                                 | Number of records in each indexing status.                                         |