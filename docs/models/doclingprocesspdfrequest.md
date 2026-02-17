# DoclingProcessPdfRequest

Request payload


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `record_name`                   | *str*                           | :heavy_check_mark:              | Name/identifier of the document |
| `pdf_binary`                    | *str*                           | :heavy_check_mark:              | Base64 encoded PDF binary data  |
| `org_id`                        | *Optional[str]*                 | :heavy_minus_sign:              | Organization ID (optional)      |