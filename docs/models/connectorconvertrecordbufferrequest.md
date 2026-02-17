# ConnectorConvertRecordBufferRequest

Request payload


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `buffer`                                 | *str*                                    | :heavy_check_mark:                       | Base64 encoded file content              |
| `convert_to`                             | *str*                                    | :heavy_check_mark:                       | Target format (e.g., 'text', 'markdown') |
| `mime_type`                              | *Optional[str]*                          | :heavy_minus_sign:                       | Original MIME type of the file           |