# Folder


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `key`                         | *Optional[str]*               | :heavy_minus_sign:            | Unique folder identifier      |
| `name`                        | *str*                         | :heavy_check_mark:            | Name of the folder            |
| `parent_id`                   | *Optional[str]*               | :heavy_minus_sign:            | Parent folder or KB ID        |
| `kb_id`                       | *str*                         | :heavy_check_mark:            | Knowledge base ID             |
| `org_id`                      | *str*                         | :heavy_check_mark:            | Organization ID               |
| `created_at_timestamp`        | *Optional[int]*               | :heavy_minus_sign:            | Creation timestamp            |
| `updated_at_timestamp`        | *Optional[int]*               | :heavy_minus_sign:            | Last update timestamp         |
| `is_deleted`                  | *Optional[bool]*              | :heavy_minus_sign:            | Whether the folder is deleted |