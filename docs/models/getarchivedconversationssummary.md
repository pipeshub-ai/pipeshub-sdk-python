# GetArchivedConversationsSummary


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `total_archived`                                                     | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Total archived conversations matching the filter                     |
| `oldest_archive`                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Archive timestamp of the first item in the current page              |
| `newest_archive`                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Archive timestamp of the last item in the current page               |