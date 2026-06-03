# RefreshTokenUser

User record returned with a refreshed access token


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | User ID            |
| `org_id`           | *str*              | :heavy_check_mark: | Organization ID    |
| `email`            | *str*              | :heavy_check_mark: | N/A                |
| `full_name`        | *str*              | :heavy_check_mark: | N/A                |
| `first_name`       | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `last_name`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `designation`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `has_logged_in`    | *bool*             | :heavy_check_mark: | N/A                |
| `is_deleted`       | *bool*             | :heavy_check_mark: | N/A                |
| `slug`             | *str*              | :heavy_check_mark: | N/A                |
| `created_at`       | *str*              | :heavy_check_mark: | N/A                |
| `updated_at`       | *str*              | :heavy_check_mark: | N/A                |
| `v`                | *int*              | :heavy_check_mark: | N/A                |