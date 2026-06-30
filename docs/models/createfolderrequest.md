# CreateFolderRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `kb_id`                                                                | *str*                                                                  | :heavy_check_mark:                                                     | Knowledge base ID                                                      |
| `folder_id`                                                            | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Parent folder ID. Omit to create at the knowledge base root.           |
| `body`                                                                 | [models.CreateFolderRequestBody](../models/createfolderrequestbody.md) | :heavy_check_mark:                                                     | Request payload                                                        |