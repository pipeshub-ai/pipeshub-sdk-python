# DoclingCreateBlocksRequest

Request payload


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `parse_result`                               | *str*                                        | :heavy_check_mark:                           | JSON-encoded DoclingDocument from /parse-pdf |
| `page_number`                                | *Optional[int]*                              | :heavy_minus_sign:                           | Optional - process specific page only        |